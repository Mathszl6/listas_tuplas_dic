palavras = ['uva','morango','banana']
string = ''

for palavra in range(len(palavras)):
    string += palavras[palavra]
    if palavra < len(palavras) - 1:
        string += ', '

print(string)
    