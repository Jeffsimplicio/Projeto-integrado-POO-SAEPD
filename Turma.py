import json
import os

# Define os caminhos dos arquivos JSON para fácil referência.
dados_json = 'dados/dados.json'
arquivo_turma_json = "dados/turma.json"

# --- CLASSE DE VALIDAÇÃO DE NOME DA TURMA ---
class Validar_nome():
    # O decorador @staticmethod permite chamar o método sem instanciar a classe.
    @staticmethod
    def validar_nome(nome):
        # 1. Verifica se o nome fornecido não está vazio.
        if len(nome) <= 0:
            return None
        
        # 2. Verifica se o arquivo de turmas já existe no sistema.
        if os.path.exists(arquivo_turma_json):
            try:
                # Abre o arquivo JSON no modo de leitura ('r').
                with open(arquivo_turma_json, 'r', encoding='utf-8') as arquivo_json:
                    # Carrega a lista de turmas existentes.
                    lista_nome = json.load(arquivo_json)
                    # Garante que o objeto carregado seja uma lista; se não for, inicializa como lista vazia.
                    if not isinstance(lista_nome, list):
                        lista_nome = []
            except json.JSONDecodeError:
                # Trata o erro se o arquivo JSON estiver vazio ou mal formatado.
                lista_nome = []
            
            # 3. Verifica se o nome da nova turma já está registrado (duplicação).
            for nomes_registrados in lista_nome:
                # O método .get('nome') é mais seguro, evita KeyError.
                # Se o nome já existir, retorna None (indica falha na validação).
                if nomes_registrados.get('nome_turma') == nome: # Corrigido para 'nome_turma'
                    return None
        
        # Se o nome for válido (não vazio e não duplicado), retorna o próprio nome.
        return nome

# --- CLASSE DE VALIDAÇÃO DE TURNO ---
class Validar_turno():
    @staticmethod
    def validar_turno(turno):
        # Verifica se a string do turno não está vazia.
        if len(turno) > 0:
            return turno
        else:
            # Se estiver vazia, retorna None.
            return None

# --- CLASSE PRINCIPAL PARA GERENCIAR A TURMA ---
class Turma:
    def __init__(self):
        # Dicionário que armazena temporariamente os dados da turma a ser cadastrada.
        self.dic_dados_turma = {}

    # Método para cadastrar a turma, recebendo todos os dados.
    def cad_turma(self, id=int, nome=str, turno=str, professor_auxiliar= int):
        self.id = id
        
        # Chama os métodos estáticos para validação dos dados.
        valida_nome = Validar_nome.validar_nome(nome)
        valida_turno = Validar_turno.validar_turno(turno)
        
        self.professor_auxiliar = professor_auxiliar

        # Início da lógica de cadastro: verifica se o nome foi validado.
        if valida_nome:
            # Se o nome for válido, verifica se o turno foi validado.
            if valida_turno:
                # 1. Preenche o dicionário com os dados validados.
                self.dic_dados_turma['id'] = self.id
                self.dic_dados_turma['nome_turma'] = valida_nome # Chave usada no arquivo JSON
                self.dic_dados_turma['turno'] = valida_turno
                self.dic_dados_turma['professor'] = self.professor_auxiliar
                
                # 2. Prepara-se para carregar os dados existentes do arquivo.
                self.lista_clone_dados = []
                
                # Se o arquivo de turmas existe, carrega o conteúdo.
                if os.path.exists(arquivo_turma_json):
                    with open(arquivo_turma_json,'r', encoding='utf-8') as arquivo_json:
                        try:
                            self.lista_clone_dados = json.load(arquivo_json)
                            # Garante que seja uma lista antes de adicionar o novo item.
                            if not isinstance(self.lista_clone_dados, list):
                                self.lista_clone_dados = []
                        except json.JSONDecodeError:
                            # Se o JSON estiver inválido/vazio, inicializa a lista.
                            self.lista_clone_dados = []
                else:
                    # Se o arquivo não existir, começa com uma lista vazia.
                    self.lista_clone_dados = []
                    
                # 3. Adiciona o dicionário da nova turma à lista.
                self.lista_clone_dados.append(self.dic_dados_turma)
                
                # 4. Sobrescreve o arquivo JSON com a lista completa (antigos + novo).
                with open(arquivo_turma_json, 'w', encoding='utf-8') as arquivo_json:
                    # Salva os dados, formatando com identação (indent=4) e UTF-8.
                    json.dump(self.lista_clone_dados, arquivo_json, indent=4, ensure_ascii=False)
                
                print(f"SUCESSO: turma {valida_nome} cadastrada")
            else:
                print("ERRO: sem turno definido")
        else:
            print("ERRO: nome já existente ou inválido")

# Lista global que armazenará os objetos de professores.
professores = [] 

# --- FUNÇÃO PARA LISTAR PROFESSORES ---
def lista_professor():
    # Abre o arquivo de dados (usuários) para encontrar os professores.
    with open(dados_json, 'r', encoding='utf-8') as arquivo_json:
        lista = json.load(arquivo_json)
        
        # Itera sobre a lista de usuários e filtra quem tem a função 'professor'.
        for i in range(len(lista)):
            if lista[i].get('funcao') == 'professor':
                professores.append(lista[i]) # Adiciona o dicionário completo do professor.
                
    print("\n")
    print("LISTA DE PROFESSORES")
    
    # Imprime os nomes de usuário dos professores.
    for i in range(len(professores)):
        print(professores[i]['user'])

# --- GERAÇÃO AUTOMÁTICA DE ID ---
# Tenta carregar as turmas existentes para determinar o próximo ID.
lista_id = []
if os.path.exists(arquivo_turma_json):
    with open(arquivo_turma_json, 'r', encoding='utf-8') as arquivo_json:
        try:
            lista_id = json.load(arquivo_json)
            if not isinstance(lista_id, list):
                lista_id = []
        except json.JSONDecodeError:
            lista_id = []

# Define o próximo ID sequencial: (número de turmas existentes) + 1.
id = len(lista_id ) +1

# --- FUNÇÃO PRINCIPAL DE INTERAÇÃO COM O USUÁRIO ---
def cad_turma():
    global id # Permite que a função modifique o ID global se necessário.
    
    # 1. Coleta os dados de entrada.
    nome = str(input("Nome: "))
    turno = str(input("Turno: "))
    
    # 2. Exibe a lista de professores disponíveis.
    lista_professor()
    
    escolher_professor = str(input("Professor: "))
    professor_auxiliar = None
    
    # 3. Busca o nome do professor escolhido para passar para o cadastro.
    for i in range(len(professores)):
        if professores[i]['user'] == escolher_professor:
            professor_auxiliar = professores[i]['user'] # Armazena o nome de usuário do professor.
            break # Encontrou, pode parar o loop
            
    # 4. Instancia a classe Turma e executa o cadastro.
    turma = Turma()
    turma.cad_turma(id, nome, turno, professor_auxiliar)

# Comentário final: Para rodar o sistema, a função `cad_turma()` deve ser chamada.
# Exemplo: cad_turma()