alunos = int(input("Digite o numero de alunos: "))

soma_notas = 0

for n in range(alunos):
    nota = float(input(f"Digite a nota dos aluno{n+1}: "))
    soma_notas = soma_notas + nota  
media_notas = soma_notas // alunos

print("A média das notas da turma é: ",media_notas)