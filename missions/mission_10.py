# 🧊 Defesa Contra Slimes

print("Slimes invadiram o porão da taverna.\nApenas aqueles com resistência baixa podem ser congelados.")
print("\n----------------------------------------\n")
input("Clique em qualquer tecla para verificar a resistência mágica de todos: ")

resistencia_magica = [15, 12, 9, 20, 30, 5, 15, 50]

print(f"\nA resistência de cada um é: {resistencia_magica}\n")

input("Clique em qualquer tecla para filtrar apenas os que tem resistência menor ou igual a 15: ")

slimes_enfraquecidos = []

for nivel in resistencia_magica:
    if nivel <= 15:
        slimes_enfraquecidos.append(nivel)

print(f"\nLista de slimes com pouca resistência: {slimes_enfraquecidos}\n")

input("Agora clique em qualquer tecla para lançar a magia: ")

print("\nA magia geada cortante foi lançada, e...")
print(f"\nVocê eliminou 100% dos slimes enfraquecidos, muito obrigado mago supremo!\n")

# nota 10

