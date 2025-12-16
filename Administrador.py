from Professor import cad_professor
from Turma import cad_turma
from Responsavel import cad_responsavel

def iniciar_cadastro( nome_usuario):
    print(nome_usuario)
    while True:
        opcao = int(input("""
O que deseja fazer?
1 -> CADASTRAR PROFESSOR
2 -> CADASTRAR ALUNOS
3 -> CADASTRAR TURMA
4 -> CADASTRAR RESPONSAVEL
5 -> Exit
    """))
        
        if opcao == 1:
            print("\n")
            cad_professor()
        elif opcao == 3:
            print("\n")
            cad_turma()
        elif opcao == 4:
            print("\n")
            cad_responsavel()
        elif opcao == 5:
            break
        elif opcao not in [1, 2, 3, 4, 5]:
            print("Opção inválida. Escolha de 1 a 5.")
        
