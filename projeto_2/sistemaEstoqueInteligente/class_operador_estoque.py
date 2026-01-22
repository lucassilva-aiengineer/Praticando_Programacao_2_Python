# Classe Operador Estoque. 
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from class_pessoa import Pessoa 
    from class_gerente import Gerente 

from typing import Union # Bíblioteca para as anotações de tipo. 

class OperadorEstoque(Pessoa):

    # Uma possível situação eu preciso das anotações de tipo nos argumentos da classe filha 
    def __init__(self, nome: str, idade: int, cpf: str, senha: str, salario: float,  lider: str= ""): # lider pode assumir um destes tipos de dados: Gerente, Pessoa ou float. 

        # Lembre-se atributos privados métodos públicos. 
        super().__init__(nome, idade, cpf, senha, salario)  # Eu crio um objeto pessoa
        self.__lider = lider                                    # E especializo o objeto filho. 


    # Definindo os getters e setters 

    # Getters 
    @property 
    def lider(self)-> str: # retornando ou um objeto Gerente ou um str 
        return self.__lider 

    @lider.setter 
    def lider(self, novo_lider: str)-> None:
        self.__novo_lider = novo_lider