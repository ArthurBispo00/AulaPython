x = -1
a = -1
b = -1

while x < 0:
    x = int(input("Digite o valor da cedula da troca: ")) 
while a < 0:
    a = int(input("Digite o valor da primeira moeda: ")) 
while b < 0:
    b = int(input("Digite o valor da segunda moeda: ")) 

if (x % a) == 0 and (x % b) == 0:
    comparacaoa = x // a
    comparacaob = x // b
    if comparacaoa < comparacaob:
         print("Possível: 0 moeda de ",b, "e", comparacaoa, "moeda(s) de", a)
    else:
        print("Possível: 0 moeda de ",a, "e", comparacaob, "moeda(s) de", b)
else:
    if (x % a) == 0:
        divisora = x // a
        print("Possível: 0 moeda de ",b, "e", divisora, "moeda(s) de", a)
    elif (x % b) == 0:
        divisorb = x // b
        print("Possível: 0 moeda de ",a, "e", divisorb, "moeda(s) de", b)
    if (x - a) % b == 0:
        divisor = (x-a) // b
        print("Possivel: 1 moeda de ", a, "e", divisor, "moeda(s) de ", b)
    elif (x - b) % a == 0:
        divisor = (x-b) // a
        print("Possivel: 1 moeda de ", b, "e", divisor, "moeda(s) de ", a)
    else:
        print("Não é possível fazer a troca")
    
    
