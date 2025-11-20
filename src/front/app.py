from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form/<tabela>")
def form(tabela):
    return render_template("form.html", tabela=tabela)

@app.route("/list/<tabela>")
def listar(tabela):
    return render_template("list.html", tabela=tabela)

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
