from faker import Faker
import random
from datetime import datetime, timedelta
import sys
import time 


def gerar_validade_a():

    hoje = datetime.now()
    dias_aleatorios = random.randint(10, 300)

    numero_aleatorio = random.randint(0, 1000)

    # print(numero_aleatorio)
    if numero_aleatorio % 3 == 0: 
        data_futura = hoje - timedelta(days= dias_aleatorios)

    else: 
        data_futura = hoje + timedelta(days= dias_aleatorios)

    return data_futura 

data = gerar_validade_a()

# print(data) 


class Estoque:
    """Esta classe modela o objeto Estoque """
    def __init__(self, lista_itens= None):
        self.__lista_itens = [] if lista_itens == None else lista_itens 
        
        """Este atributo é um list compression dos itens da lista de itens que possuem uma data de validade inferior a da consulta. """
        self.__itens_vencidos: list = [item for item in self.__lista_itens if item.vencido == True]
        self.__itens_validos: list = [item for item in self.__lista_itens if item.vencido == False]
        self.__itens_faltando: list = [item for item in self.__lista_itens if item.quantidade == 0]
        self.__valor_itens_validos: list = sum([item.preco_total for item in self.__lista_itens if item.vencido == False])
        self.__valor_itens_vencidos: list = sum([item.preco_total for item in self.__lista_itens if item.vencido == True])
        self.__total_estoque: list = sum([item.preco_total for item in self.__lista_itens])


    @property 
    def lista_itens(self):
        return self.__lista_itens 

    @property 
    def itens_vencidos(self):
        return self.__itens_vencidos 

    @property 
    def itens_faltando(self):
        return self.__itens_faltando 

    @property 
    def valor_itens_validos(self):
        return self.__valor_itens_validos 

    @property 
    def valor_itens_vencidos(self):
        return self.__valor_itens_vencidos

    @property 
    def total_estoque(self):
        return self.__total_estoque 

    @lista_itens.setter 
    def lista_itens(self, novos_itens):
        self.__lista_itens = novos_itens

    @itens_vencidos.setter 
    def itens_vencidos(self, novos_vencidos):
        self.__itens_vencidos = novos_vencidos 

    @valor_itens_validos.setter 
    def valor_itens_validos(self, valor_validos):
        self.__valor_itens_validos = valor_validos

    @valor_itens_vencidos.setter
    def valor_itens_vencidos(self, valor_vencidos):
        self.__valor_itens_vencidos = valor_vencidos


    # Métodos do objeto 

    # Método que exibe os produtos 

    def mostrar_produtos(self):

        for item in self.__lista_itens:
            print(f"""
===========================================
Item: {item.nome}
Quantidade: {item.quantidade} Un
Preço: {item.custo:.2f}
Custo Total: {item.preco_total:.2f}
Fornecedores: {item.fornecedores}
Validade: {'Vencido' if item.vencido == True else 'Válido'}
Data de Validade: {item.validade.day}/{item.validade.month}/{item.validade.year}""")

        else:
            print(f"Valor total estoque: {self.__total_estoque}")

    def mostrar_itens_validos(self):

        for item in self.__itens_validos:
            print(f"""
===========================================
Item: {item.nome}
Quantidade: {item.quantidade} Un
Preço: {item.custo:.2f}
Custo Total: {item.preco_total:.2f}
Fornecedores: {item.fornecedores}
Validade: {'Vencido' if item.vencido == True else 'Válido'}
Data de Validade: {item.validade.day}/{item.validade.month}/{item.validade.year}""")

        print(f"Valor Itens Válidos: R$ {self.__valor_itens_validos:.2f}")

    def mostrar_itens_vencidos(self):

        for item in self.__itens_vencidos: 

            print(f"""
===========================================
Item: {item.nome}
Quantidade: {item.quantidade} Un
Preço: {item.custo:.2f}
Custo Total: {item.preco_total:.2f}
Fornecedores: {item.fornecedores}
Validade: {'Vencido' if item.vencido == True else 'Válido'}
Data de Validade: {item.validade.day}/{item.validade.month}/{item.validade.year}""")

        else:
            print(f"Valor Itens Vencidos: R$ {self.__valor_itens_vencidos}")

    def mostrar_itens_faltando(self):

        for item in self.__itens_faltando:
            print(f"""
===========================================
Item: {item.nome}
Quantidade: {item.quantidade} Un
Preço: {item.custo:.2f}
Custo Total: {item.preco_total:.2f}
Fornecedores: {item.fornecedores}
Validade: {'Vencido' if item.vencido == True else 'Válido'}
Data de Validade: {item.validade.day}/{item.validade.month}/{item.validade.year}""")


# print(sum([1, 2, 3]))

# print(lista_somada)


# Testando a classe itens estoque e a classe estoque. 

# sys.exit()


def teste_1():

    print("Intens estoque: ")
    print(estoque_1.lista_itens)

    print("")
    print("Itens Faltando: ")
    print(estoque_1.itens_faltando)

    print("\nItens Vencidos: ")
    print(estoque_1.itens_vencidos)

    print("\n Valor itens válidos:\n ")

    print(estoque_1.valor_itens_validos)

    print("\n Valor itens vencidos: \n")
    print(estoque_1.valor_itens_vencidos)


# Testando métodos. 

def main():

    "Esta função cria e permite a operação dos métodos"


    objetos_itens = []


    igredientes = ["Molho de tomate", "Água mineral", "Refrigerante de Limão", "Farinha de Trigo", 
    "Tomate", "Açucar", "Sal", "Muzzarela", "Presunto", "Peperoni"]


    faker = Faker()
    for numero in range(0, 10):

        random.shuffle(igredientes)

        nome = random.choice(igredientes) 
        custo = random.uniform(5, 20)
        validade = gerar_validade_a()
        quantidade = random.randint(0, 100)
        fornecedores = [faker.last_name() for a in range(0, 3)]

        from class_item_estoque import ItemEstoque
        objeto = ItemEstoque(nome, custo, validade, quantidade, fornecedores)

        objetos_itens.append(objeto)


    estoque_1 = Estoque(objetos_itens)


    print("Bem vindo ao sistema de Estoques Pizzarias Pizza Mais.")

    while True:

        print("Para Ver o estoque digite 1.")
        print("Para Ver apenas os itens válidos digite 2.")
        print("Para ver apenas os itens vencídos digite 3.")
        print("Para Ver os itens em falta digite 4.")
        print("Para encerrar o sistema digite 5.")
        print("Para ver as opções novamente digite 6.")

        opcao = int(input("Indique a sua opção: "))

        if opcao == 1:

            print("Vendo o estoque...")
            time.sleep(2)

            estoque_1.mostrar_produtos()

        elif opcao == 2:

            print("Vendo os itens válidos...")
            time.sleep(2)

            estoque_1.mostrar_itens_validos()

        elif opcao == 3: 

            print("Vendo os itens vencídos...")
            time.sleep(2)

            estoque_1.mostrar_itens_vencidos()

        elif opcao == 4:

            print("Vendo os itens em falta...")
            time.sleep(2)

            estoque_1.mostrar_itens_faltando()

        elif opcao == 5:

            print("Encerrando o sistema...")
            time.sleep(2)

            break

        elif opcao == 6:

            print("Retornando ao menu princípal...")
            time.sleep(2)

        else: 

            print("Opção inválida!")
            time.sleep(2)

            print("Tentando novamente...")
            time.sleep(2)

try:
    main()

except TypeError as message:
    print("Message:" + " " + message)
    print("As opções devem ser descritas utilizandos apenas números!")

    print("Tentando novamente...")
    time.sleep(2)

    main()
else:

    print("Código executado com sucesso!")
    time.sleep(2)

finally: 

    print("O código terminou!")