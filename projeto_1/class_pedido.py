import time

class Pedido: 

    def __init__(self, cliente= None, pratos= None):

        self.__cliente = cliente if cliente else ""
        self.__pratos = [] if pratos == None else pratos 
        self.__preco = sum(self.__pratos.preco_total)
        self.__status = False

    # Getters

    @property 
    def cliente(self):
        return self.__cliente 

    @property 
    def pratos(self):
        return self.__pratos 

    @property 
    def preco(self):
        return self.__preco 

    @property 
    def status(self):
        return self.__status 

    # Setters 

    @cliente.setter 
    def cliente(self, novo_cliente):
        self.__cliente = novo_cliente 

    @pratos.setter 
    def pratos(self, novos_pratos):
        self.__pratos = novos_pratos 

    @preco.setter 
    def preco(self, novo_preco):
        self.__preco = novo_preco 

    @status.setter 
    def status(self, novo_status):
        self.__status = novo_status 


    # Métodos 

    def adcionar_prato(self, objeto_prato):

        self.__pratos.append(prato)

        print("Prato adicionado!")
        time.sleep(2)

    def remover_prato(self):

        for prato in self.__pratos:
            print(f"""- ID: {prato.id_}
- Nome: {prato.sabor} 
- Valor: {prato.preco} 
- Quantidade: {prato.unidades}
- Total: {prato.preco_total}""")

        print("=====================")

        print(f"Valor Total: {self.__preco}")

        while True:

            print("Removendo Pratos...")
            time.sleep(2)

            print("Para continuar digite ok.")
            print("Para encerrar digite cancelar.")

            opcao = input("Indique a sua opção: ")

            if opcao.lower() == "ok":

                id_prato = input("Indique o id do prato que você gostaria de remover:  ")
                time.sleep(2)

                nome_prato = input("Indique o nome do prato que você gostaria de remover: ")
                time.sleep(2)

                for prato in self.__pratos:

                    if prato.sabor.lower() == nome_prato.lower() or \
                    id_prato == prato.id_:

                        self.__pratos.remove(prato) 


                    else: 

                        print("Prato não encontrado!")
                        time.sleep(2)

                        print("Tentando novamente...")
                        time.sleep(2)


            elif opcao.lower() == "cancelar":

                print("Encerrando...")
                time.sleep(2)

                print("Operação Concluída!")
                time.sleep(2)

                break 

            else: 

                print("Opção não identificada...")
                time.sleep(2)

                print("Tentando novamente...")
                time.sleep(2)

    # def calcular_preco(self):

    #     valor_total = 0

    #     for prato in self.__pratos:

    #         valor_total += prato.preco

    #     self.__preco = valor_total 





# pedido_1 = Pedido("Marcos", ["Pizza Mussarela", "Pizza de Carne Seca"])

# pedido_1.adcionar_prato()

# print("Pratos:", pedido_1.pratos)

# pedido_1.remover_prato()

# print("Pratos:", pedido_1.pratos)

# lista_a = [1, 2, 3, 4, 5, 6]

# print(sum(lista_a))