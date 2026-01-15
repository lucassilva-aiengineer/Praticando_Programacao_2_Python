# Revisão Funções 

# Parâmetros vs argumentos 


# No interior da definição função chamamos esta variável com dados 
# que utilizamos no interior da função, podendo alterálos de parâmetros.

def funcao_saudacao(nome):

    return "Hello " + nome + "!"


# Quando chamamos a função, chamamos aqui os dados passados a função e utilizados 
# na mesma de argumentos. 

# print(funcao_saudacao("Mateus"))

# saudacao = funcao_saudacao(input("Indique o seu nome: "))
# print(saudacao)



# Argumentos Posicionais. 

def imprimir_nomes(nome_a, nome_b, nome_c):

    # Podemos utilizar os nossos parâmetros, as nossas 
    # entradas da forma que desejarmos na definição da nossa função.


    print(f"O terceiro nome passado: {nome_c}")
    print("O primeiro nome passado: " + " " + nome_a)
    print("O segundo nome passado: ",nome_b)



# imprimir_nomes("Mateus", "Marcos", "João")


def multiplicacao(parcela_a, parcela_b, parcela_c):

    resultado = parcela_a * parcela_b * parcela_c 

    print(f"A multiplicação {parcela_a} x {parcela_b} x {parcela_c} =", resultado) 

    lista_argumentos = [parcela_a, parcela_b, parcela_c]

    print("lista 3:", lista_argumentos)

    lista_argumentos_a = list()

    lista_argumentos_a.append(parcela_a)
    lista_argumentos_a.append(parcela_b)
    lista_argumentos_a.append(parcela_c)

    print("lista 2:", lista_argumentos_a)




# multiplicacao(10, 20, 30) 

# multiplicacao(10, 20, 30)



# Args 

# Com args nós podemos compactar 
# uma quantidade indeterminada de argumentos posicionais 
# em uma tupla atribuida a uma variável 


def adicao(*args):

    print("Args: ", args)

    print("\nIterando os nossos args: ")

    for valor in args:
        print(valor)


    soma = sum(args)

    # args.append(2) 

    print("Soma:", soma)

    return soma 

# Funciona como esperávamos. 

assert adicao(10, 20, 30, 40) == 100, "Deveria retornar o número 100"



# **Kwargs 
# Nós utilizamos os **Kawargs para podermos atribuir uma quantidade indeterminada
# de argumentos de palavra chave ao argumento de uma função, estes argumentos são 
# compactados em um dicionário, as chaves dos argumentos são as chaves dos dicionários 
# e os argumentos os valores atribuidos ao dicionário. 

def imprir_usuario(**kwargs):    

    print(type(kwargs) == dict)
    print(type(kwargs))

    print(kwargs)

    for chave in kwargs:

        print("Chave: " + chave)
        print("Valor:", kwargs[chave]) 


    for chave, valor in kwargs.items():

        print(f"""Chave: {chave} 
Valor: {valor}""")

imprir_usuario(nome= "Mateus", idade= 20, cidade= "Goiânia") 


# Objetivo, um sistema de estoque que utilize mais, funções lambda, 
# lists compression, funções especiais, map, filter, reduce, *args e **kwargs.

 