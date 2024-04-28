pri = int(input("Digite o primeiro numero: "))
sec = int(input("Digite o segundo numero: "))
terc = int(input("Digite o terceiro numero: "))
quart = int(input("Digite o quarto numero: "))
quint = int(input("Digite o quinto numero: "))

Par1 = 0
Par2 = 0
Par3 = 0
Par4 = 0
Par5 = 0

if pri % 2 == 0:
    Par1 = pri
if sec % 2 == 0:
    Par2 = sec
if terc % 2 == 0:
    Par3 = terc
if quart % 2 == 0:
    Par4 = quart
if quint % 2 == 0:
    Par5 = quint

soma_pares = Par1 + Par2 + Par3 + Par4 + Par5
print("Soma dos números pares:", soma_pares)


