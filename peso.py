altura = float(input("Digite a altura da pessoa:"))

sexo = str(input("Digite M ou F para o sexo da pessoa: "))

if sexo == "M":
    peso_ideal_masculino = (72.7*altura)-58
    print(f"seu peso ideal é{peso_ideal_masculino:.2f}")
elif sexo == "f": 
    peso_ideal_feminino = (62.1*altura)-44.7
    print(f"seu peso ideal e{peso_ideal_feminino:.2f}")
else:
    print("O peso ideal é:")