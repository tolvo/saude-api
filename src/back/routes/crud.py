"""
Rotas básicas de CRUD para as tabelas do sistema
"""
from flask import request, jsonify
from database import get_connection

VALID_TABLES = [
    "CIDADAO", "ALERGIA", "UNIDADE_SAUDE", "VACINA", 
    "PROFISSIONAL", "ENFERMEIRO", "MEDICO", 
    "UNIDADE_BASICA_SAUDE", "HOSPITAL", "INTERNACAO", 
    "CIRURGIA", "CONSULTA", "VACINACAO", "EXAME", 
    "RECEITA", "PROFISSIONAL_ATUA_US", "MEDICO_CIRURGIA", 
    "ENFERMEIRO_CIRURGIA", "PROFISSIONAL_INTERNACAO"
]

def register_crud_routes(app):
    """Registra as rotas de CRUD básico"""
    
    @app.route("/<tabela>", methods=["GET"])
    def listar(tabela):
        """Lista todos os registros de uma tabela"""
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
        """Insere um novo registro em uma tabela"""
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
