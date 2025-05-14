nomes = []
resp = 0

while resp == 0:
    nome = input('Insira o nome: ')
    if nome == 'Sair' or nome == 'sair':
        print('Saindo...')
        break
    else:
        print('Nome inserido')
        nomes.append(nome)
print(nomes)