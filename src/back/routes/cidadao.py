"""
Rotas para busca completa de informações do cidadão
"""
from flask import jsonify
from database import get_connection
from queries.cidadao_queries import (
    get_cidadao_basic_query,
    get_alergias_query,
    get_consultas_query,
    get_exames_query,
    get_receitas_query,
    get_vacinacoes_query,
    get_cirurgias_query,
    get_internacoes_query
)
from datetime import date, datetime, time, timedelta

from datetime import date, datetime, time, timedelta

def to_json_safe(value):
    if isinstance(value, datetime):
        return value.isoformat()
    elif isinstance(value, date):
        return value.isoformat()
    elif isinstance(value, time):
        return value.strftime("%H:%M:%S")
    elif isinstance(value, timedelta):
        return str(value)
    return value


def register_cidadao_routes(app):
    """Registra as rotas relacionadas a cidadãos"""
    
    @app.route("/cidadao/buscar/<cpf>", methods=["GET"])
    def buscar_cidadao_completo(cpf):
        """Busca todas as informações de um cidadão por CPF"""
        try:
            con = get_connection()
            cur = con.cursor()
            
            cur.execute(get_cidadao_basic_query(), (cpf,))
            
            cidadao = cur.fetchone()
            
            if not cidadao:
                cur.close()
                con.close()
                return jsonify({"erro": "Cidadão não encontrado"}), 404
            
            resultado = {
                "dados_basicos": {
                    "cpf": cidadao[0],
                    "nome": cidadao[1],
                    "data_nascimento": str(cidadao[2]) if cidadao[2] else None,
                    "sexo": cidadao[3],
                    "endereco": cidadao[4],
                    "telefone": cidadao[5],
                    "tipo_sanguineo": cidadao[6]
                }
            }
            
            cur.execute(get_alergias_query(), (cpf,))
            resultado["alergias"] = [row[0] for row in cur.fetchall()]
            
            cur.execute(get_consultas_query(), (cpf,))
            resultado["consultas"] = [{
                "data": str(row[0]) if row[0] else None,
                "relatorio": row[1],
                "cnes_unidade": row[2],
                "medico": row[3],
                "unidade": row[4]
            } for row in cur.fetchall()]
            
            cur.execute(get_exames_query(), (cpf,))
            resultado["exames"] = [{
                "tipo": row[0],
                "data_realizacao": str(row[1]) if row[1] else None,
                "local": row[2],
                "link_resultado": row[3],
                "data_consulta": str(row[4]) if row[4] else None
            } for row in cur.fetchall()]
            
            cur.execute(get_receitas_query(), (cpf,))
            resultado["receitas"] = [{
                "medicamento": row[0],
                "dosagem": row[1],
                "duracao": row[2],
                "data_consulta": str(row[3]) if row[3] else None
            } for row in cur.fetchall()]
            
            cur.execute(get_vacinacoes_query(), (cpf,))
            resultado["vacinacoes"] = [{
                "vacina": row[0],
                "dose": row[1],
                "data_aplicacao": str(row[2]) if row[2] else None,
                "unidade": row[3]
            } for row in cur.fetchall()]
            
            cur.execute(get_cirurgias_query(), (cpf,))
            resultado["cirurgias"] = [{
                "nome_procedimento": row[0],
                "data_realizacao": to_json_safe(row[1]),
                "duracao": to_json_safe(row[2]),
                "observacao": row[3],
                "cuidados_posteriores": row[4],
                "hospital_nome": row[5]
            } for row in cur.fetchall()]

            
            cur.execute(get_internacoes_query(), (cpf,))
            resultado["internacoes"] = [{
                "data_entrada": str(row[0]) if row[0] else None,
                "data_alta": str(row[1]) if row[1] else None,
                "motivo": row[2],
                "ala": row[3],
                "hospital": row[4]
            } for row in cur.fetchall()]
            
            cur.close()
            con.close()
            
            return jsonify(resultado)
            
        except Exception as e:
            return jsonify({"erro": str(e)}), 500
