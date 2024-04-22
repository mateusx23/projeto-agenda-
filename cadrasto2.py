agenda = []

while True:
    print("\nMenu:")
    print("1 - Cadastrar um novo contato")
    print("2 - Listar todos os contatos da agenda")
    print("9 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o e-mail do contato: ")

        contato = {
            "Nome": nome,
            "Telefone": telefone,
            "Email": email
        }

        agenda.append(contato)
        print("Contato cadastrado com sucesso!")

    elif opcao == 2:
        print("\nContatos da agenda:")
        for contato in agenda:
            print("-" * 30)
            print("Nome:", contato["Nome"])
            print("Telefone:", contato["Telefone"])
            print("Email:", contato["Email"])

    elif opcao == 9:
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida! Digite novamente.")