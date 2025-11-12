class UnidadeSaude:
    def __init__(self, cnes: str, tipo: str, nome: str, endereco: str, horario_funcionamento: str):
        self.cnes = cnes
        self.tipo = tipo  # "Unidade Básica de Saúde" ou "Hospital"
        self.nome = nome
        self.endereco = endereco
        self.horario_funcionamento = horario_funcionamento
        if self.tipo == "Hospital":
            self.capacidade = None
            self.lotacao_atual = 0 
        