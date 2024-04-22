idade = int(input("Informe a idades das pessoas: "))

if idade >= 5 and idade <= 7:
    print("criança")
elif idade >= 8 and idade <= 10:
    print("criança")
elif idade >= 11 and idade <= 13:
    print("jovens")
elif idade >= 14 and idade <= 17:
    print("jovens")
elif idade >= 18:
    print("adulto")
else:
    print("idade invalida")