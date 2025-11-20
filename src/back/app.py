from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

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

@app.route("/cidadao", methods=["GET"])
def listar():
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM cidadao")
    result = cur.fetchall()
    cur.close()
    con.close()
    return jsonify(result)

@app.route("/cidadao", methods=["POST"])
def inserir():
    data = request.json
    CPF = data["CPF"]
    Nome = data["Nome"]
    Data_nasc = data["Data_nasc"]
    Sexo = data["Sexo"]
    Endereco = data["Endereco"]
    Telefone = data["Telefone"]
    Tipo_sanguineo = data["Tipo_sanguineo"]
    Alergias = data.get("Alergias", [])

    con = None
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("INSERT INTO cidadao (CPF, Nome, Data_nasc, Sexo, Endereco, Telefone, Tipo_sanguineo) VALUES (%s, %s, %s, %s, %s, %s, %s);", (CPF, Nome, Data_nasc, Sexo, Endereco, Telefone, Tipo_sanguineo))
        for alergia in Alergias:
            cur.execute("INSERT INTO alergia_cidadao (CPF, Alergia) VALUES (%s, %s);", (CPF, alergia))
        con.commit()
        return {"status": "Inserido"}, 201
    except Exception as e:
        if con:
            con.rollback()
        return {"error": str(e)}, 400
    finally:
        if con:
            con.close()

@app.route("/profissional", methods=["POST"])
def inserir_profissional():
    data = request.json
    CPF = data["CPF"]
    Nome = data["Nome"]
    Tipo = data["Tipo"]

    con = None
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("INSERT INTO profissional (CPF, Nome, Tipo) VALUES (%s, %s, %s);", (CPF, Nome, Tipo))
        if Tipo == "Médico":
            CRM = data["CRM"]
            Especialidade = data.get("Especialidade")
            cur.execute("INSERT INTO medico (CPF, CRM, Especialidade) VALUES (%s, %s, %s);", (CPF, CRM, Especialidade))
        elif Tipo == "Enfermeiro":
            COREN = data["COREN"]
            cur.execute("INSERT INTO enfermeiro (CPF, COREN) VALUES (%s, %s);", (CPF, COREN))
        con.commit()
        return {"status": "Profissional inserido"}, 201
    except Exception as e:
        if con:
            con.rollback()
        return {"error": str(e)}, 400
    finally:
        if con:
            con.close()

@app.route("/unidade_saude", methods=["POST"])
def inserir_unidade():
    data = request.json
    CNES = data["CNES"]
    Tipo = data["Tipo"]
    Nome = data["Nome"]
    Endereco = data["Endereco"]
    Horario_func = data["Horario_func"]

    con = None
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("INSERT INTO unidade_saude (CNES, Tipo, Nome, Endereco, Horario_func) VALUES (%s, %s, %s, %s, %s);", (CNES, Tipo, Nome, Endereco, Horario_func))
        if Tipo == "Hospital":
            Capacidade = data["Capacidade"]
            cur.execute("INSERT INTO hospital (CNES, Capacidade) VALUES (%s, %s);", (CNES, Capacidade))
        elif Tipo == "Unidade Básica de Saúde":
            cur.execute("INSERT INTO unidade_basica (CNES) VALUES (%s);", (CNES,))
        con.commit()
        return {"status": "Unidade inserida"}, 201
    except Exception as e:
        if con:
            con.rollback()
        return {"error": str(e)}, 400
    finally:
        if con:
            con.close()

@app.route("/consulta", methods=["POST"])
def inserir_consulta():
    data = request.json
    CPF_cidadao = data["CPF_cidadao"]
    CPF_medico = data["CPF_medico"]
    Data_consulta = data["Data_consulta"]
    CNES_unidade = data["CNES_unidade"]
    Relatorio_medico = data["Relatorio_medico"]

    con = None
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("INSERT INTO consulta (CPF_cidadao, CPF_medico, Data_consulta, CNES_unidade, Relatorio_medico) VALUES (%s, %s, %s, %s, %s);", (CPF_cidadao, CPF_medico, Data_consulta, CNES_unidade, Relatorio_medico))
        con.commit()
        return {"status": "Consulta inserida"}, 201
    except Exception as e:
        if con:
            con.rollback()
        return {"error": str(e)}, 400
    finally:
        if con:
            con.close()

@app.route("/historico/<cpf>", methods=["GET"])
def historico_clinico(cpf):
    con = None
    try:
        con = get_connection()
        cur = con.cursor()
        query = """
        SELECT c.Nome, cons.Data_consulta, cons.Relatorio_medico, e.Tipo_exame, e.Data_realizacao, r.Medicamento, v.Nome AS Vacina, cir.Nome_procedimento, i.Motivo
        FROM cidadao c
        LEFT JOIN consulta cons ON c.CPF = cons.CPF_cidadao
        LEFT JOIN exame e ON cons.CPF_cidadao = e.CPF_cidadao AND cons.CPF_medico = e.CPF_medico AND cons.Data_consulta = e.Data_consulta
        LEFT JOIN receita r ON cons.CPF_cidadao = r.CPF_cidadao AND cons.CPF_medico = r.CPF_medico AND cons.Data_consulta = r.Data_consulta
        LEFT JOIN vacinacao vac ON c.CPF = vac.CPF_cidadao
        LEFT JOIN vacina v ON vac.Lote_vacina = v.Lote AND vac.Cod_vacina = v.Cod_vacina
        LEFT JOIN cirurgia cir ON c.CPF = cir.CPF_cidadao
        LEFT JOIN internacao i ON c.CPF = i.CPF_cidadao
        WHERE c.CPF = %s;
        """
        cur.execute(query, (cpf,))
        result = cur.fetchall()
        return jsonify(result)
    except Exception as e:
        return {"error": str(e)}, 400
    finally:
        if con:
            con.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
