n_produtos = int(input("Digite o Número de Produtos: "))
 
cont = 0
referencia = 0
referencia2 = 0

while cont < n_produtos:    
    valor_anterior = float(input("Digite o Valor anterior: "))
    valor_com_aumento = float(input("Digite o Valor após aumento: "))
    cont += 1
    Valor_em_Real = valor_com_aumento - valor_anterior
    Valor_em_Porc = (valor_com_aumento * 100) // valor_anterior
    if Valor_em_Real > referencia:
        maior_valor_real = Valor_em_Real
    if Valor_em_Porc > referencia2:
        maior_valor_porc = Valor_em_Porc
    referencia = Valor_em_Real
    referencia2 = Valor_em_Porc
print("Maior valor em real:", maior_valor_real)
print("Maior valor em porc:",maior_valor_porc,"%")