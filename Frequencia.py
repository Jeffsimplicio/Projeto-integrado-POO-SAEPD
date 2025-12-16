import json
import os
from datetime import datetime # Importa a classe datetime para manipular datas e horas.


arquivo_frequencia_json = "dados/frequencia.json" # Define o caminho do arquivo onde o histórico de frequência será salvo.

# --- CLASSE DE GESTÃO DE FREQUÊNCIA ---
class Frequencia:
    def __init__(self):
        self.dict_frequencia = {} # Dicionário inicial (não usado ativamente no método principal).

    # Método principal para registrar a presença ou falta de um aluno.
    def registrar_frequencia(self, matricula, status_frequencia):
        
        # Obtém a data e hora atual e formata como DD/MM/AAAA HH:MM.
        data_formatada = datetime.now().strftime('%d/%m/%Y %H:%M')
        
        self.matricula = matricula
        self.data = data_formatada
        
        lista_dados_frequencia = []
        aluno_encontrado = False # Flag para saber se a matrícula já existe no arquivo JSON.

        
        # --- 1. CARREGAR DADOS EXISTENTES ---
        if os.path.exists(arquivo_frequencia_json):
            try:
                # Tenta abrir o arquivo JSON no modo de leitura.
                with open(arquivo_frequencia_json, 'r', encoding='utf-8') as arquivo_json:
                    lista_dados_frequencia = json.load(arquivo_json)
                    # Garante que o objeto carregado seja uma lista; caso contrário, inicializa como lista vazia.
                    if not isinstance(lista_dados_frequencia, list):
                        lista_dados_frequencia = []
            except json.JSONDecodeError:
                # Se o JSON estiver corrompido ou vazio, inicializa a lista.
                lista_dados_frequencia = []
        
        # --- 2. PREPARA O REGISTRO DE CHAMADA ATUAL ---
        nova_chamada = {
            "data": self.data,
            "status": status_frequencia # Pode ser "Presente" ou "Faltou"
        }

        # --- 3. PROCURA E ATUALIZA REGISTRO EXISTENTE ---
        for registro in lista_dados_frequencia:
            # Verifica se a matrícula do registro atual corresponde à matrícula que está sendo processada.
            if registro.get('matricula') == self.matricula:
                
                # Se a chave "historico" não existir (primeira vez ou problema de estrutura), cria como lista vazia.
                if "historico" not in registro:
                    registro["historico"] = []
                
                # Adiciona o novo registro de frequência ao histórico daquele aluno.
                registro["historico"].append(nova_chamada)
                
                aluno_encontrado = True # Marca que o aluno foi encontrado e atualizado.
                print(f"SUCESSO: Nova presença adicionada ao histórico de {self.matricula}.")
                break # Sai do loop, pois o aluno já foi processado.
        
        # --- 4. CRIA NOVO REGISTRO (Se a matrícula não foi encontrada) ---
        if not aluno_encontrado:
            
            # Estrutura do novo registro para um aluno que está sendo registrado pela primeira vez.
            novo_registro = {
                'matricula': self.matricula,
                # O histórico é inicializado com apenas a chamada atual.
                'historico': [ nova_chamada ]
            }
            lista_dados_frequencia.append(novo_registro) # Adiciona o novo registro à lista principal.
            print(f"SUCESSO: Primeiro registro criado para a matrícula {self.matricula}.")
        
        # --- 5. SALVAR DADOS ATUALIZADOS ---
        # Abre o arquivo no modo de escrita ('w'), sobrescrevendo o conteúdo com a lista completa e atualizada.
        with open(arquivo_frequencia_json, 'w', encoding='utf-8') as arquivo_json:
            # Salva os dados no formato JSON, usando indentação para legibilidade e UTF-8.
            json.dump(lista_dados_frequencia, arquivo_json, indent=4, ensure_ascii=False)
            
        return True # Retorna sucesso na operação.


# --- FUNÇÃO DE INTERFACE PARA INICIAR A CHAMADA ---
def iniciar_frequencia(turma_recebida, lista_alunos_recebida):

    print(f"\n --- INICIANDO CHAMADA DA TURMA: {turma_recebida} ---")
    
    aplicar_freq = Frequencia() # Cria uma instância da classe Frequencia.
    
    # Itera sobre a lista de dicionários de alunos (recebida de outra parte do sistema).
    for aluno in lista_alunos_recebida:
        print(f"Aluno: {aluno['nome']} (Matrícula: {aluno['matricula']})")
        
        # Solicita a entrada do status de presença.
        presenca = input("Digite 'P' para Presença ou 'F' para Falta: ").upper()
        print("\n")
        
        # Define o status completo baseado na entrada ('P' = Presente, Outro = Faltou).
        status = "Presente" if presenca == 'P' else "Faltou"
            
        # Chama o método da classe Frequencia para persistir o registro.
        aplicar_freq.registrar_frequencia(aluno['matricula'], status)
        
    print("Chamada finalizada!")