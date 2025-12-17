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
        

class ConsultaNotas:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.dados = self._carregar_dados()

    def _carregar_dados(self):
        """Lê o arquivo JSON com as notas."""
        if os.path.exists(self.caminho_arquivo):
            try:
                with open(self.caminho_arquivo, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("Erro ao ler o arquivo de notas.")
                return []
        return []

    def buscar_notas_por_aluno(self, escolha_aluno):
        """Busca e exibe as notas de um aluno específico."""
        aluno_encontrado = False
        escolha_aluno = escolha_aluno.strip().lower()

        for registro in self.dados:
            # Acessa o nome dentro do dicionário nome_aluno
            dados_aluno = registro.get("nome_aluno", {})
            nome_aluno = dados_aluno.get("nome", "").lower()

            if nome_aluno == escolha_aluno:
                aluno_encontrado = True
                notas_1bim = registro.get("1bim", {})
                
                print("-" * 30)
                print(f"ALUNO: {dados_aluno.get('nome').upper()}")
                print(f"TURMA: {dados_aluno.get('turma')}")
                print(f"PROFESSOR: {registro.get('professor')}")
                print("-" * 30)
                print(f"Nota Prova: {notas_1bim.get('nota_prova')}")
                print(f"Nota Trabalho: {notas_1bim.get('nota_trab')}")
                print(f"Nota Final: {notas_1bim.get('nota_final')}")
                print(f"Observação: {notas_1bim.get('observacao')}")
                print("-" * 30)

        if not aluno_encontrado:
            print(f"Aluno '{escolha_aluno}' não encontrado.")
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
        
        if opcao == 1:
            consulta_notas = ConsultaNotas('dados/notas.json')
            consulta_notas.buscar_notas_por_aluno(escolha_aluno)

        if opcao == 2:
            iniciar_conversar(escolha_aluno, nome_usuario)
        
        if opcao == 4:

            break


    
