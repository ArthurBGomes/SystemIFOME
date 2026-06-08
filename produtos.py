import json
from abc import staticmethod

ARQUIVO = "produtos.json"

class Produto:
    def __init__(self, id: int, nome: str, preco: float):
        self.id = id
        self.nome = nome
        self.preco = preco

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco
    
    @nome.setter
    def nome(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("Nome não pode ser vazio")
        self.__nome = valor.strip()

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise ValueError("O preço do produto deve ser maior que 0")
        self.__preco = valor

    def to_dict(self):
        return {"id": self.__id, "nome": self.__nome, "preco": self.__preco}

    def exibir_detalhes(self):
        return f"{self.__id} - {self.__nome} | R$ {self.__preco:.2f}"
    
    @staticmethod
    def from_dict(dados: dict):
        return Produto(dados['id'], dados['nome'], dados['preco'])
    
    def __repr__(self):
        return f"Produto({self.__id}, '{self.__id}', {self.__preco})"

class RepositorioProduto:
    def __init__(self, arquivo=ARQUIVO):
        self.__arquivo = arquivo

    def carregar():
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                dados = json.load(f)
                return [Produto.from_dict(d) for d in dados]
        except FileNotFoundError:
            return []

    def salvar(self, produtos: list[Produto]):
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in produtos], f, indent=4, ensure_ascii=False)

class GerenciarProdutos:
    def __init__(self):
        self.__repositorio = RepositorioProduto()

    def __gerar_id(self, produtos: list[Produto]):
        if not produtos:
            return 1
        return max(p.id for p in produtos) + 1


    def criar_produto(self, nome: str, preco: float) -> Produto:
        produtos = self.__repositorio.carregar()
        novo = Produto(self.__gerar_id(produtos), nome, preco)
        produtos.append(novo)
        self.__repositorio.salvar(produtos)
        return novo


    def listar(self) -> list[Produto]:
        return self.__repositorio.carregar()
    
    def buscar_por_id(self, id_produto: int) -> Produto | None:
        for p in self.__repositorio.carregar():
            if p.id == id_produto:
                return p
        return None

    def atualizar(self, id_produto: int, novo_nome=None, novo_preco=None):
        if novo_nome is None and novo_preco is None:
            return ValueError("Nenhum campo para atualizar")
        
        produtos = self.__repositorio.carregar()
        for p in produtos:
            if p.id == id_produto:
                if novo_nome is not None:
                    p.nome = novo_nome
                if novo_preco is not None:
                    p.preco = novo_preco
                self.__repositorio.salvar(produtos)
                return p
        raise ValueError(f"Produto com id {id_produto} não encontrado")

def deletar(self, id_produto: int):
        produtos = self.__repositorio.carregar()
        novos = [p for p in produtos if p.id != id_produto]
        if len(novos) == len(produtos):
            raise ValueError(f"Produto com id {id_produto} não encontrado")
        self.__repositorio.salvar(novos)