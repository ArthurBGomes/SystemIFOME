import clientes
import produtos
import entregas


def menu():
    print("\n=== GERENCIADOR DE ENTREGAS ===")
    print("1 - Listar produtos")
    print("2 - Fazer pedido")
    print("3 - Visualizar status do pedido")
    print("4 - Deletar pedido")
    print("0 - Sair")


while True:
    menu()
    opcao = input("Escolha: ")
    
    if opcao == "1":
        produtos.listar_produtos()

    elif opcao == "2":
        nome = input("Insira seu Nome: ")
        localizacao = input("Insira o endereço de entrega: ")
        lista_produtos = []
        produtos.listar_produtos()
        while True:
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
            entregas.criar_entrega(nome, localizacao, lista_produtos)
        else:
            print("Nenhum produto adicionado.")
        print("Id do pedido: ", entregas.gerar_id(entregas.carregar()) - 1)

    elif opcao == "3":
        id_entrega = int(input("ID da entrega: "))
        entregas.visualizar_status(id_entrega)
    
    elif opcao == "4":
        id_entrega = int(input("ID da entrega: "))
        entregas.deletar_entrega(id_entrega)

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
