def leiaInt(msg):
    while True:
        a = input(msg)
        if a.isnumeric():
         valor = int(a)
         print(f'\033[0;32m Seu valor foi {valor}\033[m')
         break
        else:
         print('\033[0;31m Falso, digite um nnumero na forma numerica\033[m')

    
n = leiaInt('digite um numero: ')