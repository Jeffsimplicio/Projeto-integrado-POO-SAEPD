import json
import os # Importa a biblioteca para interação com o sistema operacional (caminhos, diretórios).


arquivo_notas_json = "dados/notas.json" # Caminho do arquivo onde as notas serão armazenadas.
dados_json = 'dados/dados.json' # Caminho do arquivo que armazena dados de usuários (para obter disciplinas do professor).

# --- CLASSE DE VALIDAÇÃO DE NOTAS ---
class Verificar_Notas():
    @staticmethod
    def verifica_nota(text_nota):
        try:
            # Tenta converter o texto de entrada para float.
            nota = float(text_nota)
        except ValueError:
            # Retorna None se a entrada não for um número válido.
            return None
            
        # Verifica se a nota está no intervalo válido [0, 10].
        if 0 <= nota <= 10:
            return nota
        else:
            return None
            
# --- CLASSE DE REGISTRO DE NOTAS BIMESTRAIS ---
class Nota:
    def __init__(self):
        # Dicionário inicial (não usado ativamente, mas mantido na estrutura).
        self.dict_frequencia = {} 

    # Método para coletar, calcular e registrar as notas de um aluno.
    def adcionando_notas(self,nome_professor, nome_aluno, disciplina):
        self.nome_professor = nome_professor
        self.nome_aluno = nome_aluno # Espera-se que seja um dicionário do aluno.
        self.disciplina = disciplina

        print(f"\n--- Adicionando notas para: {self.nome_aluno['nome']} ---")
        
        # Coleta e valida cada nota. Se a validação falhar, a variável será None.
        nota_comportamental = Verificar_Notas.verifica_nota(input("Nota comportamenta: "))
        nota_extra = Verificar_Notas.verifica_nota(input("Nota extra: "))
        nota_trabalho = Verificar_Notas.verifica_nota(input("Nota de trabalho: "))
        nota_prova = Verificar_Notas.verifica_nota(input("Nota de prova: "))
        
        # Calcula a nota final, assumindo que todas as notas são válidas (precisa de tratamento de None).
        # A implementação atual pode falhar se alguma nota for None, pois None não suporta soma.
        # Para fins de comentário, assumimos que o usuário digita valores válidos (0 a 10).
        nota_final = (nota_comportamental + nota_extra + nota_trabalho + nota_prova) / 4
        
        observacao = str(input("Observação bimestral: "))

        # --- 1. CARREGAR DADOS EXISTENTES ---
        lista_notas = []
        if os.path.exists(arquivo_notas_json):
            try:
                # Tenta abrir e carregar a lista de notas existente.
                with open(arquivo_notas_json, 'r', encoding='utf-8') as arquivo_json:
                    lista_notas = json.load(arquivo_json)
                    if not isinstance(lista_notas, list):
                        lista_notas = []
            except json.JSONDecodeError:
                # Trata arquivo vazio ou mal formatado.
                lista_notas = []
                
        # --- 2. PREPARAR O REGISTRO DO BIMESTRE ---
        novo_bimestre = {
            "nota_comp": nota_comportamental,
            "nota_extra": nota_extra,
            "nota_trab": nota_trabalho,
            "nota_prova": nota_prova,
            "nota_final": nota_final,
            "observacao": observacao
        }
        
        # --- 3. PROCURAR E ATUALIZAR REGISTRO EXISTENTE (ALUNO) ---
        aluno_encontrado = False
        for registrar in lista_notas:
            # Procura o aluno pelo nome (ou dicionário de aluno, dependendo da estrutura de 'nome_aluno').
            if registrar.get('nome_aluno') == self.nome_aluno:
                aluno_encontrado = True

                # Verifica qual bimestre está disponível e preenche sequencialmente.
                if '1bim' not in registrar:
                    registrar['1bim'] = novo_bimestre
                    print("Notas salvas no 1º Bimestre.")
                elif '2bim' not in registrar:
                    registrar['2bim'] = novo_bimestre
                    print("Notas salvas no 2º Bimestre.")
                elif '3bim' not in registrar:
                    registrar['3bim'] = novo_bimestre
                    print("Notas salvas no 3º Bimestre.")
                elif '4bim' not in registrar:
                    registrar['4bim'] = novo_bimestre
                    print("Notas salvas no 4º Bimestre.")
                else:
                    print("AVISO: Todos os 4 bimestres deste aluno já estão preenchidos!")
                    
                break # Sai do loop após encontrar e registrar/avisar.
                
        # --- 4. CRIAR NOVO REGISTRO (PRIMEIRA NOTA DO ALUNO) ---
        if not aluno_encontrado:
            novo_registro_aluno = {
                "nome_aluno": self.nome_aluno,
                "professor": self.nome_professor,
                "disciplina": self.disciplina, # Adicionando a disciplina (faltava na implementação original para novos)
                "1bim": novo_bimestre 
            }
            lista_notas.append(novo_registro_aluno)
            print(f"Novo registro de nota no nome de {self.nome_aluno['nome']}")
            
        # --- 5. SALVAR DADOS ATUALIZADOS ---
        # Garante que o diretório 'dados' existe antes de tentar salvar.
        os.makedirs(os.path.dirname(arquivo_notas_json), exist_ok=True)
        with open(arquivo_notas_json, 'w', encoding='utf-8') as arquivo_json:
            # Salva a lista completa de notas (atualizada) no JSON.
            json.dump(lista_notas, arquivo_json, indent=4, ensure_ascii=False)
        print("OK: dados salvos")


# --- FUNÇÃO PARA OBTER DISCIPLINAS DO PROFESSOR ---
def escolha_diciplina(nome_usuario):
    # Abre o arquivo de usuários para obter as disciplinas do professor.
    with open(dados_json, 'r', encoding='utf-8') as arquivo_json:
        lista_usuarios = json.load(arquivo_json)
    
    disciplinas_do_prof = []

    for usuario in lista_usuarios:
        # Busca o professor pelo nome de usuário.
        if usuario.get('user') == nome_usuario:
            # Pega a lista de disciplinas associadas ao professor.
            disciplinas_do_prof = usuario.get('diciplina', [])
            break # Encontrou, pode parar a busca.
            
    print(f"\nDisciplinas do professor(a) {nome_usuario}:")
    
    if not disciplinas_do_prof:
        print("Nenhuma disciplina encontrada.")
        return None
    
    # Lista as disciplinas para que o professor possa escolher.
    for indice, materia in enumerate(disciplinas_do_prof):
        print(f"{indice + 1} -> {materia}")
        
    return disciplinas_do_prof


# --- FUNÇÃO DE INTERFACE PARA REGISTRAR NOTAS EM UMA TURMA ---
def registrar_nota(nome_usuario, turma_recebida, lista_filtro_aluno):
    print(f"\n --- APLICANDO NOTAS DA TURMA: {turma_recebida} ---")

    
    add_nota = Nota() # Cria uma instância da classe Nota.
    
    # Itera sobre a lista de alunos da turma.
    for aluno in lista_filtro_aluno:
        print(f"Aluno: {aluno['nome']} (Matrícula: {aluno['matricula']})")
        
        # Obtém as disciplinas que o professor pode lecionar.
        lista_materias = escolha_diciplina(nome_usuario)
        
        disciplina_selecionada = None # Inicializa a variável.
        
        if lista_materias: 
            # Se houver mais de uma disciplina, pede a escolha.
            if len(lista_materias) > 1:
                escolha = int(input("Digite o número da disciplina: ")) - 1
                disciplina_selecionada = lista_materias[escolha]
            else: 
                # Se for apenas uma, seleciona automaticamente.
                disciplina_selecionada = lista_materias[0]
                
            # Chama o método para coletar as notas e salvá-las no JSON.
            add_nota.adcionando_notas(nome_usuario, aluno, disciplina_selecionada)
        else:
             print(f"ERRO: Professor {nome_usuario} não tem disciplinas definidas para lançar notas.")