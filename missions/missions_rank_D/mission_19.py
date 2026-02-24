# 🧭 Coordenadas do Portal
print("Um portal só abre se as coordenadas X e Y forem positivas...\nForneça corretamente as coordenadas.\n---------------------------------")

coordenada_x = float(input("Digite a coordenada x: "))
coordenada_y = float(input("Digite a coordenada y: "))


print("---------------------------------")

if coordenada_x > 0 and coordenada_y > 0:
    print("Portal Aberto")
else:
    print("Falha na Ativação")    

# nota 10