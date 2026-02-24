# 📦 Relatório de Entregas

print("Um mercador precisa saber quantas entregas foram concluídas com sucesso.")
input("Clique em uma tecla qualquer para exibir a lista: ")

concluidas = ["Sucesso", "Sucesso", "Falha", "Falha", "Falha", "Sucesso", "Falha", "Falha", "Falha", "Sucesso"]

print("-----------------lista------------------")
print(*concluidas, sep="\n")
print("----------------------------------------")

input("Clique em qualquer tecla para usar o feitiço de contagem: ")

contador_sucesso = 0

for entrega in concluidas:
    if entrega == "Sucesso":
        contador_sucesso += 1

print("\nContagem realizada...")
input("\nClique em qualquer tecla para mostrar a quantidade para o mercador: ")
print("----------------------------------------")
print(f"\n{contador_sucesso} entregas foram concluídas com sucesso.\n")
        
# nota 10

