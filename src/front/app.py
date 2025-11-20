from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

BACKEND_URL = "http://backend:5000"

html = """
<h1>Cadastro de Cidadao</h1>

<form method="POST">
  CPF: <input name="CPF" required><br><br>
  Nome: <input name="Nome" required><br><br>
  Data_nasc: <input name="Data_nasc" required><br><br>
  Sexo: <input name="Sexo" required><br><br>
  Endereco: <input name="Endereco" required><br><br>
  Telefone: <input name="Telefone" required><br><br>
  Tipo_sanguineo: <input name="Tipo_sanguineo" required><br><br>


  <button type="submit">Cadastrar</button>
</form>

<h2>Lista</h2>
<ul>
{% for p in cidadao %}
    <li> {{p[0][0]}} </li>
{% endfor %}
</ul>

<ul>
{% for p in cidadao %}

     <li>CPF:{{p[0]}} </li>
     <li>Nome:{{p[1]}} </li>
     <li>Data_nasc:{{p[2]}} </li>
     <li>Sexo:{{p[3]}} </li>
     <li>Endereco:{{p[4]}} </li>
     <li>Telefone:{{p[5]}} </li>
     <li>Tipo_sanguineo:{{p[6]}} </li>

{% endfor %}
</ul>
"""

html_historico = """
<h1>Histórico Clínico</h1>

<form method="GET" action="/historico">
  CPF: <input name="cpf" required><br><br>
  <button type="submit">Consultar</button>
</form>

{% if historico %}
<h2>Histórico de {{cpf}}</h2>
<ul>
{% for h in historico %}
    <li>Data Consulta: {{h[1]}}, Relatório: {{h[2]}}, Exame: {{h[3]}}, Medicamento: {{h[5]}}, Vacina: {{h[6]}}, Cirurgia: {{h[7]}}, Internação: {{h[8]}}</li>
{% endfor %}
</ul>
{% endif %}
"""

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        requests.post(f"{BACKEND_URL}/cidadao", json={
            "CPF": request.form["CPF"],
            "Nome": request.form["Nome"],
            "Data_nasc": request.form["Data_nasc"],
            "Sexo": request.form["Sexo"],
            "Endereco": request.form["Endereco"],
            "Telefone": request.form["Telefone"],
            "Tipo_sanguineo": request.form["Tipo_sanguineo"]
        })
    cidadao = requests.get(f"{BACKEND_URL}/cidadao").json()
    return render_template_string(html, cidadao=cidadao)

@app.route("/historico", methods=["GET"])
def historico():
    cpf = request.args.get("cpf")
    historico_data = []
    if cpf:
        response = requests.get(f"{BACKEND_URL}/historico/{cpf}")
        if response.status_code == 200:
            historico_data = response.json()
    return render_template_string(html_historico, historico=historico_data, cpf=cpf)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


