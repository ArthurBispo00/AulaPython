numero_rm = int(input("Digite o RM: "))

primeiro_numero = numero_rm // 10000
segundo_numero = (numero_rm // 1000) % 10
terceiro_numero = (numero_rm // 100) % 10
quarto_numero = (numero_rm // 10) % 10
quinto_numero = numero_rm % 10

somatoria = primeiro_numero + segundo_numero + terceiro_numero + quarto_numero + quinto_numero

print("A somatoria do rm é: ", somatoria)