num_real_positivo = int(input("Digite a quantidade de numeros inteiros: "))

qtd_num_positivos = 0
qtd_num_negativos = 0

for n in range(num_real_positivo):
    real = int(input(f"Digite o {n+1}: "))
    if real >=0:
        qtd_num_positivos = qtd_num_positivos + 1

num_seq_reais = int(input("Digite a quantidade de numeros que queres na sequencia: "))

for i in range(num_seq_reais):
    seq = int(input(f"Digite o {i+1} da sequencia: "))
    if seq >=0:
        qtd_num_positivos = qtd_num_positivos + 1
    else:
        qtd_num_negativos = qtd_num_negativos + 1
        
print("A quantidade de números reais positivos é: ",qtd_num_positivos)
print("A quantidade de números negativos são: ", qtd_num_negativos)