lista = []
def listar(lista):
    for i, item in enumerate(lista):
        print(f'O {i+1}° item é {item}')
    pass
def adicionar(dado, lista):
    lista.append(dado)
    print('O dado foi adicionado.')
    pass
def remover(dado, lista):
    lista.remove(dado)
    print('O dado foi removido.')
    pass

while True:
    print(f'Opção 1 - Listar\nOpção 2 - Adicionar Item\nOpção 3 - Remover Item\nOpção 4 - Sair')
    responde_user = input('Digite a sua opção: ')
    if responde_user == '1':
        listar(lista)
    elif responde_user == '2':
        dado = input('Digite o que deseja adicionar: ').lower()
        adicionar(dado,lista)
    elif responde_user == '3':
        dado = input('Digite o que deseja remover: ').lower()
        remover(dado,lista)
    elif responde_user == '4':
        print('Até mais!')
        break
    else:
        print('Opção inválida, digite novamente: ')