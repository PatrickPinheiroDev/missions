# 🔁 A Remoção da Maldição

print("Olá, bem-vindo ao nosso sistema\n---------------------")

senha = "admin"

while True:
    senha_digitada = input("Digite a sua senha: ")
    if senha_digitada == senha:
        print("Acesso liberado")
        break
    else:
        print("Você errou, tente novamente!")

# nota 10        