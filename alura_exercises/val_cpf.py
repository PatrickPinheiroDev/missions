cpf_fornecido = input("Digite seu CPF: ")

try:
    cpf_convertido = int(cpf_fornecido)

    if len(cpf_fornecido) != 11:
        print("Erro: O CPF deve ter exatamente 11 dígitos.")
    else:
        print("Tamanho do CPF correto, verificado!")    

except ValueError:
    print("Erro: O CPF deve conter apenas números.")

# OUTRA POSSÍVEL SOLUÇÃO:
# 
# def validar_cpf(cpf):
#     if not cpf.isdigit():
#         return "Erro: O CPF deve conter apenas números."
#     if len(cpf) != 11:
#         return "Erro: O CPF deve ter exatamente 11 dígitos."
#     return "CPF válido."
 
# cpf = input("Digite seu CPF: ")
# print(validar_cpf(cpf))