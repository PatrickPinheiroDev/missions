# 🔢 Selo da Paridade

print("Você foi designado para ajudar o tesoureiro a classificar moedas mágicas,\npara isso é necessário identificar os números pares e impares!")
print("-------------------------------------")
input("\nClique em uma tecla para executar a magia necessária: ")


def impar_ou_par():
    while True:
        numero_digitado = int(input("\nDigite um número: "))
        if numero_digitado % 2 == 0:
            print("É par!")
        else:
            print("É ímpar!")
        
        continuar = input("Deseja continuar(s/n): ").lower()
        if continuar == "n":
            print("\nO tesoureiro diz: 'Muito obrigado, sua magia é excepcional!'")
            break

impar_ou_par()

# nota 10        
                   
