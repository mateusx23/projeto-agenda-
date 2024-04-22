numeros = []
while True:

    num = int(input("Digite um número (0 para sair): "))
    
    if num == 0:
        break 
        
    numeros.append(num)
    
soma = sum(numeros)

media = soma / len(numeros)

num_elementos = len(numeros)

print("Soma:", soma)
print("Média:", media)
print("Número de elementos:", num_elementos)