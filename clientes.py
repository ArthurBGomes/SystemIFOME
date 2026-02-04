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


def atualizar_cliente(id_cliente, novo_nome, novo_endereco):
    clientes = carregar() # Carrega o arquivo
    for c in clientes: # Armazena cada elemento de clientes em c
        if c["id"] == id_cliente: # Certifica o id
            c["nome"] = novo_nome # Muda o nome
            c["endereco"] = novo_endereco # Muda o endereço
            salvar(clientes) # Salva a modificação feita
            return # Retorna nada
    print("Cliente não encontrado.") # Caso o for não seja satisfeito


def deletar_cliente(id_cliente):
    clientes = carregar()
    clientes = [c for c in clientes if c["id"] != id_cliente]
    salvar(clientes)
