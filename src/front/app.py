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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
