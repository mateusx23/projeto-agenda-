matriz = []
 
while True:
 
 selecione = int(input ("Selecione 1 - cadastro, 2- notas , 3- aluno ,9- sair:  "))
 
 
 if selecione == 1:
    aluno = str(input("informe o nome: "))
    email = str(input("informe o email: "))
    telefone = int(input("informe o numero de telefone: "))
    notas1 = float(input ("Informe a nota 1: "))
    notas2 = float(input("Informe a nota 2: "))
    notas3 = float(input("informe a nota 3: "))
    notas4 = float(input("informe a nota 4: "))
    matriz.append([aluno, email, telefone, notas1, notas2 ,notas3,notas4])

    media = (notas1 + notas2) + (notas3 + notas4) / 2 

 if media >= 10:
     print("aprovado com distinçao")
 elif media >= 7:
     print("aprovado")
 elif media >= 5:
     print("aprovado na media")
 elif media >= 4:
     print("reprovado")

 elif selecione == 2:
        print(matriz)
 
 elif selecione == 9:
    print("Sair")
    break