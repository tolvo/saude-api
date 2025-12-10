"""
Rotas básicas de CRUD para as tabelas do sistema
"""
from flask import request, jsonify
from database import get_connection
from datetime import date, datetime, time, timedelta

VALID_TABLES = [
    "CIDADAO", "ALERGIA", "UNIDADE_SAUDE", "VACINA", 
    "PROFISSIONAL", "ENFERMEIRO", "MEDICO", 
    "UNIDADE_BASICA_SAUDE", "HOSPITAL", "INTERNACAO", 
    "CIRURGIA", "CONSULTA", "VACINACAO", "EXAME", 
    "RECEITA", "PROFISSIONAL_ATUA_US", "MEDICO_CIRURGIA", 
    "ENFERMEIRO_CIRURGIA", "PROFISSIONAL_INTERNACAO"
]

def to_json_safe(value):
    """Converte tipos não serializáveis pelo Flask para strings."""
    if isinstance(value, datetime):
        return value.isoformat()
    elif isinstance(value, date):
        return value.isoformat()
    elif isinstance(value, time):
        return value.strftime("%H:%M:%S")
    elif isinstance(value, timedelta):
        return str(value)
    return value


def serialize_rows(cur, rows):
    """Converte rows do banco em dicionários JSON-safe."""
    cols = [desc[0] for desc in cur.description]
    return [
        {cols[i]: to_json_safe(row[i]) for i in range(len(cols))}
        for row in rows
    ]


def register_crud_routes(app):
    """Registra as rotas de CRUD básico"""
    
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
        rows = cur.fetchall()

        result = serialize_rows(cur, rows)

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
                f"INSERT INTO {tabela} ({campos}) VALUES ({valores})",
                list(data.values())
            )

            con.commit()
            cur.close()
            con.close()

            return jsonify({"mensagem": "Inserido!"})
        
        except Exception as e:
            return jsonify({"erro": str(e)}), 500
