a = [1,2,3,4,5,6]

#adicionar caracter
a.append (7)

print (a)

a.insert (3,3.5)
a.insert (4,3.7)

print (a)

#remover caracter
a.pop (4)

print (a)

a.remove (3)

print(a)

#criar uma lista 
b = list(range(4,12))

print (b)

#ordenar uma lista 
c = [2,1,4,5,7,6,9,8,10,23,22,25]

print(c)

c.sort()

print (c)

c.sort(reverse=True)

print (c)

#quantos elementos

len(c)

print (f'{len(c)}')

#loopings 

valor = list()
for cont in range (0,5):
    valor.append(int(input('Digite um valor: ')))

for c,v in enumerate (valor):
    print (f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')

#copiar uma linha 

j = [4,5,7,8]

print (j)

i = j[:]

print (i)

i[2]=2

print (i)

