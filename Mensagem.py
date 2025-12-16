from datetime import date

class Mensagem:
    def __init__(self, id_mensagem: int, id_remetente: int, id_destinatario: int, 
                 tipo_remetente: str, assunto: str, conteudo: str, data_envio: date, lida: bool = False):
        self.id_mensagem = id_mensagem
        self.id_remetente = id_remetente
        self.id_destinatario = id_destinatario
        self.tipo_remetente = tipo_remetente
        self.assunto = assunto
        self.conteudo = conteudo
        self.data_envio = data_envio
        self.lida = lida