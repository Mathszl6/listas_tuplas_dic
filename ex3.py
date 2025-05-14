valor = input('Insira 10 numeros separados por espaço: ').split(" ")
lista = []

for i in valor:
    num = int(i)
    lista.append(num)
print(lista)