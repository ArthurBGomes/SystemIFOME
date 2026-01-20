import json

ARQUIVO = "clientes.json"


def carregar():
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def gerar_id(clientes):
    if not clientes: #Verifica se há clientes na lista
        return 1 #Caso não houver, retorna 1
    return clientes[-1]["id"] + 1 #Caso contrário, retorna o último ID + 1


def criar_cliente(nome, endereco):
    clientes = carregar()
    cliente = {
        "id": gerar_id(clientes),
        "nome": nome,
        "endereco": endereco
    }
    clientes.append(cliente)
    salvar(clientes)


def listar_clientes():
    clientes = carregar()
    for c in clientes:
        print(f'{c["id"]} - {c["nome"]} | {c["endereco"]}')


def atualizar_cliente(id_cliente, novo_nome, novo_endereco):
    clientes = carregar()
    for c in clientes:
        if c["id"] == id_cliente:
            c["nome"] = novo_nome
            c["endereco"] = novo_endereco
            salvar(clientes)
            return
    print("Cliente não encontrado.")


def deletar_cliente(id_cliente):
    clientes = carregar()
    clientes = [c for c in clientes if c["id"] != id_cliente]
    salvar(clientes)
