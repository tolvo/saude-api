class Consulta:
    def __init__(self, cidadao_cpf: str, profissional_cpf: str, unidade_saude_cnes: str, data_consulta: str, relatorio_medico: str):
        self.cidadao_cpf = cidadao_cpf
        self.profissional_cpf = profissional_cpf
        self.unidade_saude_cnes = unidade_saude_cnes
        self.data_consulta = data_consulta 
        self.relatorio_medico = relatorio_medico
        self.receitas = []  # Lista de receitas associadas à consulta
        self.pedidos_exames = []  # Lista de pedidos de exames associados à consulta
    