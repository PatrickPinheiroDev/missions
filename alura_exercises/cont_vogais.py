lista_de_vogais = ["a","e","i","o","u"]

texto = input("Digite um texto: ")

contador_de_vogais = 0

for caractere in texto.lower():
    if caractere in lista_de_vogais:
        contador_de_vogais += 1

print(contador_de_vogais)

#ou

# def contar_vogais(texto):  
#     vogais = "aeiou"  
#     quantidade = 0  
 
#     for letra in texto.lower():  
#         if letra in vogais:  
#             quantidade += 1  
 
#     return quantidade  
 
# texto = input("Digite um texto: ") 
 
# print(f"O texto contém {contar_vogais(texto)} vogais.")
