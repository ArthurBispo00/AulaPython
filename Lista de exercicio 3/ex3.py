alunos = int(input("Digite o numero de alunos: "))

soma_notas = 0
qtd_aluno0a5 = 0
qtd_alunos6a10= 0

for n in range(alunos):
    nota = float(input(f"Digite a nota dos aluno{n+1}: "))
    if nota >= 0 and nota <= 5:
        qtd_aluno0a5 += 1
    else:
        qtd_alunos6a10 += 1 
    soma_notas = soma_notas + nota  
media_notas = soma_notas // alunos




print("A média das notas da turma é: ", media_notas)
print("A quantidade de alunos que tiraram entre 5 e 0 é: ", qtd_aluno0a5)
print("A quantidade de alunos que tiraram nota de 6 a 10 é: ", qtd_alunos6a10)