import time 

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
        self.__fornecedores: list = fornecedores if not fornecedores == None else []



    # Desenvolvendo o encapsulamento 
    # Getters
    @property 
    def id_(self):
        return self.__id_ 

    @property 
    def gerente(self):
        return self.__gerente 

    @property 
    def equipe(self):
        return self.__equipe 

    @property 
    def folha_pagamento(self):
        return self.__folha_pagamento 

    @property 
    def estoque(self):
        return self.__estoque 

    @property 
    def historico_pedidos(self):
        return self.__historico_pedidos 

    @property 
    def cardapio(self):
        return self.__cardapio 

    @property 
    def pedidos_em_preparo(self):
        return self.__pedidos_em_preparo 

    @property 
    def fornecedores(self):
        return self.__fornecedores 


    # Setters 

    @id_.setter
    def id_(self, novo_id: str):
        self.__id_ = novo_id 

    @gerente.setter
    def gerente(self, novo_gerente: str):
        self.__gerente = novo_gerente

    @equipe.setter
    def equipe(self, nova_equipe: list):
        self.__equipe = nova_equipe 

    @folha_pagamento.setter 
    def folha_pagamento(self, nova_folha: list):
        self.__folha_pagamento = nova_folha

    @estoque.setter 
    def estoque(self, novo_estoque: list):
        self.__estoque = novo_estoque 

    @historico_pedidos.setter 
    def historico_pedidos(self, historico_pedidos: list):
        self.__historico_pedidos = historico_pedidos 

    @cardapio.setter 
    def cardapio(self, n_cardapio):
        self.__cardapio = n_cardapio 

    @pedidos_em_preparo.setter 
    def pedidos_em_preparo(self, n_pedidos_preparo):
        self.__pedidos_em_preparo = n_pedidos_preparo 

    @fornecedores.setter 
    def fornecedores(self, n_fornecedores):
        self.__fornecedores = n_fornecedores 

    def contratar_colaborador(self):

        """O loop principal desta função possui três condições de parada específicadas 
a primeira quando a quantidade de contratações for igual a quantidade desejada de contratações
e a segunda quando o usuário desejar. """



        def validar_usuario():


            print("Validando usuário...")
            time.sleep(2)

            usuario_validado = False

            tentativas = 0
            while tentativas < 3:

                id_gerente = input("Indique o seu id de gerente: ")
                senha_gerente = input("Indique a sua senha: ")

                if self.__gerente:

                    if self.__gerente.id_ == id_gerente:

                        print("Gerente encontrado...")
                        time.sleep(2)

                        if self.__gerente.senha == senha_gerente: 

                            print("Senha validada...")
                            time.sleep(2)

                            usuario_validado = True 

                            break 
                        
                        else: 

                            print("Senha inválida...")
                            time.sleep(2)

                            print("Tentando novamente...")
                            time.sleep(2)

                            tentativas += 1


                    else: 

                        print("Gerente não encontrado...")
                        time.sleep(2)

                        print("Tentando novamente...")
                        time.sleep(2)

                        tentativas += 1


            return usuario_validado 


        avaliacao_usuario = validar_usuario 

        if avaliacao_usuario: 




            trabalhadores_contratar = int(input("Indique a quantidade de trabalhadores que você quer contratar: "))
            trabalhadores_contratados = 0


            while trabalhadores_contratados < trabalhadores_contratar:

                print("""Para continuar digite ok.
Para parar digite cancelar.""")
                time.sleep(2)

                opcao = input("Indique a sua opção: ")

                if opcao.lower() == "ok":

                    print("============ Formulário de Cadastro ============")
                    time.sleep(2)

                    nome = input("Indique o nome do candidato: ")

                    nome_formatado = nome.title()

                    idade = float(input("Indique a idade do candidato: "))
                    cpf = float(input("Indique o cpf do candidato: "))
                    cargo = input("Indique o cargo do candidato: ")
                    salario = float(input("Indique o salário inicial do candidato: "))

                    if idade >= 18:

                        if  1600.00 < salario < 10000.00:

                            candidato = colaborador.Colaborador(nome_formatado, idade, cpf, cargo, salario)
                            self.__equipe.append(candidato)

                            trabalhadores_contratados += 1


                        else: 

                            print("Salário não permitido!")
                            time.sleep(2)

                            print("Tentando novamente...")
                            time.sleep(2)

                    else: 

                        print("Não admitimos candidatos com idade menor que 18 anos.")  
                        time.sleep(2)

                        print("Tentando novamente...")
                        time.sleep(2)


                elif opcao == "cancelar":

                    print("Encerrando operação...")
                    time.sleep(2)

                    break 


                else: 

                    print("Opção não encontrada!")
                    time.sleep(2)

                    print("Tentando novamente...")
                    time.sleep(2)



        else: 

            print("Operação não altorizada...")
            time.sleep(2)



# Continuar a codificação, 
# seguindo o escopo e 


# Testando a class Pizzaria. 

# Criar a classe Colaborador, e consequêntemente criar a classe pessoa, e gerente para testar a classe pizzaria. 
# pizzaria = Pizzaria()