import json
import os
from Mensagem import iniciar_conversar

arquivo_aluno_json = "dados/aluno.json"

lista_filtro_aluno = []
        
def buscar_alunos_por_responsavel( nome_responsavel_busca):
    global lista_filtro_aluno
    # Limpa a lista antes de adicionar novos dados
    lista_filtro_aluno.clear()

    # Abre o arquivo JSON contendo os dados dos alunos
    with open(arquivo_aluno_json, 'r', encoding='utf-8') as arquivo_json:
        lista = json.load(arquivo_json)

    # Percorre a lista de alunos e seleciona apenas os que tem o responsavel informado
    for item in lista:
        if nome_responsavel_busca in item.get('responsavel',[]):
            lista_filtro_aluno.append(item)

    print("\n")
    print(f"Alunos sob responsabilidade: {nome_responsavel_busca}")
    for item in lista_filtro_aluno:
        print(f"matricula = {item['matricula']} --- {item['nome']}")
        




# --- Bloco de Execução Principal ---

def iniciar_perfil_responsavel(nome_usuario):

    while True:
        buscar_alunos_por_responsavel(nome_usuario)
        print("\n")
        escolha_aluno = str(input("qual aluno: "))
        print("\n")
        opcao = int(input("""
Selecione a opção desejada:
1 → Ver notas
2 → Enviar mensagem
3 → Enviar justificativas
4 → Encerrar sessão
    """))
        if opcao ==2:
            iniciar_conversar(escolha_aluno, nome_usuario)
        
        if opcao == 4:

            break


    
