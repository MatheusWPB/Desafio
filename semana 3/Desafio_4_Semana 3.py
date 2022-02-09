def fatorial (f):
    cont = 1 
    a = 1
    while cont != f+1:
        a *= cont
        cont += 1
        print(f'{a}')
    print (f'O fatorial é igual a {a}')



fatorial(6)