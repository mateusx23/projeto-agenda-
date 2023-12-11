from manipulaAluno import buscar, cadrasta, excluir, exibir, listar
from ultils import menu


turma = []

while True:
    menu()

    opcao = int(input("informe a opção: "))
   
    if opcao == 1:
       cadrasta(turma)
    elif opcao == 2:
        listar(turma)    
    elif opcao == 3:
        posicao = buscar(turma)
        exibir(turma,posicao)
    elif opcao == 4:
        posicao = buscar(turma)
    elif opcao == 5:
        posicao = buscar(turma)
        excluir(turma,posicao)
    elif opcao == 9:
        break
    else:
        print("opçao invalida")