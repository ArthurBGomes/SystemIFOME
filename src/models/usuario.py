from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email
    
    @nome.setter
    def nome(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("O nome não pode estar vazio")
        self.__nome = valor.strip()

    @email.setter
    def email(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("O email não pode estar vazio")
        if not '@' in valor:
            raise ValueError("Preencha seu email com '@'")
        self.__email = valor

    @abstractmethod
    def exibir_detalhes(self):
        pass

class Cliente(Pessoa):
    def __init__(self, nome, email, senha, endereco):
        super().__init__(nome, email, senha)
        self.__endereco = endereco

    @property
    def endereco(self):
        return self.__endereco
    
    def exibir_detalhes(self):
        return f"Cliente: {self.nome} | {self.__endereco}"
    
class Entregador(Pessoa):
    def __init__(self, nome, email, senha, veiculo):
        super().__init__(nome, email, senha)
        self.__veiculo = veiculo

    @property
    def veiculo(self):
        return self.__veiculo
    
    def exibir_detalhes(self):
        return f"Entregador: {self.nome} | {self.__veiculo}"
    
class RepositorioUsuario:
    pass