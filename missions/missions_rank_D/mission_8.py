# 📚 Registro de Recrutas

registros_de_membros_da_guilda = {
    "membro_1": {"nome": "boladin", "idade": 90, "classe": "goblin" },
    "membro_2": {"nome": "boladao", "idade": 350, "classe": "orc"},
    "membro_3": {"nome": "pidao", "idade": 130, "classe": "lobisomem"},
    "membro_4": {"nome": "eragon", "idade": 500, "classe": "tenebroso"}
}

print("Olá, jovem aventureiro!")
novo_membro = input("Gostaria de se registrar como membro da guilda (s/n): ").lower()

if novo_membro == "s":
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    classe = input("Digite sua classe: ")

    proximo_id = len(registros_de_membros_da_guilda) + 1
    nova_chave = f"membro_{proximo_id}"

    # 3. Adiciona ao dicionário
    registros_de_membros_da_guilda[nova_chave] = {
        "nome": nome, 
        "idade": idade, 
        "classe": classe
    }

    print(f"\nBem-vindo, {nome}! Você foi registrado como {nova_chave}.")

else:
    print("\nUma pena... Volte quando estiver pronto para a aventura!")


print("\n--- Registros Atualizados ---")
for id, info in registros_de_membros_da_guilda.items():
    print(f"{id}: {info['nome']} ({info['classe']}) - {info['idade']} anos")

# nota 10