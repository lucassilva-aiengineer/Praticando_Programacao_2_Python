# from __future__ import annotations
# Classe Estoque 

# try: 

#     from class_operador import Operador 

# except ModuleNotFoundError as message:
#     print(message)


from typing import Optional # Utilizando Optional para indicarmos o tipo 
                            # que de dados que os nossos argumentos irão receber 
                            # no caso o parâmetro estoque_operadores que recebe ou um tipo operador ou 
                            # None. 

from typing import List 
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from class_item_estoque import ItemEstoque
    from modulo_funcoes import funcoes
from faker import Faker
import random

# TipoOperador = type(Operador)

class Estoque:

    def __init__(self, estoque_operadores: Optional[None], estoque_itens: List[ItemEstoque]= []):

        self.__id_ = funcoes.gerar_id()
        self.__estoque_itens = estoque_itens
        self.__itens_vencidos = [item for item in self.__estoque_itens if item.vencimento == True]
        self.__itens_validos = [item for item in self.__estoque_itens if item.vencimento == False]
        self.__itens_vencimento_proximo = [item for item in self.__estoque_itens if item.vencimento_proximo == True]
        self.__itens_em_falta = [item for item in self.__estoque_itens if item.quantidade <= 0]
# TipoItemEstoque = type(ItemEstoque)

# Nomes de classes já são tipos válidos 
# def imprimir_item(lista_itens: List[ItemEstoque])-> None:

#     print(lista_itens[0: 2].nome)



# objetos_itens: List[ItemEstoque] = []


# for _ in range(0, 10):

#     nome = random.choice()
#     item = ItemEstoque(nome, validade, descricao, valor, fornecedores, vencimento)
#     objetos_itens.append(item) 

#