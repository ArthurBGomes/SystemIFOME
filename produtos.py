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


def atualizar_produto(id_produto, novo_nome=None, novo_preco=None):
    produtos = carregar()
    
    # Verifica se pelo menos um campo foi fornecido
    if novo_nome is None and novo_preco is None:
        return False, "Nenhum campo para atualizar"
    
    for p in produtos:
        if p["id"] == id_produto:
            if novo_nome is not None and novo_nome.strip() != "":
                p["nome"] = novo_nome
            if novo_preco is not None and novo_preco > 0:
                p["preco"] = novo_preco
            salvar(produtos)
            return True, p
    return False, "Produto não encontrado"


def deletar_produto(id_produto):
    produtos = carregar()
    
    # Remove o produto com o ID especificado
    produtos_atualizados = []
    produto_encontrado = False
    for p in produtos:
        if p["id"] != id_produto:
            produtos_atualizados.append(p)
        else:
            produto_encontrado = True
    
    if produto_encontrado:
        salvar(produtos_atualizados)
        return True, "Produto deletado com sucesso"
    return False, "Produto não encontrado"
