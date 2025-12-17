import json
import os
from datetime import datetime

dados_json = 'dados/dados.json'
historico_mensagens = 'dados/mensagem.json'

class Mensagem:
    def __init__(self,nome_aluno, nome_remetente, nome_destinatario, mensagem):
        self.nome_aluno = nome_aluno
        self.nome_remetente = nome_remetente
        self.nome_destinatario = nome_destinatario
        self.mensagem = mensagem
        self.dict_frequencia = {} 

    def registrar_chate(self):
        # Obtém a data e hora atual e formata como DD/MM/AAAA HH:MM.
        data_formatada = datetime.now().strftime('%d/%m/%Y %H:%M')

        lista_historico_mensagem = []
        conversa_encontrada = False

        # --- 1. CARREGAR DADOS EXISTENTES ---
        if os.path.exists(historico_mensagens):
            try:
                # Tenta abrir o arquivo JSON no modo de leitura.
                with open(historico_mensagens, 'r', encoding='utf-8') as arquivo_json:
                    lista_historico_mensagem = json.load(arquivo_json)
                    # Garante que o objeto carregado seja uma lista; caso contrário, inicializa como lista vazia.
                    if not isinstance(lista_historico_mensagem, list):
                        lista_historico_mensagem = []
            except json.JSONDecodeError:
                # Se o JSON estiver corrompido ou vazio, inicializa a lista.
                lista_historico_mensagem = []
        novo_hitorico = {
            'remetente': self.nome_remetente,
            'destinatario': self.nome_destinatario,
            'mensagem': self.mensagem,
            'data': data_formatada
        }
        for registrar in lista_historico_mensagem:
            if registrar.get('nome_aluno') == self.nome_aluno:
                if 'conversar' not in registrar:
                    registrar['conversar'] = []

                registrar['conversar'].append(novo_hitorico)
                conversa_encontrada =True
                print(f"mensagem enviada para {self.nome_destinatario}")
                break
        
        if not conversa_encontrada:
            nova_conversa = {
                'nome_aluno': self.nome_aluno,
                'conversar': [novo_hitorico]
            }
            lista_historico_mensagem.append(nova_conversa)
            print('INICIANDO UMA NOVA CONVERSA')
        
        with open(historico_mensagens, 'w', encoding='utf-8') as arquivo_json:
            json.dump(lista_historico_mensagem, arquivo_json, indent=4, ensure_ascii=False)
        return True
    

class GerenciadorMensagens:
    def __init__(self, dados_carregados):
        
        self.dados = dados_carregados

    def buscar_por_pessoa(self, nome_remetente):
        
        resultados = []
        nome_busca = nome_remetente.strip() 

        for registro in self.dados:
            if not isinstance(registro, dict): 
                continue
            nome_aluno = registro.get("nome_aluno")
            conversas = registro.get("conversar", [])

            for msg in conversas:
                if not isinstance(msg, dict): 
                    continue
                remetente = msg.get("remetente", "")
                destinatario = msg.get("destinatario", "")

                if nome_busca == remetente or nome_busca == destinatario:
                    msg_encontrada = dict(msg)
                    msg_encontrada["aluno_contexto"] = nome_aluno
                    resultados.append(msg_encontrada)
        
        return resultados

def ver_funcao(nome_remetente):
    funcao = None
    with open(dados_json, 'r', encoding='utf-8') as arquivo_json:
        lista = json.load(arquivo_json)
    for item in lista:
        if nome_remetente == item.get('user'):
            funcao = item['funcao']
            break
    return funcao


lista_professor = []
def filtra_professores():
    global lista_professor
    lista_professor.clear
    with open(dados_json, 'r', encoding='utf-8') as arquivo_json:
        lista = json.load(arquivo_json)
    for item in lista:
        if item['funcao'] == 'professor':
            lista_professor.append(item)
    print("\n")
    print("---PROFESSORES---")
    for item in lista_professor:
        print(f"NOME -> {item['user']} -- DICIPLINA -> {item['diciplina'],[]}")

lista_responsavel = []
def filtra_responsavel():
    global lista_responsavel
    lista_responsavel.clear()
    with open(dados_json, 'r', encoding='utf-8') as arquivo_json:
        lista = json.load(arquivo_json)
    for item in lista:
        if item['funcao'] == 'responsavel':
            lista_responsavel.append(item)
    print("\n")
    print("---PROFESSORES---")
    for item in lista_responsavel:
        print(f"RESPONSAVEL -> {item['user']}")

def iniciar_conversar(escolha_aluno, nome_remetente):

    dados_carregados = []
    if os.path.exists(historico_mensagens):
        try:
            with open(historico_mensagens, 'r', encoding='utf-8') as f:
                dados_carregados = json.load(f)
        except json.JSONDecodeError:
            dados_carregados = []
    gerenciador = GerenciadorMensagens(dados_carregados)

    pessoa = gerenciador.buscar_por_pessoa(nome_remetente)
    for item in pessoa:
        print(f"Msg: {item['mensagem']} | De: {item['remetente']} Para: {item['destinatario']} -> data/hora: {item['data']}")
    
    print("\n")
    print(f"Pode mandar mensagem {nome_remetente}")
    funcao = ver_funcao(nome_remetente)
    
    
    if funcao == 'professor':
        while True:

            filtra_responsavel()
            destinatario = str(input("Com quem deseja conversar? "))
            mensagem = str(input("DIGITE A MENSAGEM -> "))
            chat = Mensagem(escolha_aluno, nome_remetente, destinatario, mensagem)
            chat.registrar_chate()
            continuar = int(input("continuar? 1-sim 2-não: "))
            if continuar != 1:
                break


    if funcao == 'responsavel':
        while True:
            filtra_professores()
            destinatario = str(input("Com quem deseja conversar? "))
            mensagem = str(input("DIGITE A MENSAGEM -> "))
            chat = Mensagem(escolha_aluno, nome_remetente, destinatario, mensagem)
            chat.registrar_chate()
            continuar = int(input("continuar? 1-sim 2-não: "))
            if continuar != 1:
                break
