n = int(input("Digite o número inteiro n: "))
 
sequencia = []
 
contador = 0
while contador < n:
    sequencia.append(int(input("Digite um número: ")))
    contador += 1
 
numeros_iguais = 0
if n == 1:
    numeros_iguais = 1
if n > 0 and n != 1:        
    i = 0
    j = 0
    while i < n:
        j = i + 1
        while j < n:
            if sequencia[i] > 0:
                if sequencia[i] == sequencia[j]:
                    if numeros_iguais == 0:
                        numeros_iguais += 1
                    numeros_iguais += 1
            j += 1
        i += 1
 
print("Número total de números iguais na sequência:", numeros_iguais)