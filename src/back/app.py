from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

db_host = os.getenv("DB_HOST", "postgres_db")
db_name = os.getenv("DB_NAME", "meubanco")
db_user = os.getenv("DB_USER", "admin")
db_pass = os.getenv("DB_PASS", "admin")

def get_connection():
    return psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_pass
    )

VALID_TABLES = ["CIDADAO", "ALERGIA", "UNIDADE_SAUDE", "VACINA", "PROFISSIONAL", "ENFERMEIRO", "MEDICO", "UNIDADE_BASICA_SAUDE", "HOSPITAL", "INTERNACAO", "CIRURGIA", "CONSULTA", "VACINACAO", "EXAME", "RECEITA", "PROFISSIONAL_ATUA_US", "MEDICO_CIRURGIA", "ENFERMEIRO_CIRURGIA", "PROFISSIONAL_INTERNACAO"]

@app.route("/<tabela>", methods=["GET"])
def listar(tabela):
    tabela = tabela.upper()

    if tabela not in VALID_TABLES:
        return jsonify({"erro": "Tabela inválida"}), 404

    sql = f"SELECT * FROM {tabela}"

    filtros = []
    for chave, valor in request.args.items():
        filtros.append(f"{chave} = %s")
    if filtros:
        sql += " WHERE " + " AND ".join(filtros)
    
    con = get_connection()
    cur = con.cursor()
    cur.execute(sql, list(request.args.values()))
    result = cur.fetchall()
    cur.close()
    con.close()

    return jsonify(result)

@app.route("/<tabela>", methods=["POST"])
def inserir(tabela):
    try:    
        tabela = tabela.upper()
        if tabela not in VALID_TABLES:
            return jsonify({"erro": "Tabela inválida"}), 404
        
        data = request.json
        campos = ', '.join(data.keys())
        valores = ', '.join(['%s'] * len(data))

        con = get_connection()
        cur = con.cursor()
        cur.execute(
            f"INSERT INTO {tabela.upper()} ({campos}) VALUES ({valores})",
            list(data.values())
        )
        con.commit()
        cur.close()
        con.close()

        return jsonify({"mensagem": "Inserido!"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# Consultas "complexas"
# TODO: REVISAR TODAS AS CONSULTAS ABAIXO
@app.route("/consultas/historico_cidadao/<cpf>", methods=["GET"])
def historico_cidadao(cpf):
    """Histórico clínico completo de um cidadão"""
    try:
        con = get_connection()
        cur = con.cursor()
        
        query = """
        SELECT 
            c.Nome as cidadao,
            cons.Data_consulta as data_consulta,
            cons.Relatorio_medico as relatorio_medico,
            e.Tipo_exame as tipo_exame,
            e.Data_realizacao as data_exame,
            r.Medicamento,
            v.Nome as vacina,
            cir.Nome_procedimento,
            i.Motivo as motivo_internacao
        FROM cidadao c
        LEFT JOIN consulta cons ON c.CPF = cons.CPF_cidadao
        LEFT JOIN exame e ON cons.CPF_cidadao = e.CPF_cidadao AND cons.CPF_medico = e.CPF_medico AND cons.Data_consulta = e.Data_consulta
        LEFT JOIN receita r ON cons.CPF_cidadao = r.CPF_cidadao AND cons.CPF_medico = r.CPF_medico AND cons.Data_consulta = r.Data_consulta
        LEFT JOIN vacinacao vac ON c.CPF = vac.CPF_cidadao
        LEFT JOIN vacina v ON vac.Lote_vacina = v.Lote AND vac.Cod_vacina = v.Cod_vacina
        LEFT JOIN cirurgia cir ON c.CPF = cir.CPF_cidadao
        LEFT JOIN internacao i ON c.CPF = i.CPF_cidadao
        WHERE c.CPF = %s
        ORDER BY cons.Data_consulta DESC NULLS LAST
        """
        
        cur.execute(query, (cpf,))
        result = cur.fetchall()
        cur.close()
        con.close()
        
        return jsonify(result)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route("/consultas/vacinas_atraso", methods=["GET"])
def vacinas_atraso():
    """Cidadãos com vacinas em atraso"""
    try:
        ano_limite = request.args.get('ano', '1994')
        cod_vacina = request.args.get('vacina', 'VAC001')
        
        con = get_connection()
        cur = con.cursor()
        
        query = """
        SELECT c.CPF, c.Nome, c.Data_nasc
        FROM cidadao c
        WHERE c.Data_nasc > %s
        AND NOT EXISTS (
            SELECT 1 FROM vacinacao v 
            WHERE v.CPF_cidadao = c.CPF AND v.Cod_vacina = %s
        )
        ORDER BY c.Data_nasc DESC
        """
        
        cur.execute(query, (ano_limite + '-01-01', cod_vacina))
        result = cur.fetchall()
        cur.close()
        con.close()
        
        return jsonify(result)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route("/consultas/consultas_unidade", methods=["GET"])
def consultas_unidade():
    """Consultas por unidade de saúde em um período"""
    try:
        data_inicio = request.args.get('inicio', '2023-01-01')
        data_fim = request.args.get('fim', '2023-12-31')
        
        con = get_connection()
        cur = con.cursor()
        
        query = """
        SELECT u.Nome as unidade, COUNT(*) as numero_consultas
        FROM unidade_saude u
        JOIN consulta cons ON u.CNES = cons.CNES_unidade
        WHERE cons.Data_consulta BETWEEN %s AND %s
        GROUP BY u.CNES, u.Nome
        ORDER BY numero_consultas DESC
        """
        
        cur.execute(query, (data_inicio, data_fim))
        result = cur.fetchall()
        cur.close()
        con.close()
        
        return jsonify(result)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route("/consultas/pacientes_medicamento/<medicamento>", methods=["GET"])
def pacientes_medicamento(medicamento):
    """Pacientes com prescrição de determinado medicamento"""
    try:
        con = get_connection()
        cur = con.cursor()
        
        query = """
        SELECT DISTINCT c.CPF, c.Nome, r.Medicamento, r.Dosagem, r.Duracao
        FROM cidadao c
        JOIN receita r ON c.CPF = r.CPF_cidadao
        WHERE r.Medicamento ILIKE %s
        ORDER BY c.Nome
        """
        
        cur.execute(query, (f'%{medicamento}%',))
        result = cur.fetchall()
        cur.close()
        con.close()
        
        return jsonify(result)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route("/consultas/cidadaos_todas_vacinas", methods=["GET"])
def cidadaos_todas_vacinas():
    """Cidadãos que tomaram todas as vacinas disponíveis (Divisão Relacional)"""
    try:
        con = get_connection()
        cur = con.cursor()
        
        query = """
        SELECT c.CPF, c.Nome
        FROM cidadao c
        WHERE NOT EXISTS (
            SELECT v.Lote, v.Cod_vacina
            FROM vacina v
            EXCEPT
            SELECT vac.Lote_vacina, vac.Cod_vacina
            FROM vacinacao vac
            WHERE vac.CPF_cidadao = c.CPF
        )
        ORDER BY c.Nome
        """
        
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        con.close()
        
        return jsonify(result)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
