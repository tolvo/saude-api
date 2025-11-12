class Vacinacao:
    def __init__(self, cidadao_cpf: str, enfermeiro_cpf: str, unidade_saude_cnes: str, codigo_vacina: str, data_aplicacao: str):
        self.cidadao_cpf = cidadao_cpf
        self.enfermeiro_cpf = enfermeiro_cpf
        self.unidade_saude_cnes = unidade_saude_cnes
        self.codigo_vacina = codigo_vacina
        self.data_aplicacao = data_aplicacao