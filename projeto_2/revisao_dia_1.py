# Funções Lambda 

# Funções lambda são funções anônimas formadas apenas por palavra chave + expressão 

# Exemplo: 

# lambda argumento : expressao 

funcao_lambda = lambda argumento_a : argumento_a * 2

# print(funcao_lambda(10)) 


# Lists Compression

def exemplo():
    numeros = [funcao_lambda(numero) for numero in range(0, 10)]

    for numero in numeros: 
        print(numero) 



# As funções lambda podem ter mais de um argumento. 

def exemplo_2():

    funcao_lambda_soma = lambda numero_a, numero_b : numero_a + numero_b 

    tuplas_valores = [(1, 5), (10, 8), (20, 3)]
    numeros = [funcao_lambda_soma(tupla[0], tupla[1]) for tupla in tuplas_valores]

    print(numeros)

# As funções lamdas são excelentes quando utilizadas como argumentos de 
# outras funções. 


# geradores = (numero for numero in range(10))

# for gerador in geradores:


tuplas = [(10, 5), (20, 30), (10, 3)]

# Ordenando tuplas por meio de um critério específico, ordenando apartir de 
# um índice. 

tuplas_ordenadas = sorted(tuplas, key= lambda tupla : tupla[0])  # Essa função lambda acessa a tupla e retorna o índice 0

# Testando algo. 

# lista_chaves = [tupla[0] for tupla in tuplas]

# print(lista_chaves)

# tuplas_ordenadas_a = sorted(tuplas, key= lista_chaves)

# print(tuplas_ordenadas_a)

# Ordenando pelo reultado da soma. 

tuplas_ordenadas_soma = sorted(tuplas, key= lambda tupla : tupla[0] + tupla[1], reverse= True)
print(tuplas_ordenadas_soma)


class Estoque:

    def __init__(self, produto): 
        self.__produto = produtos if produtos != None else []


# Quando utilizamos os lists compressions geralmente, a minha visão não precisamos de 
# utilizar funções lambda, pois conseguimos operar com os números que estão sendo iterados, 
# como desejarmos. 


# Exemplo 

numeros = [numero for numero in range(1, 200 + 1)]
# print(numeros)  

raizes_quadradas = [(numero ** (1/2)) for numero in numeros] # Encontrando as raízes destes números. 

# print(raizes_quadradas)

# print(9 ** (1/2))

# Melhorando um pouco 

raizes_dict = {numero: numero ** (1/2) for numero in numeros}

# Comunicando os resultados

for chave in raizes_dict: 
    print(f"A Raís Quadrada {chave} = {raizes_dict[chave]:.3f}")


#  Map filter e reduce()

# A função map()
# A função map() funciona de uma forma parecida com a de um 
# list compression ele percorre um iteravel aplicando aquele iterável uma função. 

# Com a função map()
numeros_ao_quadrado = [chave ** 2 for chave in raizes_dict]

# Com a função map()

numeros_ao_quadrado_map = map(lambda chave: chave ** 2, raizes_dict)

print("Compression: ")
print(numeros_ao_quadrado)

print("Função Map:")
print(list(numeros_ao_quadrado_map))