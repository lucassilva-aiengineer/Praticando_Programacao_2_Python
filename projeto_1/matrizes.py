# Praticando listas 

import random 

""" Neste arquivo trabalhamos a prática de progrmação com listas """


def teste_listas_a():

    lista_a =   [   [], [], [], 
                    [], [], [],
                    [], [], []
                ]


    for lista in lista_a: 

        for numero in range(0, 10):

            numeros = random.randint(0, 9)
            lista.append(numeros)


    numeros_adicionados = []

    for lista in lista_a:

        for numero in lista:

            numeros_adicionados.append(numero)

            # print(numero) 


    quantidade_numeros = len(numeros_adicionados)
    print(quantidade_numeros)
    # print(numeros_adicionados)


def teste_listas_2():

    lista_a =   [   [[], [], []], 
                    [[], [], []], 
                    [[], [], []]
                ]


    # Acessando cada lista interna e adicionando 10 números. 

    for lista_2 in lista_a:
        for lista_3 in lista_2: 

            for numero in range(0, 10):

                numero_a = random.randint(0, 100)

                lista_3.append(numero_a)

    return lista_a

def testando_matriz():
    matriz = teste_listas_2()

    for linha in matriz: 
        for coluna in linha: 

            for numero in coluna:
                print(numero)

# print(matriz)


def construir_matriz_a():

    matriz = [  [],         # Matriz 4 x 3
                [],         # Uma matriz que possui quatro linhas e três colunas. 
                [],
                []]


    for linha in matriz: 

        for numero in range(0, 3):

            numero_a = random.randint(0, 9)
            linha.append(numero_a)


    return matriz 


matriz_a = construir_matriz_a()
print(matriz_a)

# for linha in matriz_a:
#     for numero in linha: 

#         print(numero)