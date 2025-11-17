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

VALID_TABLES = ["CIDADAO", "ALERGIA"]

@app.route("/<tabela>", methods=["GET"])
def listar(tabela):
    tabela = tabela.upper()

    if tabela not in VALID_TABLES:
        return jsonify({"erro": "Tabela inválida"}), 404

    con = get_connection()
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {tabela}")
    result = cur.fetchall()
    cur.close()
    con.close()

    return jsonify(result)


@app.route("/<tabela>", methods=["POST"])
def inserir(tabela):
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
