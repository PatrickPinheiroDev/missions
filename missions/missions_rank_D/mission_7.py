# ⚔ Ataque aos Goblins do Bosque

inimigos = {"goblin": 10, "orc": 40, "lobisomem": 20, "tenebroso": 35}

print("Um grupo pequeno de goblins está atacando viajantes. É preciso identificar os mais fracos para um ataque rápido!")
print("--------------------------------------------------")
print("Abaixo tem a lista com os inimigos mais fracos \n")

for nome, vida in inimigos.items():
    if vida <= 20:
        print(f"{nome}: {vida} de hp")

input("Clique em qualquer tecla para liberar a magia: ")
print("Muito bem invocador, a magia chama seletiva foi lançada")
print("--------------------------------------------------")
print("Você venceu!")
        
# nota 10