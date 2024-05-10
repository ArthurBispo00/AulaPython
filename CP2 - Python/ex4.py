n_inteiro = int(input("Digite um numero inteiro: "))
cont = 0
soma_50 = 0
numeros_menor_100 = 0

while cont < n_inteiro:
    sequencia = int(input("Digite os numeros da sequencia: "))
    if sequencia >= 50:
        soma_50 = soma_50 + sequencia
    if sequencia < 100:
        numeros_menor_100 += 1
    cont += 1

print("A somatória de numeros igual á 50: ", soma_50)
print("A somátoria de numeros menor que 100:", numeros_menor_100)

