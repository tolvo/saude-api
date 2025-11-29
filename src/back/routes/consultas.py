"""
Rotas para consultas complexas e relatórios
"""
from flask import request, jsonify
from database import get_connection
from queries.consultas_queries import (
    get_historico_cidadao_query,
    get_vacinas_atraso_query,
    get_consultas_unidade_query,
    get_pacientes_medicamento_query,
    get_cidadaos_todas_vacinas_query
)

def register_consultas_routes(app):
    """Registra as rotas de consultas complexas"""
    
    @app.route("/consultas/historico_cidadao/<cpf>", methods=["GET"])
    def historico_cidadao(cpf):
        """Histórico clínico completo de um cidadão (formato tabular)"""
        try:
            con = get_connection()
            cur = con.cursor()
            
            query = get_historico_cidadao_query()
            
            cur.execute(query, (cpf,))
            result = cur.fetchall()
            cur.close()
            con.close()
            
            return jsonify(result)
        except Exception as e:
            return jsonify({"erro": str(e)}), 500

    @app.route("/consultas/vacinas_atraso", methods=["GET"])
    def vacinas_atraso():
        """Cidadãos com vacinas em atraso"""
        try:
            ano_limite = request.args.get('ano', '1994')
            cod_vacina = int(request.args.get('vacina', '1'))
            
            con = get_connection()
            cur = con.cursor()
            
            query = get_vacinas_atraso_query()
            
            cur.execute(query, (ano_limite + '-01-01', cod_vacina))
            result = cur.fetchall()
            cur.close()
            con.close()
            
            return jsonify(result)
        except Exception as e:
            return jsonify({"erro": str(e)}), 500

    @app.route("/consultas/consultas_unidade", methods=["GET"])
    def consultas_unidade():
        """Consultas por unidade de saúde em um período"""
        try:
            data_inicio = request.args.get('inicio', '2023-01-01')
            data_fim = request.args.get('fim', '2023-12-31')
            
            con = get_connection()
            cur = con.cursor()
            
            query = get_consultas_unidade_query()
            
            cur.execute(query, (data_inicio, data_fim))
            result = cur.fetchall()
            cur.close()
            con.close()
            
            return jsonify(result)
        except Exception as e:
            return jsonify({"erro": str(e)}), 500

    @app.route("/consultas/pacientes_medicamento/<medicamento>", methods=["GET"])
    def pacientes_medicamento(medicamento):
        """Pacientes com prescrição de determinado medicamento"""
        try:
            con = get_connection()
            cur = con.cursor()
            
            query = get_pacientes_medicamento_query()
            
            cur.execute(query, (f'%{medicamento}%',))
            result = cur.fetchall()
            cur.close()
            con.close()
            
            return jsonify(result)
        except Exception as e:
            return jsonify({"erro": str(e)}), 500

    @app.route("/consultas/cidadaos_todas_vacinas", methods=["GET"])
    def cidadaos_todas_vacinas():
        """Cidadãos que tomaram todas as vacinas disponíveis (Divisão Relacional)"""
        try:
            con = get_connection()
            cur = con.cursor()
            
            query = get_cidadaos_todas_vacinas_query()
            
            cur.execute(query)
            result = cur.fetchall()
            cur.close()
            con.close()
            
            return jsonify(result)
        except Exception as e:
            return jsonify({"erro": str(e)}), 500
