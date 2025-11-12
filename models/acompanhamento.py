class Acompanhamento:
    def __init__(self, internacao_id: str, profissional_cpf: str, data_hora: str, observacoes: str):
        self.internacao_id = internacao_id
        self.profissional_cpf = profissional_cpf
        self.data_hora = data_hora
        self.observacoes = observacoes
