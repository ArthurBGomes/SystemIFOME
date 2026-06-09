import json

ARQUIVO = "clientes.json"


def carregar():
    with open(ARQUIVO, "r", encoding="utf-8") as f: #Abre o arquivo e armazena em f
        return json.load(f) #Ele carrega os dados armazenados em f


def salvar(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f: #Abre o arquivo e armazena em f
        json.dump(dados, f, indent=4, ensure_ascii=False) #Ele salva o obj. dados em f, com uma identação com 4 espaços


def gerar_id(clientes):
    if not clientes: #Verifica se há clientes na lista
        return 1 #Caso não houver, retorna 1
    return clientes[-1]["id"] + 1 #Caso contrário, retorna o último ID + 1


def criar_cliente(nome, endereco):
    clientes = carregar() #carrega o arquivo
    cliente = { #Gera o dicionário com as informações
        "id": gerar_id(clientes), # Gera o id
        "nome": nome, # Pede o nome
        "endereco": endereco # Pede o endereço
    }
    clientes.append(cliente) # Adiciona cliente a clientes
    salvar(clientes) # Salva os dados


def listar_clientes():
    clientes = carregar() # Carrega o arquivo
    for c in clientes: # Adiciona cada elemento de clientes em c
        print(f'{c["id"]} - {c["nome"]} | {c["endereco"]}') # Printa cada elemento


def atualizar_cliente(id_cliente, novo_nome=None, novo_endereco=None):
    clientes = carregar()

    for cliente in clientes:
        if cliente["id"] == id_cliente:
            # Verifica se pelo menos um campo foi fornecido
            if novo_nome is None and novo_endereco is None:
                return False, "Nenhum campo para atualizar"

            if novo_nome is not None and novo_nome.strip() != "":
                cliente["nome"] = novo_nome

            if novo_endereco is not None and novo_endereco.strip() != "":
                cliente["endereco"] = novo_endereco

            salvar(clientes)
            return True, cliente

    return False, "Cliente não encontrado"



def deletar_cliente(id_cliente):
    clientes = carregar()
    
    # Remove o cliente com o ID especificado
    clientes_atualizados = []
    cliente_encontrado = False
    for c in clientes:
        if c["id"] != id_cliente:
            clientes_atualizados.append(c)
        else:
            cliente_encontrado = True
    
    if cliente_encontrado:
        salvar(clientes_atualizados)
        return True, "Cliente deletado com sucesso"
    return False, "Cliente não encontrado"
