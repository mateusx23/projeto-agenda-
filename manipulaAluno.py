def cadrasta(vetor):
    aluno = {}
    aluno  ['nome'] = input("informe o nome: ")
    aluno  ['disciplina'] = input("informe a disciplina : ")
    aluno  ['nota1'] = float(input("informe a nota 1 do aluno:"))
    aluno  ['nota2'] = float(input("informe a nota 2 do aluno: "))
    aluno  ['nota3'] = float(input("informe a nota 3 do aluno:"))
    aluno  ['nota4'] = float(input("informe a nota 4 do aluno:"))
    vetor.append(aluno)
def listar(turma):
        for matriculado in turma:
            media = (matriculado['nota1'] + matriculado['nota2'] + matriculado['nota3'] + matriculado['nota4']) / 4
            situaçao =''
            if media >= 7:
                situaçao = 'aprovado'
            else:
                situaçao = 'reprovado'
            print(f"""{matriculado['nome']} - {matriculado['disciplina']}
                   - {matriculado['nota1']} - {matriculado['nota2']}
                     - {matriculado['nota3']} - {matriculado['nota4']})
                        {media:.2f} - {situaçao}""")
def buscar(turma):
        nomebusca = input("informe o nome para excluir:")
        posicao = -1
        i = 0
        for m in turma:
            if m['nome'].lower() == nomebusca .lower():
                posicao = i
                break
            i = i + 1
        return posicao
def excluir(turma,posicao):
      if posicao > -1:
            turma.pop(posicao)
      else:
            print("Não encontrado")
def exibir(turma, posicao):
         if posicao > -1:
                print(f"""{turma[posicao]['nome']} - {turma[posicao]['disciplina']} - 
                      {turma[posicao]['nota1']} - {turma[posicao]['nota2']} 
                      {turma[posicao]['nota3']} - {turma[posicao]['nota4']} """)
                
def alterar(turma,posicao):
       if posicao > -1:
            turma[posicao]['nome'] = input("informe o nome: ")
            turma[posicao]['disciplina'] = input("informe a disciplina : ")
            turma[posicao]['nota1'] = float(input("informe a nota 1 do aluno:"))
            turma[posicao]['nota2'] = float(input("informe a nota 2 do aluno: "))
            turma[posicao]['nota3'] = float(input("informe a nota 3 do aluno: "))
            turma[posicao]['nota4'] = float(input("informe a nota 4 do aluno: "))
       else:
            print("nao encontrado.")
def feznada():
      print("estou fazendo nada")

                