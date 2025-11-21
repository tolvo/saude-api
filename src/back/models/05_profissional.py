class Profissional:
    def __init__(self, nome: str, cpf: str, tipo: str, registro_orgaoclass: str, numero_registro: str, especialidade: str = ""):
        self.nome = nome
        self.cpf = cpf
        self.tipo = tipo  # "Médico" ou "Enfermeiro"
        self.registro_orgaoclass = registro_orgaoclass  # "CRM"
        self.numero_registro = numero_registro
        self.especialidade = especialidade  # Apenas para médicos
        self.unidades_saude = []  # Lista de unidades de saúde onde o profissional atua
    