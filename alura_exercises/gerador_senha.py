import string
import secrets

letras_maiusculas = string.ascii_uppercase
letras_minusculas = string.ascii_lowercase
numeros = string.digits
simbolos = string.punctuation

lista_geral = [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation]
itens_da_lista_juntos = list("".join(lista_geral))
    
senha = secrets.choice(letras_maiusculas) + secrets.choice(letras_minusculas) + secrets.choice(numeros) + secrets.choice(simbolos) 

for _ in range(8):
    senha += secrets.choice(itens_da_lista_juntos)

lista_senha = list(senha)
secrets.SystemRandom().shuffle(lista_senha)
senha_final = "".join(lista_senha)

print(senha_final)











# alphabet = string.ascii_letters + string.digits
# password = ''.join(secrets.choice(alphabet) for i in range(8))

# print(password)