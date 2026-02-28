# 🔹 INICIALIZAÇÃO
saldo_final = 0.0
energia_restante = 0

# ---------------- PARTE 1 — Controle de Acesso ----------------
print("\n---------------- Controle de Acesso ao Distrito Comercial --------------------")
nome = input("\nDigite seu nome: ")
idade = int(input("Digite sua idade: "))
credencial = input("Digite a credencial (comum, mercador, nobre): ").lower()

if idade >= 18 or credencial == "nobre":
    print("\n✅ Entrada permitida!")
else:
    print("❌ Entrada bloqueada!")

# ---------------- PARTE 2 — Registro de Transações ----------------
print("\n------------------------ Registro de Transações -----------------------")
lista_de_transacoes = []

print("\nDigite os valores (positivos = venda / negativos = despesa).")
print("Digite 'fim' para encerrar o registro.")

while True:
    entrada = input("\nValor da transação: ").lower()
    if entrada == 'fim':
        break
    try:
        valor = float(entrada)
        lista_de_transacoes.append(valor)
    except ValueError:
        print("❌ Digite um número válido ou 'fim'.")

if lista_de_transacoes:
    vendas = sum([v for v in lista_de_transacoes if v > 0])
    despesas = sum([d for d in lista_de_transacoes if d < 0])
    saldo_final = sum(lista_de_transacoes)
    
    print(f"\nTotal de transações: {len(lista_de_transacoes)}")
    print(f"Soma das Vendas: R${vendas:.2f}")
    print(f"Soma das Despesas: R${despesas:.2f}")
    print(f"Saldo Final: R${saldo_final:.2f}")
    
    status = "Lucro" if saldo_final > 0 else "Empate" if saldo_final == 0 else "Prejuízo"
    print(f"Status: {status}")

# ---------------- PARTE 3 — Controle de Estoque ----------------
print("\n------------------------- Controle de Estoque ------------------------")
pocoes, pergaminhos, elixires = 50, 30, 20

if input("\nGostaria de retirar algum item (s/n): ").lower() == "s":
    while True:
        escolha = input("\nItem (Poções/Pergaminhos/Elixires): ").lower()
        try:
            qtd = int(input("Quantidade: "))
        except ValueError: continue

        if "poc" in escolha:
            if qtd > pocoes: print("⚠️ Estoque insuficiente!")
            else: 
                pocoes -= qtd
                if pocoes < 5: print(f"🚨 ALERTA: Estoque de Poções criticamente baixo ({pocoes})!")
        elif "perga" in escolha:
            if qtd > pergaminhos: print("⚠️ Estoque insuficiente!")
            else: 
                pergaminhos -= qtd
                if pergaminhos < 5: print(f"🚨 ALERTA: Estoque de Pergaminhos baixo ({pergaminhos})!")
        elif "elixir" in escolha:
            if qtd > elixires: print("⚠️ Estoque insuficiente!")
            else: 
                elixires -= qtd
                if elixires < 5: print(f"🚨 ALERTA: Estoque de Elixires baixo ({elixires})!")

        if input("\nRetirar mais algum? (s/n): ").lower() == "n": break

# ---------------- PARTE 4 — Energia Arcana ----------------
print("\n-------------- Verificação de Energia Arcana ---------------")
energia_atual = int(input("Energia atual: "))
custo = int(input("Custo do feitiço: "))

if energia_atual >= custo:
    energia_restante = energia_atual - custo
    print("✨ Magia Executada!")
else:
    energia_restante = energia_atual
    print("❌ Energia Insuficiente!")

# ---------------- PARTE 5 — Relatório Final ----------------
print("\n-------------- Relatório Final da Capital ---------------")    
print(f"- Visitante: {nome}")
print(f"- Resultado Financeiro: R${saldo_final:.2f}")
print(f"- Estoque Final: P:{pocoes} | Pg:{pergaminhos} | E:{elixires}")
print(f"- Última Energia: {energia_restante}")
print("\n✨ Sistema Emergencial Reconstruído com Sucesso ✨")