Salario_incial = float(input("Digite o salario incial: "))
Salario_final = float(input("Digite o salario recebido apos o aumento: "))

Resultado = (Salario_final * 100 // Salario_incial) - 100

print("o aumento foi de: ", Resultado, "%")