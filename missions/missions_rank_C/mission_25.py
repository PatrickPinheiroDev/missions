# 🛡 Controle de Acesso à Fortaleza
senha = "ControleTotal_123"

tentativas = 3
print("Você tem 3 tentativas para inserir corretamente sua senha\nCaso erre as 3 tentativas seu acesso será bloqueado permanentemente...")


while tentativas > 0:
    tentativas -= 1
    senha_digitada = input("\nDigite aqui a sua senha: ")
    if senha_digitada == senha:
        print("\nAcesso Permitido")
        break
    else:
        print("\nAcesso Bloqueado")        

if tentativas == 0:
    print("\nVocê atingiu o limite de tentativas, seu acesso está com bloqueio permanente!")      
else:
    print("Bem-vindo(a)!")      

# nota 10 