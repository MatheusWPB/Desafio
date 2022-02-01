
from random import randint

j = int(input('Quantos jogos irá jogar?? '))

g = int(input('Quantos numeros irá querer?? '))

cont = 0 
cont2 = 0 

lista2 = list()

while cont != j:
    lista = list()
    for c in (cont,j):
        n = randint (0,60)
        if n not in lista:
            lista.append(n)
        if n in lista:
            cont = cont + 1

    lista2.append(lista)
print (f'{lista2}')
