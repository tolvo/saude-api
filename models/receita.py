class Receita:
    def __init__(self, consulta_id: str, medicamento: str, dosagem: str, duracao_tratamento: str):
        self.consulta_id = consulta_id
        self.medicamento = medicamento
        self.dosagem = dosagem
        self.duracao_tratamento = duracao_tratamento