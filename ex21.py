numero = input('Insira 10 numeros separados por virgula: ').split(',')
normais = [int(n) for n in numero]

for n in normais:
    if n % 2 == 0:
        normais.remove(n)
print(normais)