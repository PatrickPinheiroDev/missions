# 🔐 Verificação do Código Arcano

print("Você acabou de chegar em uma vila...\npara entrar, necessitam do código arcano para que o selo mágico seja liberado")
print("--------------------------------------")

codigo_do_selo_magico = input("Caro aventureiro, digite aqui o código arcano: ")
tamanho_do_codigo = len(codigo_do_selo_magico)

if tamanho_do_codigo >= 8:
    print("\nO código arcano está válido, está aqui seu selo mágico: 🏹\n")
else:
    print("\nCódigo inválido! Você não é quem diz ser...\nO selo foi bloqueado!\nNão ouse voltar aqui aventureiro.\n")    

# nota 10