palavra = "Mateus5"

print(list(enumerate(palavra)))

# sys.exit()

# valores = [letra for letra in palavra if letra != 'a' else 'b' ] Não é um ternary e sim um compression list

valores = [letra if letra != 'a' else '*' for letra in palavra] # Expression list 

string_protegida = ""
# string_protegida += [valores]

for letra in valores:
    string_protegida += letra

print(string_protegida)

# import string 

# letras = []

# letras += string.ascii_uppercase
# print(letras)