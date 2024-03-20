distancia_metros = float(input("Digite a distancia percorrida em metros: "))
tempo = float(input("Digite o tempo levado em segundos: "))



velocidade_media = distancia_metros // tempo

velocidade_km = 3.6 * velocidade_media

print("A velocidade média em m/s é: ", velocidade_media)
print("A velociade média em km/h é: ", velocidade_km)