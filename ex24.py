numero = input('Insira 10 numeros separados por virgula: ').split(',')
pares = [int(n) for n in numero if int(n) % 2 == 0]
impares = [int(n) for n in numero if int(n) % 2 != 0]

print(pares)
print(impares)