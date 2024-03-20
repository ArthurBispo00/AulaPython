valor_do_produto = float(input("Digite o preço: "))
valor_do_desconto = float(input("Digite o desconto percentual: "))
valor_do_aumento = float(input("Digite o aumento percentual: "))

percentual_de_aumento = 0
percentual_de_desconto = 0

if valor_do_aumento != 0:
    percentual_de_aumento = valor_do_aumento / 100
elif valor_do_desconto != 0:
    percentual_de_desconto = valor_do_desconto / 100

# Cálculo do preço final
resultado = valor_do_produto * (1 + percentual_de_aumento) * (1 - percentual_de_desconto)

print("O preço final é:", resultado)

