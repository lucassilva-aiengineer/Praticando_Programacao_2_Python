from class_pessoa import Pessoa 

class Cliente(Pessoa):

    def __init__(self, nome= None, cpf= None, pedido= None, idade= None):
        super().__init__(nome, cpf, idade)

        self.__pedido: list = pedido if pedido else []


    # Defindo o encapsulamento. 
    # Criando formas especiais de acessar os atributos, proteger 
    # o acesso, tanto na leitura quanto na escrita. 

    # Getters
    @property 
    def pedidos(self):
        return self.__pedidos 

    @pedidos.setter 
    def pedidos(self, novos_pedidos):
        self.__pedidos = novos_pedidos

