numeros = input('Insira 5 números separados por virgula: ').split(',')

if len(numeros) != 5:
    print('Insira exatamente 5 números.')
else: 
    for num in numeros:
        if int(num) > 10:
            print(f'{num} é maior que 10.')
        else: 
            print(f'{num} não é maior que 10.')