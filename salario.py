professor_hora_aula = int(input("informe o valor liquido que o professor ira receber:"))

numeros_de_horas = int(input("informe o valor liquido que o professor ira receber em horas:"))

numero_total_de_atividades_extras = float(input("informe o valor liquido que o professor ira receber em horas extras:"))

valor_total_do_desconto = float(input("informe o valor descontado do valor liquido do professor:"))

valor_liquido = (professor_hora_aula * numeros_de_horas) + numero_total_de_atividades_extras - valor_total_do_desconto

print(f'o valor liquido do professor é{valor_liquido}')