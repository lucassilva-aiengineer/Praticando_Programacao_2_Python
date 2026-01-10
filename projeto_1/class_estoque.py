import funcoes as fnc 

class Estoque:
    """Esta classe modela o objeto Estoque """

    def __init__(self, lista_itens= None):
        self.__lista_itens = [] if lista_itens == None else lista_itens 
        
        """Este atributo é um list compression dos itens da lista de itens que possuem uma data de validade inferior a da consulta. """
        self.__itens_vencidos: list = [item for item in self.__lista_itens if itens]
        self.__itens_faltando: list = []
        self.__valor_itens_com_validade: list = []
        self.__valor_vencidos: list = []
        self.__total_estoque: list = [] 


    