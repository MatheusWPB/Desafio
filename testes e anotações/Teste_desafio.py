from random import randint

print('-'*30)
print('   Sorteador de jogos  '.upper())
print('-'*30)

lista=list()
j = int(input('Quantos jogos irá jogar?? '))
c = int(input('quantos jogos serão sorteados??  '))
cont = 0
m = 0

lista2 = list()
while m != j:
    while cont != c:
     n = randint (0,60)
     if n not in lista:
        lista.append(n)
        n += 1
        cont += 1 
     if n in lista:
        n += 1
        lista.append(n)
        cont +=  1
    lista.sort()
    lista2.append(lista.copy())
    lista.clear()
    cont = 0
    m += 1
print (f'Seus numeos são: {lista2}')