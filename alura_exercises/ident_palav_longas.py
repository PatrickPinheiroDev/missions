# receber texto
# transformar em palavras separadas dentro de uma lista
texto = input("Digite um texto: ").split(" ")
# contar quantidade de letras
palavras_longas = []

for palavra in texto:
    if len(palavra) >= 10:
        palavras_longas.append(palavra)

if palavras_longas:
    resultado = ", ".join(palavras_longas)
    print(f"Palavras longas encontradas: {resultado}")

else: 
    print("Nenhuma palavra longa foi encontrada no texto.")
#exibir todas as palavras que possuem mais de 10 letras. 


    