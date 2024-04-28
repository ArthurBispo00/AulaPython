num = int(input("Digite um numero positivo: "))

divisor = 0

while num <= 0 :
    print(f"Dado invalido, o numero {num} não é divisivel ou é negativo")
    num = int(input("Digite um numero positivo: "))

div = num

while num >0:
    resultado = div % num
    if resultado == 0:
        divisor = divisor + 1
    num = num - 1

print(f"A quantidade de divisores de {div} é: ", divisor)