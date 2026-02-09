import json

ARQUIVO = "produtos.json"


def carregar():
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def gerar_id(produtos):
    if not produtos:
        return 1
    return produtos[-1]["id"] + 1


def criar_produto(nome, preco):
    produtos = carregar()
    produto = {
        "id": gerar_id(produtos),
        "nome": nome,
        "preco": preco
    }
    produtos.append(produto)
    salvar(produtos)


def listar_produtos():
    produtos = carregar()
    for p in produtos:
        print(f'{p["id"]} - {p["nome"]} | R$ {p["preco"]:.2f}')


def atualizar_produto(id_produto, novo_nome, novo_preco):
    produtos = carregar()
    for p in produtos:
        if p["id"] == id_produto:
            p["nome"] = novo_nome
            p["preco"] = novo_preco
            salvar(produtos)
            return
    print("Produto não encontrado.")


def deletar_produto(id_produto):
    produtos = carregar()
    try:
        id_produto = int(id_produto)
    except ValueError:
        print("ID inválido. Digite um número.")
        return
    
    # Remove o produto com o ID especificado
    produtos_atualizados = []
    for p in produtos:
        if p["id"] != id_produto:
            produtos_atualizados.append(p)
    
    salvar(produtos_atualizados)
