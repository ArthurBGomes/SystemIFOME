import json

ARQUIVO = "entregas.json"


def carregar():
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def gerar_id(entregas):
    if not entregas:
        return 1
    return entregas[-1]["id"] + 1


def criar_entrega(nome, localizacao, produtos):
    """
    produtos = lista de dicionários:
    [
        {"id_produto": 1, "quantidade": 2},
        {"id_produto": 3, "quantidade": 1}
    ]
    """
    entregas = carregar()

    entrega = {
        "id": gerar_id(entregas),
        "nome": nome,
        "localizacao": localizacao,
        "produtos": produtos,
        "status": "Pendente"
    }

    entregas.append(entrega)
    salvar(entregas)


def listar_entregas():
    entregas = carregar()
    for e in entregas:
        print(f"\nEntrega #{e['id']}")
        print(f"Cliente ID: {e['id_cliente']}")
        print(f"Status: {e['status']}")
        print("Produtos:")
        for p in e["produtos"]:
            print(f"  Produto {p['id_produto']} | Qtd: {p['quantidade']}")


def atualizar_status(id_entrega, novo_status):
    entregas = carregar()
    for e in entregas:
        if e["id"] == id_entrega:
            e["status"] = novo_status
            salvar(entregas)
            return
    print("Entrega não encontrada.")


def deletar_entrega(id_entrega):
    entregas = carregar()
    entregas = [e for e in entregas if e["id"] != id_entrega]
    salvar(entregas)


def visualizar_status(id_entrega):
    entregas = carregar()
    for e in entregas:
        if e["id"] == id_entrega:
            print(f"\nEntrega #{e['id']}")
            print(f"Nome: {e['nome']}")
            print(f"Localização: {e['localizacao']}")
            print(f"Status: {e['status']}")
            print("Produtos:")
            for p in e["produtos"]:
                print(f"  Produto {p['id_produto']} | Qtd: {p['quantidade']}")
            return
    print("Entrega não encontrada.")
