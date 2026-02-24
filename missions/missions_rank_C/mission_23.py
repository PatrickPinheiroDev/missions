def calcular_area(largura, altura):
    return (largura * altura) 

print("O engenheiro da cidade precisa calcular área de vários terrenos.")
input("Clique em qualquer tecla para iniciar: ")
print("---------------------------------------")

while True:
    largura = float(input("Digite a largura do terreno: "))
    altura = float(input("Digite a altura do terreno: "))
    print(f"O total da área é: {calcular_area(largura, altura)} m²")
    continuar = input("Gostaria de continuar(s/n): ").lower()
    if continuar == "n":
        print("\nEspero ter ajudado, até a próxima!")
        break
    print("---------------------------------------")


# nota 8.5 - 10