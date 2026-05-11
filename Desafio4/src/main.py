produtos = []
vendas = []

def cadastrar_produto():
    print("\n--- Cadastro ---")
    try:
        nome = input("Nome do produto: ")
        preco = float(input("Preço: R$ "))
        estoque = int(input("Estoque inicial: "))
        
        novo_produto = {"nome": nome, "preco": preco, "estoque": estoque}
        produtos.append(novo_produto)
        print("Produto cadastrado!")
    except:
        print("Erro: No preço e estoque, use apenas números.")

def realizar_venda():
    print("\n--- Venda ---")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado!")
        return

    try:
        cliente = input("Nome do cliente: ")
        
        posicao = 0
        for p in produtos:
            print(f"{posicao}. {p['nome']} - R$ {p['preco']} (Estoque: {p['estoque']})")
            posicao = posicao + 1

        escolha = int(input("\nDigite o número do produto: "))
        qtd = int(input("Quantidade: "))

        produto_escolhido = produtos[escolha]

        if qtd > produto_escolhido['estoque']:
            print("Erro: Estoque insuficiente.")
        else:
            valor_bruto = produto_escolhido['preco'] * qtd
            
            desconto = 0
            if qtd > 10:
                desconto = valor_bruto * 0.05
            
            valor_final = valor_bruto - desconto
            produto_escolhido['estoque'] = produto_escolhido['estoque'] - qtd

            vendas.append({
                "cliente": cliente,
                "produto": produto_escolhido['nome'],
                "quantidade": qtd,
                "valor_bruto": valor_bruto,
                "desconto": desconto,
                "valor_final": valor_final
            })
            print("Venda realizada!")
    except:
        print("Erro: Digite valores válidos.")

def gerar_relatorio():
    print("\n=== Relatório de Vendas ===")
    total = 0
    for v in vendas:
        print(f"Cliente: {v['cliente']}")
        print(f"Produto: {v['produto']}")
        print(f"Quantidade: {v['quantidade']}")
        print(f"Valor Bruto: R$ {v['valor_bruto']}")
        print(f"Desconto: R$ {v['desconto']}")
        print(f"Valor Final: R$ {v['valor_final']}")
        print("-" * 20)
        total = total + v['valor_final']
        
    print(f"Total Arrecadado: R$ {total}")

# Menu
opcao = "0"
while opcao != "4":
    print("\n1. Cadastrar Produto | 2. Realizar Venda | 3. Gerar Relatório | 4. Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        realizar_venda()
    elif opcao == "3":
        gerar_relatorio()
    elif opcao == "4":
        print("Saindo do sistema...")
    else:
        print("Opção inválida.")