from class_pessoa import Pessoa 

class Gerente(Pessoa):

    def __init__(self, nome= None, cpf= None, salario= None, equipe= None, senha= None, idade= None):
        super().__init__(nome, cpf, idade)

        self.__salario = salario 
        self.__equipe = [] if not equipe else equipe 
        self.__senha = "" if not senha else senha

    #Getters 

    @property 
    def salario(self):
        return self.__salario 

    @property 
    def equipe(self):
        return self.__equipe 

    @property 
    def senha(self):
        return self.__senha 

    @salario.setter 
    def salario(self, novo_salario):
        self.__salario = novo_salario 

    @equipe.setter 
    def equipe(self, nova_equipe):
        self.__equipe = novo_equipe 

