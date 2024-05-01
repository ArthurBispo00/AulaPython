p = 20
nM = 0 #Nota Maior
nm = 70 #Nota Menor
perc20 = 0 #Percentual de notas até 20 
perc50 = 0 #Percentual de notas entre 21 e 50 questões
perc70 = 0 #Percentual de notas de 51 até 70 questões
for n in range(p):
    nota = int(input(f"Digite a {n+1} nota: "))
    if nM < nota:
        nM = nota
    if nm > nota:
        nm = nota
    if nota < 21:
        perc20 = perc20 + 1
    elif nota > 20 and nota < 51:
        perc50 = perc50 + 1
    elif nota > 50:
        perc70 = perc70 + 1

Resultado1 = (perc20 * 100) / 20
Resultado2 = (perc50 *100) / 20
Resultado3 = (perc70 * 100) / 20

print("O Percentual de alunos que acertou até 20 é: ", Resultado1)
print("O Percentual de alunos que acertou entre 21 e 50 é: ", Resultado2)
print("O Percentual de alunos que acertou até 51 e 70 é: ", Resultado3)


