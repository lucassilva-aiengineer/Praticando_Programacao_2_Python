import string 
from typing import List 
import random 


def gerar_id(*args, **kwargs) -> str:

    id_ = ""

    alfabeto: List[str] = []
    alfabeto += string.ascii_lowercase + string.ascii_uppercase 

    caracteres = kwargs["caracteres"]

    for a in range(caracteres):

        # selecao = random.randint(0, 2)

        if a < 3: 

            numero_id = random.randint(0, 10) 

            id_ += str(numero_id) 

        else:

            random.shuffle(alfabeto)
            id_ += random.choice(alfabeto)
    # id_ = input("Indique uma função: ") 

    return id_

# print() 

lista_letras: List[str] = []

lista_letras += string.ascii_lowercase + string.ascii_uppercase

print(lista_letras)