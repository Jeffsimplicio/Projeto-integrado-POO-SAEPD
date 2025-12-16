import json
from Administrador import iniciar_cadastro
from Perfil_professor import iniciar_perfil_professor

arquivo_dados = 'dados/dados.json'
nome_usuario = 0
class Login:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def validacão_user(self):
        
        with open(arquivo_dados, 'r', encoding='utf-8') as dados:
            lista_dados= json.load(dados)
            for i in range(len(lista_dados)):
                if lista_dados[i]['user'] == self.user:
                    if lista_dados[i]['password'] == self.password:
                        if lista_dados[i]['funcao'] == 'admin':
                            print("login feituado com sucesso")
                            nome_usuario = lista_dados[i]['user']
                            iniciar_cadastro(nome_usuario)
                            return
                        if lista_dados[i]['funcao'] == 'professor':
                            print("login feituado com sucesso")
                            nome_usuario = lista_dados[i]['user']
                            iniciar_perfil_professor(nome_usuario)
                            return
                            
                              
            
            print("usuario nao encontrado")
            return None
                    

if __name__ == "__main__":
    print("-"*10,"bem vindo ao SAEPD","-"*10)

    user = str(input("usuario: "))
    password = str(input("senha: "))
    login = Login(user, password)
    login.validacão_user()
