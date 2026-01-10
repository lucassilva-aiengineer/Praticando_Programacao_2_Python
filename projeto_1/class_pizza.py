class Pizza: 
    def __init__(self, sabor= None, descricao= None, igredientes= None, \
    preco= None, custo= None, unidades= None):

        self.__sabor = sabor if sabor else ""
        self.__descricao: str = descricao if descricao else ""
        self.__igredientes: list = [] if not igredientes else igredientes
        self.__preco: float = preco if preco != None else 0
        self.__custo: funcoes.calcular_custo_pizza(self.__igredientes)
        self.__unidades: int = unidades if unidades else 0
        self.__preco_total: float = self.__unidades * self.__preco

    # Getters 

    @property 
    def sabor(self):
        return self.__sabor 

    @property 
    def descricao(self):
        return self.__descricao 

    @property 
    def igredientes(self):
        return self.__igredientes 

    @property 
    def preco(self):
        return self.__preco 

    @property 
    def custo(self):
        return self.__custo 

    @property 
    def unidades(self):
        return self.__unidades 

    @property 
    def preco_total(self):
        return self.__preco_total 

    # Setters 

    @sabor.setter 
    def sabor(self, novo_sabor):
        self.__sabor = novo_sabor 

    @descricao.setter 
    def descricao(self, nova_descricao):
        self.__descricao = nova_descricao 

    @igredientes.setter 
    def igredientes(self, novos_igredientes):
        self.__igredientes = novos_igredientes 

    @preco.setter 
    def preco(self, novo_preco):
        self.__preco = novo_preco 

    @custo.setter 
    def custo(self, novo_custo):
        self.__custo = novo_custo

    @unidades.setter 
    def unidades(self, nova_quantidade):
        self.__unidades = nova_quantidade 

    @preco_total.setter 
    def preco_total(self, novo_preco):
        self.__preco_total = novo_preco 


    # Métodos 

    def adicionar_igredientes(self):

        """ Este método permite a adicão de igredientes a pizza. """

        igredientes_adicionar = int(input("Indique a quantidade de igredientes adicionados: "))

        igredientes_adicionados = 0
        while igredientes_adicionados < igredientes_adicionar:

            nome = input("Indique o nome do igrediente: ")

            # self.__igredientes += [nome]
            self.__igredientes.extend([nome])

            igredientes_adicionar += 1 

        print("Operação concluída :)")
        time.slee(2)

        print("...")
        time.sleep(2)

