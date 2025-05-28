frase = input('Insira uma frase: ').split(' ')

def words(frase_toda):
    lista = [palavra for palavra in frase_toda]

    return lista

palavras = words(frase)
print(palavras)