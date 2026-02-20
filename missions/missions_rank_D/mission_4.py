# 🎒 O Depósito da Taverna

lista_de_itens = []

print("Olá taverneiro, seja bem vindo ao sistema de controle de itens\n--------------------")

while True:
    escolha_do_taverneiro = input("O que deseja fazer (adicionar, remover ou verificar total): ")


    if escolha_do_taverneiro == "adicionar":
        item_adicionado = input("Qual o nome do item que gostaria de adicionar: ")
        lista_de_itens.append(item_adicionado)
        continuar = input("Para continuar usando o sistema clique 's': ")
        if continuar != 's':
            break


    elif escolha_do_taverneiro == "remover":
        item_removivel = input("Qual o nome do item que deseja remover: ")
        if item_removivel in lista_de_itens:
            lista_de_itens.remove(item_removivel)  
            continuar = input("Para continuar usando o sistema clique 's': ")
            if continuar != 's':
                break
        else:
            print(f"O item {item_removivel} já não consta na sua lista de itens.")

    elif escolha_do_taverneiro == "verificar total":
        print(len(lista_de_itens))
        continuar = input("Para continuar usando o sistema clique 's': ")
        if continuar != 's':
            break

    else:
        print("Você digitou uma opção inválida, tente novamente!")


print("Obrigado por ter utilizado nosso sistema.\n---------------")
print(f"Sua lista total de itens atualmente é: {lista_de_itens}, e a quantidade total é {len(lista_de_itens)} itens.")

# nota 9.5
