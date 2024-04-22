valor = int(input("informe o valor :"))

valor2 = int(input("informe o valor:"))

prestaçao = int(input("informe o valor da prestaçao:"))

taxa = float(input("informe o valor da taxa:"))

tempo = int(input("informe o valor do tempo:"))

dias_da_prestaçao = valor +(valor2 *(taxa / 100)* tempo)

print(f'O valor da prestaçao é {dias_da_prestaçao}')