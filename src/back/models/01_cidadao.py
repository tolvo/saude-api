class Cidadao:
    def __init__(self, nome: str, idade: int, cpf: str, data_nascimento: str, endereco: str, contato: str, alergias: list, tipo_sanguineo: str):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = None
        self.endereco = None
        self.contato = None
        self.alergias = []
        self.tipo_sanguineo = None