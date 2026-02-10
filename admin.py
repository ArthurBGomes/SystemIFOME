import clientes
import produtos
import entregas


def menu():
    print("\n=== GERENCIADOR DE ENTREGAS ===")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Atualizar clientes")
    print("4 - Deletar clientes")
    print("5 - Cadastrar produto")
    print("6 - Listar produtos")
    print("7 - Atualizar produtos")
    print("8 - Deletar produtos")
    print("9 - Criar entrega")
    print("10 - Listar entregas")
    print("11 - Atualizar status da entrega")
    print("12 - Deletar entrega")
    print("0 - Sair")


while True:
    menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do cliente: ")
        endereco = input("Endereço: ")
        clientes.criar_cliente(nome, endereco )

    elif opcao == "2":
        clientes.listar_clientes()

    elif opcao == "3":
        clientes.listar_clientes()
        try:
            id_cliente = int(input("Digite o ID do cliente que você quer atualizar: "))
            nome = input("Novo nome (ENTER para manter): ").strip()
            endereco = input("Novo endereço (ENTER para manter): ").strip()
            nome = nome if nome else None
            endereco = endereco if endereco else None

            sucesso, resultado = clientes.atualizar_cliente(id_cliente, nome, endereco)
            if sucesso:
                print(f"Cliente atualizado com sucesso!")
            else:
                print(f"Erro: {resultado}")
        except ValueError:
            print("ID inválido. Digite um número.")

    elif opcao == "4":
        try:
            id_cliente = int(input("Digite o ID do cliente que você quer deletar: "))
            sucesso, mensagem = clientes.deletar_cliente(id_cliente)
            print(mensagem)
        except ValueError:
            print("ID inválido. Digite um número.")

    elif opcao == "5":
        nome = input("Nome do produto: ")
        try:
            preco = float(input("Preço: "))
            produtos.criar_produto(nome, preco)
        except ValueError:
            print("Preço inválido. Digite um número.")

    elif opcao == "6":
        produtos.listar_produtos()

    elif opcao == "7":
        produtos.listar_produtos()
        try:
            id_produto = int(input("ID do produto que você quer atualizar: "))
            novo_nome = input("Novo nome (ENTER para manter): ").strip()
            novo_preco = input("Novo preço (ENTER para manter): ").strip()
            novo_nome = novo_nome if novo_nome else None
            novo_preco = float(novo_preco) if novo_preco else None
            
            sucesso, resultado = produtos.atualizar_produto(id_produto, novo_nome, novo_preco)
            if sucesso:
                print(f"Produto atualizado com sucesso!")
            else:
                print(f"Erro: {resultado}")
        except ValueError:
            print("ID ou preço inválido. Digite um número.")

    elif opcao == "8":
        try:
            id_produto = int(input("ID do produto: "))
            sucesso, mensagem = produtos.deletar_produto(id_produto)
            print(mensagem)
        except ValueError:
            print("ID inválido. Digite um número.")

    elif opcao == "9":
        clientes.listar_clientes()
        try:
            id_cliente = int(input("ID do cliente: "))
        except ValueError:
            print("ID inválido. Digite um número.")
            continue

        nome_entrega = input("Nome da entrega (opcional): ")
        localizacao = input("Localização/Endereço de entrega: ")
        observacao = input("Observação (opcional): ")
        
        lista_produtos = []
        while True:
            produtos.listar_produtos()
            try:
                id_produto = int(input("ID do produto (0 para sair): "))
            except ValueError:
                print("ID inválido. Digite um número.")
                continue
            if id_produto == 0:
                break
            try:
                qtd = int(input("Quantidade: "))
            except ValueError:
                print("Quantidade inválida. Digite um número.")
                continue
            lista_produtos.append({
                "id_produto": id_produto,
                "quantidade": qtd
            })

        if lista_produtos:
            entregas.criar_entrega(id_cliente, nome_entrega, localizacao, lista_produtos, observacao)
            print(f"Entrega criada com sucesso!")
        else:
            print("Nenhum produto adicionado.")

    elif opcao == "10":
        entregas.listar_entregas()

    elif opcao == "11":
        try:
            id_entrega = int(input("ID da entrega: "))
            print("Status: Pendente | Em preparo | Em rota | Entregue")
            status = input("Novo status: ")
            sucesso, mensagem = entregas.atualizar_status(id_entrega, status)
            print(mensagem)
        except ValueError:
            print("ID inválido. Digite um número.")

    elif opcao == "12":
        try:
            id_entrega = int(input("ID da entrega: "))
            sucesso, mensagem = entregas.deletar_entrega(id_entrega)
            print(mensagem)
        except ValueError:
            print("ID inválido. Digite um número.")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
