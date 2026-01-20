from class_pessoa import Pessoa
from typing import List
from class_operador_estoque import OperadorEstoque
import time
import sys

class Gerente(Pessoa):

    """A classe que define a criação dos objetos Gerentes, aqueles que admnistram equipes
    admitindo ou demintindo funcionários."""
    def __init__(self, nome: str= "", idade: int= 0, cpf: str= "", senha: str= "", salario: float=  0.0, equipe: List[OperadorEstoque, Pessoa]= [])-> None:

        super().__init__(nome, idade, cpf, senha, salario)  # Instânciamos um objeto pessoa e depois especializamos. 

        self.__equipe = equipe 


    # Defindo os Getters 
    # O acesso de leitura. 

    @property 
    def equipe(self)-> List[OperadorEstoque, Pessoa]:
        return self.__equipe 

    @equipe.setter 
    def equipe(self, nova_equipe: List[OperadorEstoque, Pessoa])-> None:
        self.__equipe = nova_equipe


    # Métodos dos objetos 

    def mostrar_time(self)-> None:

        for colaborador in self.__equipe:

            print(f"""
ID: {colaborador.id_pessoa}
---------------------------
Nome: {colaborador.nome}   |
---------------------------
Idade: {colaborador.idade} |
---------------------------
CPF: {colaborador.cpf}     |
---------------------------
""")
    def demitir_pessoa(self)-> bool:

        """Este método permite que o gerente demita funcionários, acessa a lista de equipe 
        ou a lista de todos os funcionarios criados. """

        pessoa_nome = input("Indique o nome da pessoa que será demitida: ")
        id_pessoa = input("Indique o id da pessoa que será demitida: ")

        senha = input("Indique a sua senha de acesso: ")

        if self.__senha == senha:

            for colaborador in self.__equipe:

                if colaborador.nome.lower() == pessoa_nome.lower() and colaborador.id_pessoa == id_pessoa: 

                    colaborador.status = False 

                    print("Colaborador Encontrado!")
                    time.sleep(2)

                    print("Demitindo...")
                    time.sleep(2)

                    print("Operação Concluída!")
                    time.sleep(2)

                    return True

                else: 
                    print("Colaborador não encontrado!")
                    time.sleep(2)

                    print("Tente Novamente...")
                    time.sleep(2)

                    return False 

        else: 

            print("Senha inválida!")
            time.sleep(2)

            print("Tente novamente...")
            time.sleep(2)

            return False 

