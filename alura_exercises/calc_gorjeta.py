from funcoes import valor_da_gorjeta, valor_total

valor_da_conta = float(input("Digite o valor da conta: "))
porcentagem_da_gorjeta = float(input("Digite a porcentagem de gorjeta(%): "))

print(f"Valor da gorjeta: R$ {valor_da_gorjeta(valor_da_conta, porcentagem_da_gorjeta):.2f}")
print(f"Total a pagar: R$ {valor_total(valor_da_conta, porcentagem_da_gorjeta):.2f}")