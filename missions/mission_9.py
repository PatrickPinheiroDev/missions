# 🌙 Vigília na Torre Oeste
 
print("Guardião, precisamos de você!\nNos ajude a verificar se a torre tem visibilidade contra uma possível invasão.\n--------------------------")

input("Pressione qualquer tecla para descobrir: ")

tochas = [True, False, True, False, True, False, True, False]

total_de_tochas = len(tochas)
contador_de_tochas_acesas = 0

for fogo in tochas:
    if fogo  == True:
        contador_de_tochas_acesas += 1
            
if contador_de_tochas_acesas >= 4:
    print(f"De {total_de_tochas} tochas, {contador_de_tochas_acesas} delas estão acesas!\nJá é o suficiente, nossa visibilidade está garantida...")
else:
    print(f"De {total_de_tochas} tochas, somente {contador_de_tochas_acesas} delas estão acesas!\nMenos da metade da torre está com visibilidade, precisamos agir!")    

# nota 10    
