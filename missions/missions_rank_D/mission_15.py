# 🏹 Treinamento de Resistência

print("O treinador da guilda quer saber o maior valor de resistência entre os recrutas...\nPara isso você foi selecionado para lançar o feitiço maximus!")
print("Abaixo está a lista de resistência: ")
print("--------------------------------------")

resistencia_dos_recrutas = [2,5,20,50,12,24,65,23,78,99,105]

print(*resistencia_dos_recrutas, sep='\n')

input("\nClique em qualquer tecla para lançar o feitiço: ")
print("\n------------------------------------")

print(f"O feitiço foi concretizado, o maior valor é: {max(resistencia_dos_recrutas)}\n")

# nota 7.5