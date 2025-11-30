"""
Queries para cidadão
"""

def get_cidadao_basic_query():
    return """
        SELECT cpf, nome, data_nasc, sexo, endereco, telefone, tipo_sanguineo
        FROM cidadao
        WHERE cpf = %s
    """

def get_alergias_query():
    return "SELECT alergia FROM alergia WHERE cpf = %s"

def get_consultas_query():
    return """
        SELECT c.data, c.relatorio, c.unidade_saude,
               m.nome as medico_nome, u.nome as unidade_nome
        FROM consulta c
        LEFT JOIN medico med ON c.medico = med.cpf
        LEFT JOIN profissional m ON med.cpf = m.cpf
        LEFT JOIN unidade_saude u ON c.unidade_saude = u.cnes
        WHERE c.cidadao = %s
        ORDER BY c.data DESC
    """

def get_exames_query():
    return """
        SELECT e.tipo, e.data_realiza, e.local, e.link, e.data
        FROM exame e
        WHERE e.cidadao = %s
        ORDER BY e.data_realiza DESC
    """

def get_receitas_query():
    return """
        SELECT r.medicamento, r.dosagem, r.duracao, r.data
        FROM receita r
        WHERE r.cidadao = %s
        ORDER BY r.data DESC
    """

def get_vacinacoes_query():
    return """
        SELECT v.nome_popular, vac.dose, vac.data, u.nome as unidade_nome
        FROM vacinacao vac
        JOIN vacina v ON vac.vacina_lote = v.lote AND vac.vacina_cod = v.cod
        LEFT JOIN unidade_saude u ON vac.ubs = u.cnes
        WHERE vac.cidadao = %s
        ORDER BY vac.data DESC
    """

def get_cirurgias_query():
    return """
        SELECT c.nome_procedimento, c.data_realizacao, c.duracao,
               c.observacao, c.cuidados_posteriores, h.nome as hospital_nome
        FROM cirurgia c
        LEFT JOIN hospital hosp ON c.cnes = hosp.cnes
        LEFT JOIN unidade_saude h ON hosp.cnes = h.cnes
        WHERE c.cidadao = %s
        ORDER BY c.data_realizacao DESC
    """

def get_internacoes_query():
    return """
        SELECT i.data_entrada, i.data_alta, i.motivo, i.ala_hospitalar,
               h.nome as hospital_nome
        FROM internacao i
        LEFT JOIN hospital hosp ON i.cnes = hosp.cnes
        LEFT JOIN unidade_saude h ON hosp.cnes = h.cnes
        WHERE i.cidadao = %s
        ORDER BY i.data_entrada DESC
    """