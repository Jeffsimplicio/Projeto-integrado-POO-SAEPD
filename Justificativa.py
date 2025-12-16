from datetime import date

class Justificativa:
    def __init__(self, id_justificativa: int, id_responsavel: int, id_aluno: int, 
                 tipo: str, descricao: str, data: date, anexo: str):
        self.id_justificativa = id_justificativa
        self.id_responsavel = id_responsavel
        self.id_aluno = id_aluno
        self.tipo = tipo
        self.descricao = descricao
        self.data = data
        self.anexo = anexo