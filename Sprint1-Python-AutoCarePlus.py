import time  # Importa a bliblioteca time

while True:  # Não permite que o programa encerre
    #Mesagem inicial 
    print("########################################################-----Bem vindo ao AutoCarePlus------########################################################################"
    "\nOnde Seu carro e Bem vindo")
    #Informacões do Menu
    print("########################################################-----Digite a Opcão desejada:------########################################################################")
    print("1 - Agendar revisão  \n2 - Realizar AutoDiaguinostico")
    print("3 - Fale Conosco ")
    print("5 - Sair")
    
    # Variáveis para controle de opções e dados
    falharificada = 0
    anoverificado = 0
    ano = 0
    kmrodado = 0
    opcao_agendamento = 0
    multiplicador = 0
    marca = 0
    horario = 0
    modelo = 0
    marcaverificada = 0
    verificadados = 0
    bateria = 0
    
    #########AutoAgendamento######################################################
    
    # Comando de repetição para verificar se a opção digitada é válida (número entre 1 e 4)
    while verificadados == 0:
        opcao_desejada = input("Digite a Opcao desejada: ")
        #Verificar se o usuário digitou um caractér valido
        if opcao_desejada.isdigit():
            numero = int(opcao_desejada)
            opcao_desejada2 = int(opcao_desejada)
            verificadados = 1 #Finaliza a repetição se o usuario digitou um caracter valido exemplo no caso numeros e não letras
        else: #caso digite letra em vez de numero adverte o usuário
            print("Por favor, digite apenas números .")
    verificadados = 0
    
    # Se a opção não for válida, solicita novamente
    while opcao_desejada2 < 1 or opcao_desejada2 > 4:
        print("Opcao invalida")
        opcao_desejada2 = input("Digite a Opcao desejada:")
        print("1 - Agendar revisão  \n2 - Realizar AutoDiaguinostico")
        print("3 - pecas \n4 - Contato")
        print("5 - Sair")

    # Se a opção for agendar revisão
    if opcao_desejada2 == 1:
        CPF = int(input("Digite o CPF sem o traco: "))

        # Solicita a marca do veículo
        print("Qual Marca do veiculo")
        print("1 - Volkswagem  \n2 - Chevrolet")
        print("3 - Ford \n4 - FIAT")

        while verificadados == 0:
            marca = input("Digite a marca: ")
            if marca.isdigit():
                marcaverificada = int(marca)
                verificadados = 1
            else:
                print("Por favor, digite apenas números .")
        verificadados = 0
        
        # Verifica se a marca digitada é válida
        if marcaverificada == 1 or marcaverificada == 2 or marcaverificada == 3:
            modelo = str(input("Digite o modelo: "))

            while verificadados == 0:
                ano = input("Digite o ano: ")
                if ano.isdigit():
                    anoverificado = int(ano)
                    verificadados = 1
                else:
                    print("Por favor, digite apenas números .")

           #Verifica a quilometragem informada do veiculo
            kmrodado = float(input("Digite a km: "))
            if kmrodado >=1000 and kmrodado <20000:
                print("Valor da revisao para o veiculo",modelo,ano,"é",kmrodado*0.1)
            elif kmrodado >=20000 and kmrodado <30000:
                print("Valor da revisao para o veiculo",modelo,ano,"é",kmrodado*0.19)
            elif kmrodado >=30000 and kmrodado <40000:
                print("Valor da revisao para o veiculo",modelo,ano,"é",kmrodado*0.22)
            elif kmrodado >=40000 and kmrodado <50000:
                print("Valor da revisao para o veiculo",modelo,ano,"é",kmrodado*0.02)
            elif kmrodado >=50000 and kmrodado <60000:
                print("Valor da revisao para o veiculo",modelo,ano,"é",kmrodado*0.01)
            elif kmrodado >=60000 and kmrodado <70000:
                print("Valor da revisao para o veiculo",modelo,ano,"é",kmrodado*0.2)
            elif kmrodado >=70000 and kmrodado <80000:
                print("Valor da revisao para o veiculo",modelo,ano,"é",kmrodado*0.2)
            elif kmrodado >=80000 and kmrodado <90000:
                print("Valor da revisao para o veiculo",modelo,ano,"é",kmrodado*0.2)
            elif kmrodado >=90000 and kmrodado <100000:
                print("Valor da revisao para o veiculo",modelo,ano,"é",kmrodado*0.2)
            elif kmrodado >= 100000:
                print("entrar em contato via telefone")

            # Oferece a opção de agendar o serviço
            print("Deseja agendar servico:")
            print("1 - sim  \n2 - nao")
            opcao_agendamento = int(input("Digite a opcao:"))
            if opcao_agendamento == 1:
                data_marcada = str(input("Digite a data desejada para atendimento: "))
                print("Escolha os horarios disponiveis para data: ")
                print("1 - 8:00  \n2 - 11:45")
                print("3 - 9:00 \n4 - 12:30")
                horario = int(input("Selecione horario"))
                #verifica se foi digitado somente as opções de 1 a 4 se não advere o usuário
                while horario < 1 or horario > 4:
                    print("opcao invalidada")            
                    horario = int(input("Selecione horario")) 
                print("Servico agendado para o CPF:", CPF, "para veiculo", modelo, "\npara data:", data_marcada, "e o horario selecionado")
                time.sleep(3)
            else:
                print("Volte sempre!")
                time.sleep(3)

    # Fim do bloco de agendamento
    
    # Bloco para realizar auto diagnóstico
    elif opcao_desejada2 == 2:
        placa = str(input("Digite A PLACA: "))

        # Solicita a marca do veículo
        print("Qual Marca do veiculo")
        print("1 - Volkswagem  \n2 - Chevrolet")
        print("3 - Ford \n4 - FIAT")
        #Verificar se o usuário digitou um caractér valido
        while verificadados == 0:
            marca = input("Digite a marca: ")
            if marca.isdigit():
                marcaverificada = int(marca)
                verificadados = 1
            else:
                print("Por favor, digite apenas números .")
        verificadados = 0
        #Verifica qual a marca foi selecionada pelo usuario se for maior que 4 adverte usuario
        while marcaverificada < 1 or marcaverificada > 4:
            print("Opcao invalida")

        modelo = str(input("Digite o modelo: "))
        #Verificar se o usuário digitou um caractér valido
        while verificadados == 0:
            ano = input("Digite o ano: ")
            if ano.isdigit():
                anoverificado = int(ano)
                verificadados = 1
            else:
                print("Por favor, digite apenas números .")

        print("###################Autodiaguinostico##################################"
            "\nSELECIONE A ORIGEM DA FALHA")
        #Menu de Falhas do carro
        print("1 - BATERIA  \n2 - MECANICO")
        print("3 - PANE-ELETRICA")
        print("5 - Sair")
        verificadados = 0
        #Verificar se o usuário digitou um caractér valido
        while verificadados == 0:
            falha = input("Selecione a origem da falha: ")
            if falha.isdigit():
                falharificada = int(falha)
                verificadados = 1
            else:
                print("Por favor, digite apenas números .")

        while falharificada < 1 or falharificada > 3:
            print("Opcao invalida")
        #Caso a falha seja na bateria
        if falharificada == 1:
            print("No INDICADOR DE NIVEL DE BATERIA INDICAR QUAL COLORACAO:")
            print("1 - VERDE  \n2 - PRETO")
            print("3 - BRANCO  \n2")
            verificadados = 0
            #Verificar se o usuário digitou um caractér valido
            while verificadados == 0:
                bateria = input("Selecione a cor: ")
                if bateria.isdigit():
                    bateriaverificada = int(bateria)
                    verificadados = 1
                else:
                    print("Por favor, digite apenas números .")
            #verifica qual opção de falha na bateria e selecionada
            if bateriaverificada == 1:
                print("Bateria esta carregada, será necessário agendamento de uma revisão")
                time.sleep(3)
            elif bateriaverificada == 2:
                ("Será necessário a troca da bateria devido ter chego ao fim de sua vida útil")
                time.sleep(3)
            else:
                print("Será necessário carga na bateria")
                time.sleep(3)
    # Fim do bloco de auto diagnóstico
    
    # Bloco para falar com a equipe de suporte
    elif opcao_desejada2 == 3:
        email = input("Informe o email: ")
        pergunta = input("Pergunta dúvidas: ")
        print("Mais tarde breve entraremos em contato")
        print("Obrigado por utilizar nossos serviços")
        time.sleep(3)
    # Fim do bloco de suporte

    # Se a opção for inválida
    else:
        print("opcao invalida")
        time.sleep(3)
        
    # Verifica se o usuário escolheu sair do programa
    if opcao_desejada2 == 5:
        break  # Sai do programa e finaliza
