# 📜 Ordenação dos Pergaminhos
lista_de_pergaminhos_para_feiticos = ["\nBola de Fogo", "Armadura de Gelo", "Drenar Vida", "Cura Menor", "Evocação de Mortos", "Grito da Morte", "Fúria da Natureza", "Invisibilidade", "Karaté Arcano", "Luz Sagrada", "Mão do Destino"]

print("Olá mago, você acaba de chegar na biblioteca de pergaminhos de feitiços...\nO bibliotecário precisa da sua ajuda para ordenar os pergaminhos em ordem alfabética.")
print("---------------------")
print("Atualmente está uma bagunça, olhe isto: ")
print(*lista_de_pergaminhos_para_feiticos, sep='\n')

input("\nClique em uma tecla qualquer para conjurar o feitiço da organização alfabética: ")
print("----------------------------------------------------")

lista_de_pergaminhos_para_feiticos.sort()
print("O feitiço foi lançado e agora está tudo em ordem alfabética!\nVeja abaixo: ")
print(*lista_de_pergaminhos_para_feiticos, sep='\n')
print("\nO bibliotecário agradece imensamente seus serviços.\n")

# nota 10