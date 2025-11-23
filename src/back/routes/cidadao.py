"""
Rotas para busca completa de informações do cidadão
"""
from flask import jsonify
from database import get_connection

def register_cidadao_routes(app):
    """Registra as rotas relacionadas a cidadãos"""
    
    @app.route("/cidadao/buscar/<cpf>", methods=["GET"])
    def buscar_cidadao_completo(cpf):
        """Busca todas as informações de um cidadão por CPF"""
        try:
            con = get_connection()
            cur = con.cursor()
            
            # Dados básicos do cidadão
            cur.execute("""
                SELECT cpf, nome, data_nasc, sexo, endereco, telefone, tipo_sanguineo
                FROM cidadao
                WHERE cpf = %s
            """, (cpf,))
            
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
            
            # Alergias
            cur.execute("SELECT alergia FROM alergia WHERE cpf = %s", (cpf,))
            resultado["alergias"] = [row[0] for row in cur.fetchall()]
            
            # Consultas
            cur.execute("""
                SELECT c.data, c.relatorio, c.unidade_saude, 
                       m.nome as medico_nome, u.nome as unidade_nome
                FROM consulta c
                LEFT JOIN medico med ON c.medico = med.cpf
                LEFT JOIN profissional m ON med.cpf = m.cpf
                LEFT JOIN unidade_saude u ON c.unidade_saude = u.cnes
                WHERE c.cidadao = %s
                ORDER BY c.data DESC
            """, (cpf,))
            resultado["consultas"] = [{
                "data": str(row[0]) if row[0] else None,
                "relatorio": row[1],
                "cnes_unidade": row[2],
                "medico": row[3],
                "unidade": row[4]
            } for row in cur.fetchall()]
            
            # Exames
            cur.execute("""
                SELECT e.tipo, e.data_realiza, e.local, e.link, e.data
                FROM exame e
                WHERE e.cidadao = %s
                ORDER BY e.data_realiza DESC
            """, (cpf,))
            resultado["exames"] = [{
                "tipo": row[0],
                "data_realizacao": str(row[1]) if row[1] else None,
                "local": row[2],
                "link_resultado": row[3],
                "data_consulta": str(row[4]) if row[4] else None
            } for row in cur.fetchall()]
            
            # Receitas
            cur.execute("""
                SELECT r.medicamento, r.dosagem, r.duracao, r.data
                FROM receita r
                WHERE r.cidadao = %s
                ORDER BY r.data DESC
            """, (cpf,))
            resultado["receitas"] = [{
                "medicamento": row[0],
                "dosagem": row[1],
                "duracao": row[2],
                "data_consulta": str(row[3]) if row[3] else None
            } for row in cur.fetchall()]
            
            # Vacinações
            cur.execute("""
                SELECT v.nome_popular, vac.dose, vac.data, u.nome as unidade_nome
                FROM vacinacao vac
                JOIN vacina v ON vac.vacina_lote = v.lote AND vac.vacina_cod = v.cod
                LEFT JOIN unidade_saude u ON vac.ubs = u.cnes
                WHERE vac.cidadao = %s
                ORDER BY vac.data DESC
            """, (cpf,))
            resultado["vacinacoes"] = [{
                "vacina": row[0],
                "dose": row[1],
                "data_aplicacao": str(row[2]) if row[2] else None,
                "unidade": row[3]
            } for row in cur.fetchall()]
            
            # Cirurgias
            cur.execute("""
                SELECT c.nome_procedimento, c.data_realizacao, c.duracao, 
                       c.observacao, c.cuidados_posteriores, h.nome as hospital_nome
                FROM cirurgia c
                LEFT JOIN hospital hosp ON c.cnes = hosp.cnes
                LEFT JOIN unidade_saude h ON hosp.cnes = h.cnes
                WHERE c.cidadao = %s
                ORDER BY c.data_realizacao DESC
            """, (cpf,))
            resultado["cirurgias"] = [{
                "procedimento": row[0],
                "data_realizacao": str(row[1]) if row[1] else None,
                "duracao": str(row[2]) if row[2] else None,
                "observacoes": row[3],
                "cuidados": row[4],
                "hospital": row[5]
            } for row in cur.fetchall()]
            
            # Internações
            cur.execute("""
                SELECT i.data_entrada, i.data_alta, i.motivo, i.ala_hospitalar, 
                       h.nome as hospital_nome
                FROM internacao i
                LEFT JOIN hospital hosp ON i.cnes = hosp.cnes
                LEFT JOIN unidade_saude h ON hosp.cnes = h.cnes
                WHERE i.cidadao = %s
                ORDER BY i.data_entrada DESC
            """, (cpf,))
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
