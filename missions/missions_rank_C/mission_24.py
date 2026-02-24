# 📊 Análise de Níveis de Energia

print("O conselho arcano precisa saber quantos níveis estão acima da média.")
input("Clique em qualquer tecla para conjurar a magia: ")
print("------------------------------------------------")
print("Magia conjurada...")

def media(lista):
    if not lista:  
        return 0
    return sum(lista) / len(lista)

lista_de_niveis_de_energia = [2, 5, 7, 8, 15, 25, 30, 32, 21, 34, 21, 22]

media_armazenada = media(lista_de_niveis_de_energia)

contador_de_valores_acima_da_media = 0

for valor in lista_de_niveis_de_energia:
    if valor > media_armazenada:
        contador_de_valores_acima_da_media += 1

input("\nClique em qualquer tecla para ver o resultado: ")

print(f"\n{contador_de_valores_acima_da_media} valores estão acima da média.")

# nota 9.5