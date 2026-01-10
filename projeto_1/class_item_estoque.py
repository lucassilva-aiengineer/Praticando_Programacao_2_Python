from funcoes import gerar_id

class ItemEstoque:
    """ Esta classe modela os itens que poderam ser adicionados 
    ao estoque da pizzaria."""

    def __init__(self, nome, custo= None, validade: str= "01-01-2026", unidades= None, fornecedores= None):

        self.__id_ = gerar_id()
        self.__nome = nome 
        self.__fornecedores = [] if fornecedores == None else fornecedores
        self.__custo: float = custo if custo != None else 0 
        self.__validade: str = validade 
        self.__vencimento: bool = False 
        self.__unidades: int = 0 if unidades == None else unidades 
        self.__preco_total: float = self.__unidades * self.__custo 


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
    def vencimento(self):
        return self.__vencimento 

    @property 
    def unidades(self):
        return self.__unidades 

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

    @vencimento.setter 
    def vencimento(self, novo_vencimento):
        self.__vencimento = novo_vencimento 

    @unidades.setter 
    def unidades(self, quantidade_unidades):
        self.__unidades = quantidade_unidades 

    @preco_total.setter 
    def preco_total(self, novo_preco):
        self.__preco_total = novo_preco 

