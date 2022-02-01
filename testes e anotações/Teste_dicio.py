#dicionario

filme = {'titulo':'StarWars',
        'ano':1977,
        'diretor' : 'GeorgeLucas',
}

print(filme.values())

print(filme.keys())

print(filme.items())

for k,v in filme.items():
    print(f'O {k} é {v}')

#dicionarios em listas

brasil = list()
estado = {'uf':'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado)
brasil.append(estado2)

print(f'{brasil}')

#Dicionario em listas

estado = dict()
brasil = list()
for c in range (0,2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:  
    for k, v  in e.items():
        print(f'O campo {k} tem valor {v}')  