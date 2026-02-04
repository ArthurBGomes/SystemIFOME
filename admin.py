import clientes
import produtos
import entregas


def menu():
    print("\n=== GERENCIADOR DE ENTREGAS ===")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Cadastrar produto")
    print("4 - Listar produtos")
    print("5 - Deletar produtos")
    print("6 - Criar entrega")
    print("7 - Listar entregas")
    print("8 - Atualizar status da entrega")
    print("9 - Deletar entrega")
    print("0 - Sair")


while True:
    menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do cliente: ")
        endereco = input("Endereço: ")
        clientes.criar_cliente(nome, endereco)

    elif opcao == "2":
        clientes.listar_clientes()

    elif opcao == "3":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        produtos.criar_produto(nome, preco)

    elif opcao == "4":
        produtos.listar_produtos()

    elif opcao ==  "5":
        id_produto = input("ID do produto: ")
        produtos.deletar_produto(id_produto)

    elif opcao == "6":
        clientes.listar_clientes()
        id_cliente = int(input("ID do cliente: "))

        lista_produtos = []
        while True:
            produtos.listar_produtos()
            id_produto = int(input("ID do produto (0 para sair): "))
            if id_produto == 0:
                break
            qtd = int(input("Quantidade: "))
            lista_produtos.append({
                "id_produto": id_produto,
                "quantidade": qtd
            })

        entregas.criar_entrega(id_cliente, lista_produtos)

    elif opcao == "7":
        entregas.listar_entregas()

    elif opcao == "8":
        id_entrega = int(input("ID da entrega: "))
        print("Status: Pendente | Em preparo | Em rota | Entregue")
        status = input("Novo status: ")
        entregas.atualizar_status(id_entrega, status)

    elif opcao == "9":
        id_entrega = int(input("ID da entrega: "))
        entregas.deletar_entrega(id_entrega)

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
