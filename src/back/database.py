"""
Configuração e gerenciamento da conexão com o banco de dados
"""
import psycopg2
import os

# Configurações do banco de dados
db_host = os.getenv("DB_HOST", "postgres_db")
db_name = os.getenv("DB_NAME", "meubanco")
db_user = os.getenv("DB_USER", "admin")
db_pass = os.getenv("DB_PASS", "admin")

def get_connection():
    """
    Cria e retorna uma nova conexão com o banco de dados PostgreSQL
    
    Returns:
        psycopg2.connection: Objeto de conexão com o banco
    """
    return psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_pass
    )
