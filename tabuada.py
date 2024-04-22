def tabuada(N):
    for i in range(1, N+6):
        print(f"{i} x {N} = {i*N}")

N = int(input("Digite o valor de N: "))
tabuada(N)
