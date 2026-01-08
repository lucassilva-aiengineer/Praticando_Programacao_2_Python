from class_pessoa import Pessoa

class Colaborador(Pessoa):

    def __init__(self, nome= None, cpf= None, cargo= None, salario= None, idade= None):

        # Meio que criamos um objeto pessoas e 
        # especializamos ele 
        super().__init__(nome, cpf, idade) 

        self.__cargo = cargo
        self.__salario = salario


    @property 
    def cargo(self):
        return self.__cargo

    @property 
    def salario(self):
        return self.__salario 

    @cargo.setter 
    def cargo(self, novo_cargo):
        self.__cargo = novo_cargo 

    @salario.setter 
    def salario(self, novo_salario):
        self.__salario = novo_salario 
