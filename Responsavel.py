import json
import os


dados_json = 'dados/dados.json'

class Validar_nome:
    @staticmethod
    def validar_nome( nome):
        if len(nome) > 0:
            return nome
        else:
            return None
        
class Validar_email:
    @staticmethod
    def validar_email(email):
        if '@' in email and '.' in email:
            return email
        else:
            return None
class Validar_senha:
    @staticmethod
    def validar_senha(senha):
        if len(senha) >= 6:
            return senha
        else:
            return None

class Responsavel:
    def __init__(self):
        self.dic_add_dados = {}
        self.lista_telefone = []

    def cad_rasponsavel(self, id, user, password, email):
        self.id = id
        nome_valido = Validar_nome.validar_nome(user)
        password_valido = Validar_senha.validar_senha(password)
        email_valido = Validar_email.validar_email(email)
        

        if nome_valido:
            if email_valido:
                if password_valido:
                    self.dic_add_dados['id'] = self.id
                    self.dic_add_dados['user'] = nome_valido
                    self.dic_add_dados['password'] = password_valido
                        
                    while True:
                        tel_valido = str(input("Telefone: "))
                        self.lista_telefone.append(tel_valido)
                        continuar = int(input("continuar? 1-sim 2-não: "))

                        if continuar != 1:
                            break
                    self.dic_add_dados['telefone'] = self.lista_telefone
                    self.dic_add_dados['email'] = email_valido
                    self.dic_add_dados['funcao'] = "responsavel"

                    self.lista_clone_dados = []
                    if os.path.exists(dados_json):
                        with open(dados_json, 'r', encoding='utf-8') as arquivo_jason:
                            try:
                                self.lista_clone_dados = json.load(arquivo_jason)
                                if not isinstance(self.lista_clone_dados, list):
                                    self.lista_clone_dados =[]
                            except json.JSONDecodeError:
                                self.lista_clone_dados = []
                    else:
                        self.lista_clone_dados = []
                    self.lista_clone_dados.append(self.dic_add_dados)
                    with open(dados_json, 'w', encoding='utf-8') as arquivo_json:
                        json.dump(self.lista_clone_dados, arquivo_json, indent=4, ensure_ascii=False)         
                    print(f"ADCIONADO: {nome_valido}")
                else:
                    print("ERRO: senha invalida!!")
            else:
                print("ERRO: email invalido!!")        
        else:
            print("ERRO: nome invalido!!")
# --- Bloco para carregar lista_id no escopo global (usando o novo caminho) ---
if os.path.exists(dados_json):
    with open(dados_json, 'r', encoding='utf-8') as arquivo_json:
        try:
            lista_id = json.load(arquivo_json)
            if not isinstance(lista_id, list):
                 lista_id = []
        except json.JSONDecodeError:
            lista_id = []

id = len(lista_id ) +1

def cad_responsavel():
    while True:
        global id
        nome = str(input("Nome: "))
        email = str(input("Email: "))
        password = str(input("Senha: "))

        responsavel = Responsavel()
        responsavel.cad_rasponsavel(id, nome, password, email)
        print("\n")
        opcao = int(input("continuar? 1-sim 2-não: "))
        if opcao != 1:
            break

        id += 1
