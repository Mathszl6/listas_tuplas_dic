num = input('Insira 5 numeros separados por virgula: ').split(',')
lista = [int(i) for i in num]

print(f'A lista é: {lista}\nO maior valor é: {max(lista)}\nO menor valor é: {min(lista)}')