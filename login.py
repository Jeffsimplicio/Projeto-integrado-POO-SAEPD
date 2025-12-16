import json  # Importa a biblioteca padrão JSON, utilizada para manipulação de dados estruturados em formato texto.

from Administrador import iniciar_cadastro  # Importa a função iniciar_cadastro do módulo Administrador, responsável por inicializar processos específicos do perfil administrativo.
from Perfil_professor import iniciar_perfil_professor  # Importa a função iniciar_perfil_professor do módulo Perfil_professor, destinada a iniciar funcionalidades específicas do perfil docente.

arquivo_dados = 'dados/dados.json'  # Define o caminho do arquivo JSON que contém os dados de usuários e suas credenciais.
nome_usuario = 0  # Inicializa a variável nome_usuario com valor numérico, embora semanticamente deveria ser uma string (ponto de atenção).

class Login:  # Declaração da classe Login, que encapsula a lógica de autenticação de usuários.
    def __init__(self, user, password):  # Método construtor da classe, responsável por inicializar os atributos user e password.
        self.user = user  # Atribui o nome de usuário fornecido ao atributo da instância.
        self.password = password  # Atribui a senha fornecida ao atributo da instância.

    def validacão_user(self):  # Método responsável por validar as credenciais do usuário.
        
        with open(arquivo_dados, 'r', encoding='utf-8') as dados:  # Abre o arquivo JSON em modo leitura, garantindo suporte a caracteres especiais com UTF-8.
            lista_dados = json.load(dados)  # Carrega os dados do arquivo em uma estrutura Python (lista/dicionário).
            for i in range(len(lista_dados)):  # Itera sobre a lista de usuários armazenados.
                if lista_dados[i]['user'] == self.user:  # Verifica se o usuário fornecido corresponde ao existente no arquivo.
                    if lista_dados[i]['password'] == self.password:  # Confere se a senha fornecida corresponde à registrada.
                        if lista_dados[i]['funcao'] == 'admin':  # Caso a função seja "admin", direciona para o fluxo administrativo.
                            print("login feituado com sucesso")  # Mensagem de confirmação de login.
                            nome_usuario = lista_dados[i]['user']  # Armazena o nome do usuário autenticado (atenção: variável local, não global).
                            iniciar_cadastro(nome_usuario)  # Chama a função iniciar_cadastro para habilitar funcionalidades administrativas.
                            return  # Encerra o método após autenticação bem-sucedida.
                        if lista_dados[i]['funcao'] == 'professor':  # Caso a função seja "professor", direciona para o fluxo docente.
                            print("login feituado com sucesso")  # Mensagem de confirmação de login.
                            nome_usuario = lista_dados[i]['user']  # Armazena o nome do usuário autenticado.
                            iniciar_perfil_professor(nome_usuario)  # Chama a função iniciar_perfil_professor para habilitar funcionalidades docentes.
                            return  # Encerra o método após autenticação bem-sucedida.
            
            print("usuario nao encontrado")  # Caso nenhum usuário corresponda às credenciais fornecidas, informa falha na autenticação.
            return None  # Retorna None explicitamente, indicando ausência de validação.

if __name__ == "__main__":  # Estrutura condicional que garante a execução apenas quando o arquivo é executado diretamente, não quando importado como módulo.
    print("-"*10, "bem vindo ao SAEPD", "-"*10)  # Exibe mensagem de boas-vindas ao sistema SAEPD.

    user = str(input("usuario: "))  # Solicita ao usuário a entrada de seu nome de usuário, convertendo para string.
    password = str(input("senha: "))  # Solicita ao usuário a entrada de sua senha, convertendo para string.
    login = Login(user, password)  # Instancia a classe Login com os dados fornecidos.
    login.validacão_user()  # Executa o método de validação para autenticar o usuário.
