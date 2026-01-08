import funcoes 

class Pessoa: 

    def __init__(self, nome= None, cpf= None, idade= None):

        self.__id_ = funcoes.gerar_id()
        self.__idade = idade
        self.__nome = nome if nome else ""
        self.__cpf = cpf if cpf else "" 


    @property 
    def id_(self):
        return self.__id_ 

    @property 
    def nome(self):
        return self.__nome

    @property 
    def cpf(self):
        return self.__cpf  



    @id_.setter 
    def id_(self, novo_id):
        self.__id_ = novo_id 

    @nome.setter 
    def nome(self, novo_nome):
        self.__nome = novo_nome 

    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf 


    