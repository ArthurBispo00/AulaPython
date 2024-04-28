dec = int(input("Informe o numero: "))

resp = ""


while dec > 0:
    res = dec % 16
    resp = str(res) + resp
    dec = dec // 16

if(resp > 9 and resp>= 10):
    print("A", res)

    
