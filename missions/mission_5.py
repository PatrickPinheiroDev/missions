# 📜 O Pergaminho das Runas

print("Me diga a palavra ou texto que eu irei revelar os padrões ocultos\n---------------")
escolha_do_texto = input("Escreva aqui sua palavra/frase: ")

total_de_caracteres = len(escolha_do_texto.replace(" ", ""))
total_de_palavras = len(escolha_do_texto.split())

print(f"Total de caracteres: {total_de_caracteres} caracteres.")
print(f"Total de palavras: {total_de_palavras} palavras.")
print(escolha_do_texto.upper())
print(escolha_do_texto.lower())

# nota 10