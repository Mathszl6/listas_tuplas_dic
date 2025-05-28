nomes = input('Insira os nomes desejados separados por vírgula: ').split(',')
nomeNormal = []

for nome in nomes:
    if nome not in nomeNormal:
        nomeNormal.append(nome)

print(nomeNormal)