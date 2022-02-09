def maior (*a):
    lista = len(a)
    cont = 0
    lista2 = list()
    cont2 = 0
    while cont != lista:
        lista2.append(a[cont2])
        cont2 += 1
        cont += 1
    lista2.sort()
    lista2.reverse()
    print (lista2)
    print (f'o numero maior digitado foi {lista2[0]}')



maior(14,540,36)
maior (600,800,90,8)
maior(15,50,80,68,900,40,21,4)