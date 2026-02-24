# 🌪 Defesa Contra Lobos da Montanha

niveis_de_ameaça = [1,1,2,2,2,3,4,5,5,5,5,6,7,8,8,8,8,8,8,9,10,10,10]

print("Um grupo de lobos com diferentes níveis de ameaça foi avistado.\nApenas os de ameaça alta devem ser marcados...")

input("\nClique qualquer tecla para filtrar os lobos com maior nivel de ameaça: ")
print("------------------------------------------------")
for nivel in niveis_de_ameaça:
    if nivel >= 8:
        print(nivel)
print("------------------------------------------------")   
print("Filtragem realizada com sucesso...")
input("\nClique em qualquer tecla para marcar esses lobos: ")     
print("\nA magia Marca do Caçador foi ativada e todos os lobos de alta ameaça estão marcados por ela, muito bem!\n")        

# nota 10 