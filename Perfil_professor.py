import json # Importa o módulo json
from Frequencia import iniciar_frequencia # Importa a função 
from lancarNota import registrar_nota # Importa a função responsável pelo registro de notas dos alunos
from Mensagem import iniciar_conversar

arquivo_turma_json = "dados/turma.json" # Define o caminho do arquivo JSON que armazena os dados das turmas

arquivo_aluno_json = "dados/aluno.json"

# Lista global utilizada para armazenar os alunos
lista_filtro_aluno = []


# Função que filtra os alunos pertencentes a uma turma específica
def filtrar_aluno(turma):
    global lista_filtro_aluno
    # Limpa a lista antes de adicionar novos dados
    lista_filtro_aluno.clear()

    # Abre o arquivo JSON contendo os dados dos alunos
    with open(arquivo_aluno_json, 'r', encoding='utf-8') as arquivo_json:
        lista = json.load(arquivo_json)

    # Percorre a lista de alunos e seleciona apenas os que pertencem à turma informada
    for item in lista:
        if item.get('turma') == turma:
            lista_filtro_aluno.append(item)

    print("\n")
    print(f"ALUNOS DA TURMA: {turma}")
    for item in lista_filtro_aluno:
        print(f"matricula = {item['matricula']} --- {item['nome']}")


lista_turma = []
# Função responsável por listar todas as turmas cadastradas no sistema
def listar_turma():
    global lista_turma

    # Abre o arquivo JSON contendo os dados das turmas
    with open(arquivo_turma_json, 'r', encoding='utf-8') as arquivo_json:
        lista_dados_json = json.load(arquivo_json)

    # Atualiza a lista de turmas com os dados do arquivo
    lista_turma.clear()
    lista_turma.extend(lista_dados_json)

    # Exibe as turmas disponíveis
    print("\n")
    print("Lista das turmas:")

    for item in lista_turma:
        print(f"turmas -> {item['nome_turma']}")


# Função principal que inicializa o perfil do professor no sistema
def iniciar_perfil_professor(nome_usuario):
    # Exibe o nome do professor autenticado no sistema
    print(nome_usuario)

    # Estrutura de repetição que mantém o menu ativo até o usuário optar por sair
    while True:

        # Lista as turmas disponíveis
        listar_turma()

        # Solicita ao professor a escolha de uma turma
        turma = str(input("Escolha uma turma: "))

        # Filtra e exibe os alunos da turma selecionada
        filtrar_aluno(turma)
        escolha_aluno = str(input("qual aluno: "))

        # Exibe o menu de opções disponíveis ao professor
        opcao = int(input("""
Selecione a opção desejada:
1 → Registrar presença dos alunos
2 → Lançar notas
3 → Enviar mensagem
4 → Consultar justificativas
5 → Encerrar sessão
    """))

        if opcao == 1:
            print("\n")
            iniciar_frequencia(turma, lista_filtro_aluno)

        if opcao == 2:
            print("\n")
            registrar_nota(nome_usuario, turma, lista_filtro_aluno)
        if opcao == 3:
            print("\n")
            
            iniciar_conversar(escolha_aluno, nome_usuario)
        if opcao == 5:

            break
