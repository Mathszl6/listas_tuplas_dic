nomes = input('Insira 5 nomes separados por virgula: ').split(',')
lista = [nome for nome in nomes]

if len(lista) != 5:
    print('Por favor insira exatamente 5 nomes.')
else:
    for name in lista:
        print(name)