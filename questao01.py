estoque = {}

while True:
   
    print("\n===== Gerenciamento de Estoque =====")
    print("1 - Adicionar produto")
    print("2 - Excluir produto")
    print("3 - Atualizar quantidade de um produto")
    print("4 - Exibir todos os produtos")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        estoque[nome] = quantidade
        print(f"Produto '{nome}' adicionado com {quantidade} unidades.")

    elif opcao == "2":
        nome = input("Digite o nome do produto a excluir: ")
        if nome in estoque:
            del estoque[nome]
            print(f"Produto '{nome}' excluido do estoque.")
        else:
            print("Produto não encontrado.")

    elif opcao == "3":
        nome = input("Digite o nome do produto: ")
        if nome in estoque:
            nova_quantidade = int(input("Digite a nova quantidade: "))
            estoque[nome] = nova_quantidade
            print(f"Quantidade do produto '{nome}' atualizada para {nova_quantidade}.")
        else:
            print("Produto não encontrado.")

    elif opcao == "4":
        if estoque:
            print("\n=== Estoque Atual ===")
            for produto, quantidade in estoque.items():
                print(f"{produto}: {quantidade} unidades")
        else:
            print("O estoque está vazio.")

    elif opcao == "5":
        print("Saindo do gerenciamento!")
        break

    else:
        print("Opção inválida! Tente novamente.")