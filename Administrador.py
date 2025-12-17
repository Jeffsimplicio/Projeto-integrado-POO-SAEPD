from Professor import cad_professor  # Importa a função cad_professor do módulo Professor, responsável por cadastrar novos docentes no sistema.
from Turma import cad_turma          # Importa a função cad_turma do módulo Turma, utilizada para registrar novas turmas acadêmicas.
from Responsavel import cad_responsavel  # Importa a função cad_responsavel do módulo Responsavel, destinada ao cadastro de responsáveis pelos alunos.
from Aluno import cad_aluno

def iniciar_cadastro(nome_usuario):  # Define a função iniciar_cadastro, que recebe como parâmetro o nome do usuário autenticado.
    
    while True:  # Estrutura de repetição infinita, garantindo que o menu seja exibido continuamente até que o usuário opte por sair.
        print(f"que deseja fazer? {nome_usuario}")
        opcao = int(input(f""" 
1 -> CADASTRAR PROFESSOR
2 -> CADASTRAR ALUNOS
3 -> CADASTRAR TURMA
4 -> CADASTRAR RESPONSAVEL
5 -> Exit
    """))
        
        if opcao == 1:  # Caso a opção escolhida seja 1, inicia o processo de cadastro de professor.
            print("\n")  # Imprime uma quebra de linha para melhor formatação visual.
            cad_professor()  # Chama a função cad_professor para executar o cadastro de docentes.
        if opcao == 2:  # Caso a opção escolhida seja 2, inicia o processo de cadastro de professor.
            print("\n")  # Imprime uma quebra de linha para melhor formatação visual.
            cad_aluno()  # Chama a função cad_aluno para executar o cadastro de docentes.
        elif opcao == 3:  # Caso a opção escolhida seja 3, inicia o processo de cadastro de turma.
            print("\n")  # Imprime uma quebra de linha para separar visualmente as ações.
            cad_turma()  # Chama a função cad_turma para executar o cadastro de turmas.
        elif opcao == 4:  # Caso a opção escolhida seja 4, inicia o processo de cadastro de responsável.
            print("\n")  # Imprime uma quebra de linha para clareza na saída.
            cad_responsavel()  # Chama a função cad_responsavel para executar o cadastro de responsáveis.
        elif opcao == 5:  # Caso a opção escolhida seja 5, encerra o loop e finaliza o menu de cadastro.
            break  # Interrompe a execução do laço while, encerrando a função.
        elif opcao not in [1, 2, 3, 4, 5]:  # Caso o usuário insira um valor fora das opções válidas.
            print("Opção inválida. Escolha de 1 a 5.")  # Exibe mensagem de erro orientando a escolha correta.
