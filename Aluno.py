# Importação do módulo json
import json

# Importação do módulo os
import os

# Importação da classe datetime
from datetime import datetime

# Define o caminho do arquivo JSON
dados_json = 'dados/dados.json'

arquivo_turma_json = "dados/turma.json"

arquivo_aluno_json = "dados/aluno.json"


# Classe para validação do nome do aluno
class Validar_nome:


    @staticmethod
    def validar_nome(nome):
        if len(nome) > 0:
            return nome
        else:
            return None


# Classe para validação da matrícula do aluno
class Validar_matricula():


    @staticmethod
    def validar_matricula(matricula):
        if len(matricula) <= 0:
            return None

        # Verifica se o arquivo de alunos é existente
        if os.path.exists(arquivo_aluno_json):
            try:
                # Abre o arquivo JSON para leitura das matrículas cadastradas
                with open(arquivo_turma_json, 'r', encoding='utf-8') as arquivo_json:
                    lista_matricula = json.load(arquivo_json)

                    if not isinstance(lista_matricula, list):
                        lista_matricula = []
            except json.JSONDecodeError:
                lista_matricula = []

            for matriculas_registrados in lista_matricula:
                if matriculas_registrados.get('matricula') == matricula:
                    return None

        return matricula


# Classe Aluno
class Aluno:

    # Método construtor da classe Aluno
    def __init__(self):
        self.dic_add_dados = {}
        self.lista_responsavel = []

    # Método responsável pelo cadastro de um aluno no sistema
    def cad_aluno(self, matricula, nome, turma, dt_nascimento):

        valida_matricula = Validar_matricula.validar_matricula(matricula)
        valida_nome = Validar_nome.validar_nome(nome)

        turma_aluno = turma
        data_nascimento = dt_nascimento

        if valida_matricula:
            if valida_nome:

                self.dic_add_dados['matricula'] = valida_matricula
                self.dic_add_dados['nome'] = valida_nome

                funcao_lista_responsavel()

                # Permite o cadastro de um ou mais responsáveis
                while True:
                    cont = 1
                    escolha_reponsavel = str(input(f"{cont}º responsavel: "))
                    self.lista_responsavel.append(escolha_reponsavel)
                    continuar = int(input("Deseja continuar? 1-sim 2-não: "))
                    if continuar != 1:
                        break

                # Armazena os responsáveis dos alunos
                self.dic_add_dados['responsavel'] = self.lista_responsavel
                self.dic_add_dados['nascimento'] = data_nascimento
                self.dic_add_dados['turma'] = turma_aluno

                self.lista_clone_dados = []

                if os.path.exists(arquivo_aluno_json):
                    with open(arquivo_aluno_json, 'r', encoding='utf-8') as arquivo_json:
                        try:
                            self.lista_clone_dados = json.load(arquivo_json)
                            if not isinstance(self.lista_clone_dados, list):
                                self.lista_clone_dados = []
                        except json.JSONDecodeError:
                            self.lista_clone_dados = []
                else:
                    self.lista_clone_dados = []

                # Adiciona o novo aluno à lista
                self.lista_clone_dados.append(self.dic_add_dados)

                with open(arquivo_aluno_json, 'w', encoding='utf-8') as arquivo_json:
                    json.dump(self.lista_clone_dados, arquivo_json, indent=4, ensure_ascii=False)

                # Exibe mensagem de sucesso
                print(f"SUCESSO: aluno {valida_nome} cadastrada")

                self.lista_responsavel.clear()
            else:
                print("ERRO: nome Invalido")
        else:
            print("ERRO: matricula invalida")


# Lista global para armazenar os responsáveis
lista_responsavel = []


def funcao_lista_responsavel():
    global lista_responsavel
    lista_responsavel.clear()

    with open(dados_json, 'r', encoding='utf-8') as arquivo_json:
        lista = json.load(arquivo_json)

    for item in lista:
        if item.get('funcao') == 'responsavel':
            lista_responsavel.append(item)

    print("\n")
    print("LISTA DE RESPONSAVEIS")

    if not lista_responsavel:
        print("Nenhum responsável cadastrado.")
        return

    for item in lista_responsavel:
        print(f"Nome: {item['user']}")


lista_turma = []


# Função listar as turmas
def listar_turma():
    global lista_turma

    # Abre o arquivo JSON contendo os dados das turmas
    with open(arquivo_turma_json, 'r', encoding='utf-8') as arquivo_json:
        lista_dados_json = json.load(arquivo_json)

    # Atualiza a lista de turmas
    lista_turma.clear()
    lista_turma.extend(lista_dados_json)

    # Exibe as turmas disponíveis
    print("\n")
    print("LISTA DE TURMAS")

    for item in lista_turma:
        print(f"turmas -> {item['nome_turma']}")


# Função para ajustar e validar o formato da data de nascimento
def ajustar_mascarar_data_nascimento(data_str):
    data_str = data_str.strip()

    # Tenta converter a data no formato padrão DD/MM/AAAA
    try:
        data_objeto = datetime.strptime(data_str, "%d/%m/%Y")
        return data_objeto.strftime("%d/%m/%Y")
    except ValueError:
        pass

    # Remove caracteres não numéricos da data
    data_limpa = "".join(filter(str.isdigit, data_str))

    if len(data_limpa) == 8:
        formato_sem_mascara = "%d%m%Y"
        try:
            data_objeto = datetime.strptime(data_limpa, formato_sem_mascara)
            return data_objeto.strftime("%d/%m/%Y")
        except ValueError:
            return None

    return None


# Função para iniciar o processo de cadastro de alunos
def cad_aluno():
    # Estrutura de repetição
    while True:

        matricula = str(input("Matricula: "))
        nome = str(input("Nome: "))
        data = ajustar_mascarar_data_nascimento(input("Data de Nascimento: "))
        data_nascimento = data

        listar_turma()
        escolher_turma = str(input("Turma: "))

        turma = None

        # Verifica se a turma informada existe
        for item in lista_turma:
            if item['nome_turma'] == escolher_turma:
                turma = item['nome_turma']
                break

        if turma is None:
            print("ERRO: Turma selecionada não existe na lista.")
            continue

            # Cria um objeto da classe Aluno
        aluno = Aluno()
        aluno.cad_aluno(matricula, nome, turma, data_nascimento)

        print("\n")

        # Pergunta se deseja continuar o cadastro
        opcao = int(input("continuar? 1-sim 2-não: "))
        if opcao != 1:
            break

