produtos = []


valor_total_estoque = 0
quantidade_produtos = 0

while True:
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))

    produto = {'nome': nome, 'preco': preco, 'quantidade': quantidade}
    produtos.append(produto)

    valor_total_estoque += preco * quantidade
    quantidade_produtos += 1

    resposta = input("Deseja continuar cadastrando produtos? (s/n)")
    if resposta.lower() == 'n':
        break

print("Valor total do estoque:", valor_total_estoque)
print("Quantidade de produtos cadastrados:", quantidade_produtos)