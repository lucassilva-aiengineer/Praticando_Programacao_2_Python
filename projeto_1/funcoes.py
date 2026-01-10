import random 
from class_estoque import Estoque


def gerar_id():

    id_ = ""

    caracteres_gerar = 10
    caracteres_gerados = 0
    while caracteres_gerados < caracteres_gerar:

        numero_a = random.randint(0, 9)

        if not str(numero_a) in id_: 

            id_ += str(numero_a)

            caracteres_gerados += 1


    return id_ 



def calcular_custo_pizza():

    """Esta função calcula o valor de custo das pizzas 
    calculando os valores dos igredientes. """

    pass 


def calcular_valor_estoque(objeto):

    valor_total = 0 

    for item in objeto.__lista_itens 

