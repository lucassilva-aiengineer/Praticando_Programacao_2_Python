import random 

def gerar_id():

    id_ = ""

    caracteres_gerar = 10
    caracteres_gerados = 0
    while caracteres_gerados < caracteres_gerar:

        numero_a = random.randint(0, 9)

        if not str(numero_a) in id_: 

            id_ += str(numero_a)

            caracteres_gerados += 1


    return id_ 

