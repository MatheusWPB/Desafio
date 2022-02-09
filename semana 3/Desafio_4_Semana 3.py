def fatorial (f,  show =True):
    '''
    --> O programa faz com que assim que dado um valor, irá calcular o fatorial do valor digitado, mas precisando em seguida do valor, colocar para show True que mostrará os calculos feitos e False para não mostrar os calculos, ficando ('numero', show = True ) ou ('numero', show = False ) 
    '''
    cont = 1 
    a = 1
    while cont != f+1:
        if show:
            print(cont, end ='')
            cont2 = 0
            while cont2 != 1:
                cont2 += 1
                print(' x ', end ='')
        a *= cont
        cont += 1
    if show == False:
        print (f' O fatorial de {f} = {a}')
    if show == True:
        print (f'= {a}')



fatorial(6, show = True)