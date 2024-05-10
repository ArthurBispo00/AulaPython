def menu():
    print("\nDETRAN\n")
    print("1 - Inclui\n2 - Lista\n3 - Sai")
    opcao = int(input("Selecione: "))
    return opcao

def submenu():
    print("1 - Altera\n2 - Exclui\n3 - Faz nada")
    opcao = int(input("Selecione: "))
    return opcao

def altera_exclui(lista, pos, acao):
    ind = (pos - 1) * 5
    if acao == 2:
        for x in range(5):
            lista.pop(ind)
    elif acao == 1:
        altera_carro(lista,ind)
    else:
        print("Fazendo nada")

def altera_carro(lista,ind):
    mod = input(f"Modelo ({lista[ind]}): ")
    if len(mod) > 0:
        lista[ind] = mod

    mar = input(f"Marca ({lista[ind+1]}): ")
    if len(mar) > 0:
        lista[ind+1] = mar

    
    ver = input(f"Marca ({lista[ind+2]}): ")
    if len(ver) > 0:
        lista[ind+2] = ver

    
    ano = input(f"Marca ({lista[ind+3]}): ")
    if len(ano) > 0:
        lista[ind+3] = int(ano)
    
    
    pl = input(f"Marca ({lista[ind+4]}): ")
    if len(pl) > 0:
        lista[ind+4] = pl


def inclui_veiculo(lista):
    lista.append(input("Modelo: "))
    lista.append(input("Marca: "))
    lista.append(input("Versão: "))
    lista.append(int(input("Ano: ")))
    lista.append(input("Placa: "))

def lista_veiculo(lista):
    i=0
    j=0
    while i < len(lista):

        print(f"{j}) {lista[1]} {lista[i + 4]}")
        i = i + 5
        j = j + 1


op = menu()
carros = []
carros = ['Polo', 'Volks', 'MSI', 2023, 'XAB-4579', 'UP', 'Volksvagem', 'TSI', 2022, 'RTX']

while op!= 3:
    if op == 1:
        print("Inclui Veículo")
        inclui_veiculo(carros)
        print(carros)
    elif op == 2:
        print("Lista Veículo")
        lista_veiculo(carros)
        pos = int(input("Selecione o carro: "))
        acao = submenu()
        altera_exclui(carros, pos, acao)
    else:
        print("opcao inválida!")
    op = menu()