gols_a = int(input("Gols A: "))
gols_b = int(input("Gols B: "))

# Decidindo resultado
if gols_a == gols_b:
    print("Empate")
else:
    if gols_a > gols_b:
        print("Time A")
    else:
        print("Vencedor Time B")

print("Fim do programa")
