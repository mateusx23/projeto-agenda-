
from ultils import menu

turma = []

while True:
   

    opcao = int(input("informe a opção: "))
    if opcao == 1:
        cadrasta(turma)
        elif opcao == 2:
        for matriculado in turma:
            media = (matriculado['nota1'] + matriculado['nota2'] + matriculado['nota3'] + matriculado['nota4']) / 2
            situaçao =''
            if media >= 7:
                situaçao = 'aprovado'
            else:
                situaçao = 'reprovado'
            print(f"""{matriculado['nome']} - {matriculado['disciplia']}
                   - {matriculado['nota1']} - {matriculado['nota2']}
                     - {matriculado['nota3']} - {matriculado['nota4']})
                        {media:.2f} - {situaçao}""")
            
    elif opcao == 3:
        nomebusca = input("informe o nome para busca:")
        posicao = - 1
        i = 0
        for m in turma:
            if m['nome'].lower() == nomebusca .lower():
                posicao = i
                break
            i = i + 1

            if posicao > - 1:
                print(f"""{turma[turma[posicao]]['nome']} - {turma[turma[posicao]]['disciplina']} - 
                      {turma[turma[posicao]]['nota1']} - {turma[turma[posicao]]['nota2']} 
                      {turma[posicao]['nota3']} - {turma[turma[posicao]]['nota4']} """)
                



            #else:
               #print("nao encontrado")
    elif opcao == 4:
        nomebusca = input("informe o nome para alterar")

        posicao = -1
        i = 0
        for matriculado in turma:
            if matriculado['nome'].lower() == nomebusca.lower():
                posicao = i
                break
            i = i + 1
        if posicao > -1:

            turma[posicao]['nome'] = input("informe o nome: ")
            turma[posicao]['diciplina'] = input("informe a diciplina : ")
            turma[posicao]['nota1'] = float(input("informe a nota 1 do aluno:"))
            turma[posicao]['nota2'] = float(input("informe a nota 2 do aluno: "))
            turma[posicao]['nota3'] = float(input("informe a nota 3 do aluno: "))
            turma[posicao]['nota4'] = float(input("informe a nota 4 do aluno: "))
        else:
         print("nao encontrado.")
    elif opcao == 5:
        nomebusca = input("informe  o nome para excluir: ")
        
        posicao = -1
        i = 0
        for matricula in turma:
            if matricula['nome'].lower() == nomebusca.lower():
                posicao = i
                break
            i = i + 1
        if posicao > -1:
            turma.pop(posicao)
        else:
            print("nao encontrado")
    elif opcao == 9:
        break
    else:
        print("opçao invalida")