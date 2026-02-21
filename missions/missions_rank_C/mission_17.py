# 🧾 Registro de Recrutas
print("A guilda precisa registrar nomes de novos recrutas...")
input("Clique em uma tecla para lançar o feitiço e registrar nomes: ")

lista_de_nomes = []

while True:
    nome = input("Digite seu nome: ").lower()
    lista_de_nomes.append(nome)
    continuar = input("Gostaria de registrar mais algum nome(s/n): ").lower()
    if continuar == "n":
        break

print("-------------------")
input("Agora clique em qualquer tecla para conjurar o feitiço que vê a quantidade de registros: ")
print("-------------------")
print(f"Foram registrados {len(lista_de_nomes)} recrutas!")

# nota 9.5
