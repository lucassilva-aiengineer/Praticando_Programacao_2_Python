

class Pizzaria: 

    def __init__(self, gerente= None, equipe= None, folha_pagamento= None, \
    estoque= None, historico_pedidos= None, cardapio= None, pedidos_em_preparo= None, \
    fornecedores= None):

        self.__id_ = gerar_id()
        self.__gerente: str = gerente if gerente != None else ""
        self.__equipe: list = equipe if equipe != None else list()
        self.__folha_pagamento: list = folha_pagamento if folha_pagamento != None else list()
        self.__estoque: list = estoque if not estoque == None else list()
        self.__historico_pedidos: list = historico_pedidos if not historico_pedidos == None else list()
        self.__cardapio: list = cardapio if not cardapio == None else list()
        self.__pedidos_em_preparo: list = pedidos_em_preparo if pedidos_em_preparo != None else []


# Continuar a codificação, 
# seguindo o escopo e 