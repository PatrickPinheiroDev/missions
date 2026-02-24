# 🧮 Contagem de Cristais de Mana

print("Um mago precisa saber quantos cristais possuem carga positiva.")

cargas = [-1, -4, -15, 13, 15, 60, 2, -6, -6, 2, 0]

print("Abaixo estão os valores de carga de cada cristal: ")
print("\n-----------------------cargas------------------------\n")
print(*cargas, sep=", ")
print("\n-----------------------------------------------------")

contador_de_cargas_positivas = 0

for valor in cargas:
    if valor > 0:
        contador_de_cargas_positivas += 1

input("Clique em qualquer tecla para conjurar o feitiço de cargas positivas: ")        

print("\nMuito bem...")
print(f"\nTotal de cargas positivas: {contador_de_cargas_positivas}")        

# nota 10