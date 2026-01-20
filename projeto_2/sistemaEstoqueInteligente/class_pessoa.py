# Class pessoa 

from typing import List

class Pessoa:

    """ A classe que define o objeto pessoa, a super classe ou classe mãe das 
    classes OperadorEstoque e Gerente"""

    objetos_pessoa_criados: List[Pessoa] = []   # Lista com todos os obetos criados 
    ids_gerados: List[str] = []                 # Lista com todos os ids criados 
    pessoas_criadas = 0                         # Quantidade com todas as pessoas criadas

    def __init__(self, nome: str= "", idade: int= 0, cpf: str= "", senha: str= "", salario: float= 0.0):

        self.__id_pessoa = modulo_funcoes.gerar_id()
        self.__nome = nome 
        self.__idade = idade 
        self.__cpf = cpf 
        self.__senha = senha 
        self.__salario = salario 
        self.__status = True

        Pessoa.objetos_pessoa_criados.append(self)
        Pessoa.ids_gerados.append(self.__id_pessoa)
        # Pessoa.pessoas_criadas = Pessoa.pessoas_criadas + 1 

        Pessoa.pessoas_criadas += 1



    # Defindo os getters 
    # As regras e a lógica de leitura, defindo de que maneira os atributos 
    # desta classe poderão ser lidos. 

    @property 
    def id_pessoa(self)-> str:
        return self.__id_pessoa 

    @property 
    def nome(self)-> str: 
        return self.__nome 

    @property 
    def idade(self)-> int:
        return self.__idade

    @property 
    def cpf(self)-> str:

        # cpf_formatado = [cpf[indice] for letra in range(len(self.__cpf)) if ]
        cpf_formatado_lista = [tupla[1] if tupla[0] < 2 else "*" for tupla in enumerate(self.__cpf)]

        cpf_formatado = ""

        for caracter in cpf_formatado_lista: 
            cpf_formatado += caracter 

        return cpf_formatado 

    @property 
    def senha(self)-> str :
        return self.__senha 

    @property 
    def salario(self)-> float: 
        return self.__salario 

    @property 
    def status(self)-> bool: 
        return self.__status

    # Defindo os setters 
    # A maneira pela qual os atributos poderam ser escritos. 
    # Os atributos podem ser alterados, porém da forma que eu definir. 

    @id_pessoa.setter
    def id_pessoa(self, id_: str)-> None:
        self.__id_pessoa

    @nome.setter
    def nome(self, novo_nome: str)-> None: #Poderiamos adotar algumas restrições porém as limitaremos. 
        self.__nome = novo_nome 

    @idade.setter 
    def idade(self, nova_idade: int)-> None: 
        self.__idade = nova_idade 

    @cpf.setter 
    def cpf(self, novo_cpf: str)-> None: 
        self.__cpf = novo_cpf

    @senha.setter 
    def senha(self, nova_senha: str)-> None:
        self.__senha = nova_senha

    @salario.setter
    def salario(self, novo_salario: float)-> None:
        self.__salario = novo_salario 


    @status.setter 
    def status(self, novo_status: bool)-> None: 
        self.__status = novo_status

