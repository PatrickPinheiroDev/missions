# 🔮 O Selo da Soma Elemental

print("Bem-vindo ao jogo!\n")
numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
print("--------------------------------------------------\n")

print(f"{numero_1} + {numero_2} é igual a: {numero_1 + numero_2}")
print(f"{numero_1} - {numero_2} é igual a: {numero_1 - numero_2}")
print(f"{numero_1} x {numero_2} é igual a: {numero_1 * numero_2}")
if numero_2 == 0:
    print(f"{numero_1} ÷ {numero_2} é impossível de ser executado, pois nenhum número é divisível por 0")
else:    
    print(f"{numero_1} ÷ {numero_2} é igual a: {numero_1 / numero_2:.1f}")

# Nota: 8.5 
# Esqueci de botar um f string e espaços de texto incorretos.
# Segunda nota: 10