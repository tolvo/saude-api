class Internacao:
    def __init__(self, cidadao_cpf: str, data_entrada: str, data_alta: str, motivo_internacao: str, ala_hospitalar: str):
        self.cidadao_cpf = cidadao_cpf
        self.data_entrada = data_entrada
        self.data_alta = data_alta
        self.motivo_internacao = motivo_internacao
        self.ala_hospitalar = ala_hospitalar
        self.profissionais_saude = []  # Lista de CPFs dos profissionais de saúde que acompanham a internação
