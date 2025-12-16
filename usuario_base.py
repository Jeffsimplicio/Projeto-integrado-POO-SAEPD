# Importa módulos necessários para criar uma Classe Abstrata (ABC)
from abc import ABC, abstractmethod

class Usuario(ABC):
    """
    Classe Abstrata base para todos os perfis de usuário do sistema SAEPD.
    Define o contrato mínimo (atributos e métodos obrigatórios).
    """
    def __init__(self, id_usuario, nome, email, senha):
        self._id_usuario = id_usuario
        self._nome = nome
        self._email = email
        self._senha = senha 

    @abstractmethod
    def validar_acesso(self):
        """Método abstrato que força a implementação nas classes filhas."""
        pass

    @abstractmethod
    def exibir_painel(self):
        """Método abstrato para exibir o painel específico do perfil."""
        pass

    def obter_email(self):
        return self._email
