"""
Pacote de rotas do backend
Organiza todas as rotas em módulos separados
"""
from .crud import register_crud_routes
from .cidadao import register_cidadao_routes
from .consultas import register_consultas_routes

def register_all_routes(app):
    """
    Registra todas as rotas da aplicação
    
    Args:
        app: Instância do Flask
    """
    register_crud_routes(app)
    register_cidadao_routes(app)
    register_consultas_routes(app)
