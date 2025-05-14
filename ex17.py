numeros = input('Insira os números separados por virgula: ').split(',')
lista = [int(num) for num in numeros]
media = 0

for num in lista:
    media += num / len(lista)
print(media)