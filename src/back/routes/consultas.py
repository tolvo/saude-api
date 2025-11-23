"""
Rotas para consultas complexas e relatórios
"""
from flask import request, jsonify
from database import get_connection

def register_consultas_routes(app):
    """Registra as rotas de consultas complexas"""
    
    @app.route("/consultas/historico_cidadao/<cpf>", methods=["GET"])
    def historico_cidadao(cpf):
        """Histórico clínico completo de um cidadão (formato tabular)"""
        try:
            con = get_connection()
            cur = con.cursor()
            
            query = """
            SELECT 
                c.nome as cidadao,
                cons.data as data_consulta,
                cons.relatorio as relatorio_medico,
                e.tipo as tipo_exame,
                e.data_realiza as data_exame,
                r.medicamento,
                v.nome_popular as vacina,
                cir.nome_procedimento,
                i.motivo as motivo_internacao
            FROM cidadao c
            LEFT JOIN consulta cons ON c.cpf = cons.cidadao
            LEFT JOIN exame e ON cons.cidadao = e.cidadao AND cons.medico = e.medico AND cons.data = e.data
            LEFT JOIN receita r ON cons.cidadao = r.cidadao AND cons.medico = r.medico AND cons.data = r.data
            LEFT JOIN vacinacao vac ON c.cpf = vac.cidadao
            LEFT JOIN vacina v ON vac.vacina_lote = v.lote AND vac.vacina_cod = v.cod
            LEFT JOIN cirurgia cir ON c.cpf = cir.cidadao
            LEFT JOIN internacao i ON c.cpf = i.cidadao
            WHERE c.cpf = %s
            ORDER BY cons.data DESC NULLS LAST
            """
            
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
            
            query = """
            SELECT c.cpf, c.nome, c.data_nasc
            FROM cidadao c
            WHERE c.data_nasc > %s
            AND NOT EXISTS (
                SELECT 1 FROM vacinacao v 
                WHERE v.cidadao = c.cpf AND v.vacina_cod = %s
            )
            ORDER BY c.data_nasc DESC
            """
            
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
            
            query = """
            SELECT u.nome as unidade, COUNT(*) as numero_consultas
            FROM unidade_saude u
            JOIN consulta cons ON u.cnes = cons.unidade_saude
            WHERE cons.data BETWEEN %s AND %s
            GROUP BY u.cnes, u.nome
            ORDER BY numero_consultas DESC
            """
            
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
            
            query = """
            SELECT DISTINCT c.cpf, c.nome, r.medicamento, r.dosagem, r.duracao
            FROM cidadao c
            JOIN receita r ON c.cpf = r.cidadao
            WHERE r.medicamento ILIKE %s
            ORDER BY c.nome
            """
            
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
            
            query = """
            SELECT c.cpf, c.nome
            FROM cidadao c
            WHERE NOT EXISTS (
                SELECT v.lote, v.cod
                FROM vacina v
                EXCEPT
                SELECT vac.vacina_lote, vac.vacina_cod
                FROM vacinacao vac
                WHERE vac.cidadao = c.cpf
            )
            ORDER BY c.nome
            """
            
            cur.execute(query)
            result = cur.fetchall()
            cur.close()
            con.close()
            
            return jsonify(result)
        except Exception as e:
            return jsonify({"erro": str(e)}), 500
