# 📦 Inventário da Guilda 

print("A guilda precisa listar todos os itens do estoque...")
input("Clique em qualquer tecla para exibir o inventario: ")

inventario_guilda = {
    "Moedas de Ouro": 1500,
    "Poções de Cura": 45,
    "Minério de Ferro": 120,
    "Couro de Dragão": 5,
    "Pergaminhos de Teleporte": 12,
    "Penas de Fênix": 3
}

print("\n----------inventário da guilda------------\n")

for key, value in inventario_guilda.items():
    print(f"{key}: {value}")
print("\n------------------------------------------")

print("Agora você precisa conjurar o feitiço de contagem de itens, precisamos de você!")
input("Clique em qualquer tecla para conjurar o feitiço: ")
print("\n------------------------------------------")
print(f"\nO feitiço funcionou, agora temos o total controle do sistema...")

total_estoque = sum(inventario_guilda.values())
print(f"\nTOTAL DE ITENS NO ESTOQUE: {total_estoque}")

# nota 8.5