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



    print(data)
    CPF = data["CPF"]
    Nome = data["Nome"]
    Data_nasc = data["Data_nasc"]
    Sexo = data["Sexo"]
    Endereco = data["Endereco"]
    Telefone = data["Telefone"]
    Tipo_sanguineo = data["Tipo_sanguineo"]

    con = get_connection()
    cur = con.cursor()
    cur.execute("INSERT INTO cidadao (CPF, Nome, Data_nasc, Sexo, Endereco, Telefone, Tipo_sanguineo) VALUES (%s, %s, %s, %s, %s, %s, %s);", (CPF, Nome, Data_nasc, Sexo, Endereco, Telefone, Tipo_sanguineo))
    con.commit()
    cur.close()
    con.close()
    return {"status": "Inserido"}, 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
