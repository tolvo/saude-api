"""
Queries para consultas complexas
"""

def get_historico_cidadao_query():
    return """
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

def get_vacinas_atraso_query():
    return """
    SELECT c.cpf, c.nome, c.data_nasc
    FROM cidadao c
    WHERE c.data_nasc > %s
    AND NOT EXISTS (
        SELECT 1 FROM vacinacao v
        WHERE v.cidadao = c.cpf AND v.vacina_cod = %s
    )
    ORDER BY c.data_nasc DESC
    """

def get_consultas_unidade_query():
    return """
    SELECT u.nome as unidade, COUNT(*) as numero_consultas
    FROM unidade_saude u
    JOIN consulta cons ON u.cnes = cons.unidade_saude
    WHERE cons.data BETWEEN %s AND %s
    GROUP BY u.cnes, u.nome
    ORDER BY numero_consultas DESC
    """

def get_pacientes_medicamento_query():
    return """
    SELECT DISTINCT c.cpf, c.nome, r.medicamento, r.dosagem, r.duracao
    FROM cidadao c
    JOIN receita r ON c.cpf = r.cidadao
    WHERE r.medicamento ILIKE %s
    ORDER BY c.nome
    """

def get_cidadaos_todas_vacinas_query():
    return """
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