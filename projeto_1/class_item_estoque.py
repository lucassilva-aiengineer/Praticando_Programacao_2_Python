import funcoes_a
from datetime import datetime

def comparar_datas(validade):


    hoje = datetime.now()
    if validade <= hoje:  

        return True

    else: 
        return False 

# assert comparar_datas(data) == True, "Deveria ser True" 

class ItemEstoque:
    """ Esta classe modela os itens que poderam ser adicionados 
    ao estoque da pizzaria."""

    def __init__(self, nome, custo= None, validade: str= "01-01-2026", quantidade= None, fornecedores= None):

        self.__id_ = funcoes_a.gerar_id()
        self.__nome = nome 
        self.__fornecedores = [] if fornecedores == None else fornecedores
        self.__custo: float = custo if custo != None else 0 
        self.__validade: str = validade 
        self.__vencido: bool = comparar_datas(self.__validade)  
        self.__quantidade: int = 0 if quantidade == None else quantidade 
        self.__preco_total: float = self.__quantidade * self.__custo 


    # Definindo os getters 
    @property 
    def nome(self):
        return self.__nome 

    @property 
    def fornecedores(self):
        return self.__fornecedores

    @property 
    def custo(self):
        return self.__custo 

    @property 
    def validade(self):
        return self.__validade 

    @property
    def vencido(self):

        """ Quando o item estiver vencido terá valor True 
        quando não terá valor false."""

        return self.__vencido 

    @property 
    def quantidade(self):
        return self.__quantidade

    @property 
    def preco_total(self):
        return self.__preco_total 

    # Setter 
    # Definindo a escrita 
    @nome.setter 
    def nome(self, novo_nome):
        self.__nome = novo_nome 

    @fornecedores.setter 
    def fornecedores(self, novos_fornecedores):
        self.__fornecedores = novos_fornecedores

    @custo.setter 
    def custo(self, novo_custo):
        self.__custo = novo_custo 

    @validade.setter 
    def validade(self, nova_validade):
        self.__validade = nova_validade

    @vencido.setter 
    def vencido(self, novo_vencimento):
        self.__vencido = novo_vencimento

    @quantidade.setter 
    def quantidade(self, quantidade_unidades):
        self.__quantidade = quantidade_unidades 

    @preco_total.setter 
    def preco_total(self, novo_preco):
        self.__preco_total = novo_preco 

