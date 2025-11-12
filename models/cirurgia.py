class Cirurgia:
    def __init__(self, cidadao_cpf: str, medicos_cpfs: list, enfermeiros_cpfs: list, nome_procedimento: str, duracao: str, data_realizacao: str, observacoes_medicas: str, cuidados_posteriores: str):
        self.cidadao_cpf = cidadao_cpf
        self.medicos_cpfs = medicos_cpfs  # Lista de CPFs dos médicos
        self.enfermeiros_cpfs = enfermeiros_cpfs  # Lista de CPFs dos enfermeiros
        self.nome_procedimento = nome_procedimento
        self.duracao = duracao
        self.data_realizacao = data_realizacao
        self.observacoes_medicas = observacoes_medicas
        self.cuidados_posteriores = cuidados_posteriores