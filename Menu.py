# Cadastro do produto farinha com nome, quantidade e preço
farinha = {
    'nome': 'Farinha',
    'quantidade': 10,
    'preço': 4.99
}

# Cadastro do produto ovo
ovo = {
    'nome': 'Ovo',
    'quantidade': 12,
    'preço': 29.99
}

# Cadastro do produto leite
leite = {
    'nome': 'Leite',
    'quantidade': 7,
    'preço': 12.99
}

# Cria um loop infinito para manter o menu funcionando
while True:

    # Exibe o menu principal do sistema
    print("\n=== SISTEMA DE ESTOQUE ===")
    print("1 - Visualizar Estoque Atual")
    print("2 - Registrar Entrada de Produto")
    print("3 - Registrar Saída de Produto")
    print("4 - Sair do Sistema")

    # Solicita que o usuário escolha uma opção
    opcao = int(input("Escolha uma opção: "))

    # Opção 1 - Mostrar estoque atual
    if opcao == 1:

        # Exibe todos os produtos cadastrados
        print("====Estoque Atual====")
        print(farinha)
        print(ovo)
        print(leite)

    # Opção 2 - Registrar entrada de produtos
    elif opcao == 2:

        # Solicita o nome do produto
        produto = input("Digite o nome do produto: ")

        # Solicita a quantidade que será adicionada
        quantidade = int(input("Digite a quantidade: "))

        # Verifica se o produto é farinha
        if produto == "farinha":

            # Adiciona a quantidade ao estoque
            farinha["quantidade"] += quantidade

            # Exibe a nova quantidade atualizada
            print(f"Entrada registrada. Nova quantidade de {farinha['nome']}: {farinha['quantidade']}")

        # Verifica se o produto é ovo
        elif produto == "ovo":

            # Atualiza o estoque do ovo
            ovo["quantidade"] += quantidade

            # Mostra a quantidade atualizada
            print(f"Entrada registrada. Nova quantidade de {ovo['nome']}: {ovo['quantidade']}")

        # Verifica se o produto é leite
        elif produto == "leite":

            # Atualiza o estoque do leite
            leite["quantidade"] += quantidade

            # Exibe a nova quantidade
            print(f"Entrada registrada. Nova quantidade de {leite['nome']}: {leite['quantidade']}")

        # Caso o produto não exista
        else:
            print("Produto não encontrado no estoque.")

    # Opção 3 - Registrar saída de produtos
    elif opcao == 3:

        # Solicita o nome do produto
        produto = input("Digite o nome do produto: ")

        # Solicita a quantidade desejada
        quantidade = int(input("Digite a quantidade: "))

        # Verifica se o produto escolhido é farinha
        if produto == 'farinha':

            # Confere se existe estoque suficiente
            if farinha["quantidade"] >= quantidade:

                # Remove a quantidade do estoque
                farinha["quantidade"] -= quantidade

                # Exibe mensagem de sucesso
                print("Sucesso, encomendado.")

            # Caso não tenha estoque suficiente
            else:
                print("Sem estoque.")

        # Verifica se o produto é ovo
        elif produto == 'ovo':

            # Confere se existe quantidade suficiente
            if ovo["quantidade"] >= quantidade:

                # Remove a quantidade do estoque
                ovo["quantidade"] -= quantidade

                # Exibe mensagem de sucesso
                print("Sucesso, encomendado.")

            # Caso não tenha estoque suficiente
            else:
                print("Sem estoque.")

        # Verifica se o produto é leite
        elif produto == 'leite':

            # Verifica se há estoque suficiente
            if leite["quantidade"] >= quantidade:

                # Remove a quantidade do estoque
                leite["quantidade"] -= quantidade

                # Mensagem de sucesso
                print("Sucesso, encomendado.")

            # Caso não tenha estoque suficiente
            else:
                print("Sem estoque.")

    # Opção 4 - Encerrar o sistema
    elif opcao == 4:

        # Exibe mensagem de despedida
        print("Encerrando sistema...")

        # Interrompe o loop while True
        break

    # Caso o usuário digite uma opção inválida
    else:

        # Exibe mensagem de erro
        print("Opção inválida.")