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
from class_item_estoque import ItemEstoque
from faker import Faker
import random

# TipoOperador = type(Operador)

class Estoque:

    def __init__(self, estoque_operadores: Optional[None], estoque_itens: List[None]):
        pass 




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