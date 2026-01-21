from class_pessoa import Pessoa
from typing import List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from class_operador_estoque import OperadorEstoque 

import time
import sys
from faker import Faker
import random  




class Gerente(Pessoa):

    """A classe que define a criação dos objetos Gerentes, aqueles que admnistram equipes
    admitindo ou demintindo funcionários."""
    def __init__(self, nome: str= "", idade: int= 0, cpf: str= "", senha: str= "", salario: float=  0.0, equipe: list[OperadorEstoque | Pessoa] = [])-> None:

        super().__init__(nome, idade, cpf, senha, salario)  # Instânciamos um objeto pessoa e depois especializamos. 

        self.__equipe = equipe 

        for colaborador in self.__equipe:      # Alterando 
            colaborador.lider = self


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


# Testando a classe Gerente 

def teste_1()-> None:

    faker = Faker('pt_BR')

    objetos_pessoa = [OperadorEstoque(faker.name_male(),
                                        random.randint(20, 70), 
                                        faker.cpf(),
                                        senha= 'abcd',
                                        salario= random.unform(20000, 30000), 
                                        # lider= "Gerente A"
                                        ) for numero in range(5)]


    gerente_1 = Gerente("Marcos", 22, "00000-0000", "1234", 30000, objetos_pessoa)

    