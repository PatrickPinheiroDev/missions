# 🏛 O Registro Oficial da Estalagem

from random import randint

def cadastro_novo_hospede():
    lista_hospedes = []  
    while True: 
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        numero_do_quarto = randint(1, 151)

        hospede = {"nome": nome, "idade": idade, "numero do quarto": numero_do_quarto}
        lista_hospedes.append(hospede)  # adiciona à lista

        novo_cadastro = input("Deseja cadastrar mais alguém (s/n)? ").lower()
        if novo_cadastro == "n":
            break

    return lista_hospedes

lista_de_hospedes_cadastrados = cadastro_novo_hospede()
print(lista_de_hospedes_cadastrados)

# nota 10

