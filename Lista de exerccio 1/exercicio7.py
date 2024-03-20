def separar_digitos(numero):
    # Calcula o dígito das dezenas
    dezenas = numero // 10

    # Calcula o dígito das unidades
    unidades = numero % 10

    return dezenas, unidades

# Solicita ao usuário que insira um número entre 0 e 99
numero = int(input("Digite um número entre 0 e 99: "))

# Verifica se o número está dentro do intervalo permitido
if 0 <= numero <= 99:
    # Chama a função para separar os dígitos
    dezenas, unidades = separar_digitos(numero)
    
    # Imprime os resultados
    print("Dígito das dezenas:", dezenas)
    print("Dígito das unidades:", unidades)
else:
    print("O número inserido está fora do intervalo permitido.")
