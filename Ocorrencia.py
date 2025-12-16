from datetime import date

class Ocorrencia:
    def __init__(self, id_ocorrencia: int, id_aluno: int, id_professor: int, 
                 tipo: str, descricao: str, data: date):
        self.id_ocorrencia = id_ocorrencia
        self.id_aluno = id_aluno
        self.id_professor = id_professor
        self.tipo = tipo
        self.descricao = descricao
        self.data = data