#🪙 Separação das Moedas Reais

print("O tesoureiro deseja separar as moedas de valor alto das de valor baixo... ")
print("--------------------------------------------")
input("Para isso, clique em uma tecla para criar um sistema: ")

moedas = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

moedas_com_valor_baixo = []
moedas_com_valor_alto = []

for valor in moedas:
    if valor >= 50:
        moedas_com_valor_alto.append(valor)
    else:
        moedas_com_valor_baixo.append(valor)

print("--------------------------------------------")
print("Muito bem mago, o sistema foi criado e as moedas já foram separadas...\nmas elas estão ocultas!")
input("Para que o tesoureiro possa ter acesso, clique em uma tecla e conjure a magia do holograma: ")

print(f"\nSua conjuração teve sucesso, aqui está a lista das moedas com valor igual ou acima de 50: {moedas_com_valor_alto}")
print(f"E a lista das moedas com valor abaixo de 50: {moedas_com_valor_baixo}\n")

# nota 10