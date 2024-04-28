opcao = 0

import time

while opcao !=6:
    print("Locadora FIAP")
    print("1 - Alugar carro \n2 - Cadastro cliente")
    print("3 - Consulta carro \n4 - Análise de Crédito")
    print("5 - Fale conosco \n6 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        cpf = int(input("Informe o CPF: "))
        cartegoria = int(input("Informe a categoria (básico, premium e luxo): "))
        print("cod 224 bmw 2020 R$ 500")
        print("cod 238 audi Q3 2020 R$500")
        print("cod 237 mercdez gla 2020 R$ 450")
        codigo = int(input("Codigo do Veiculo"))
        dias = int(input("Informe quantidade de dias "))
        print("Você alugou uma BMW 2020 e vai pagar no total R$: ", dias*500)
        time.sleep(2)

    elif opcao == 2:
        pass
    elif opcao == 3:
        pass
    elif opcao == 4:
        pass
    elif opcao == 5:
        email = input("informe o email")
        Pergunta = input("Pergunta duvidas")
        print("Mais tarde breve entramos em contato")
        print(" obrigado por utilizar nossos Servicos")
    else:
        print("opcao invalida")