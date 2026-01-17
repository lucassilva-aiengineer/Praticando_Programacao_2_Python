# Classe item estoque 

from typing import Union, List

class ItemEstoque: # PascalCase, todas as palavras com letras maiúsculas.

    """ A classe Item estoque é voltado a definição dos objetos
        que serão armazenados no estoque. """


    def __init__(self, nome: str= "", validade: Union[str]= "", descricao: str= "", valor: float= 0.0, \
    fornecedores: List[str]= [], vencimento: bool= False)-> None:


        self.__nome = nome
        self.__validade = validade # Se validade for igual a um valor
        self.__descricao = descricao 
        self.__valor = valor 
        self.__fornecedores = fornecedores 
        self.__vencimento = vencimento  


    # Os nossos getters 

    @property 
    def nome(self)-> str:
        return self.__nome

    @property
    def validade(self)-> str:
        return self.__validade 

    @property 
    def descricao(self)-> str:
        return self.__descricao 

    @property 
    def valor(self)-> float:
        return self.__valor 

    @property 
    def fornecedores(self)-> List[str]:
        return self.__fornecedores 

    @property 
    def vencimento(self)-> bool:
        return self.__vencimento 



    # Os nossos setters 
    # Que nos permitem o acesso a escrita os métodos de escrita.
    
    @nome.setter 
    def nome(self, novo_nome: str)-> None: 
        self.__nome =  novo_nome

    @validade.setter 
    def validade(self, nova_validade: str)-> None:
        self.__validade = nova_validade 

    @descricao.setter 
    def descricao(self, nova_descricao: str)-> None:
        self.__descricao = nova_descricao

    @valor.setter 
    def valor(self, novo_valor: float)-> None:
        self.__valor = novo_valor 

    @fornecedores.setter 
    def fornecedores(self, lista_fornecedores: List[str])-> None:
        self.__fornecedores 

    @vencimento.setter 
    def vencimento(self, novo_vencimento: str)-> None:
        self.__vencimento 



