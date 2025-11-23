"""
Aplicação Principal do Backend - PEC (Prontuário Eletrônico do Cidadão)
Sistema de gestão de dados urbanos em saúde

Estrutura:
- database.py: Gerenciamento de conexões com PostgreSQL
- routes/: Módulos de rotas organizados por funcionalidade
  - crud.py: Operações básicas de CRUD
  - cidadao.py: Busca completa de informações do cidadão
  - consultas.py: Consultas complexas e relatórios
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from flask_cors import CORS
from routes import register_all_routes

# Inicializa a aplicação Flask
app = Flask(__name__)
CORS(app)

# Registra todas as rotas da aplicação
register_all_routes(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
