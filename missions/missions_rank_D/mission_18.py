# 📊 Controle de Temperatura do Armazém

print("O responsável pelo armazém precisa garantir que a temperatura esteja dentro do intervalo seguro para armazenar poções raras.")
print("-----------------------------")

temperatura_atual = int(input("Digite a temperatura atual: "))

print("\nDescubra se essa temperatura é a ideal...")
input("Para isso, clique em qualquer tecla para lançar o feitiço: ")
print("-----------------------------")

if 15 <= temperatura_atual <= 25:
    print("Temperatura Segura")
else:
    print("Temperatura Fora do Padrão")

# nota 10