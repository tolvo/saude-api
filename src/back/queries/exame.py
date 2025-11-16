class Exame:
    def __init__(self, consulta_id: str, tipo_exame: str, data_realizacao: str, local_realizacao: str, resultado_link: str):
        self.consulta_id = consulta_id
        self.tipo_exame = tipo_exame  # Ex: "Laboratorial", "Imagem", etc.
        self.data_realizacao = data_realizacao  
        self.local_realizacao = local_realizacao
        self.resultado_link = resultado_link