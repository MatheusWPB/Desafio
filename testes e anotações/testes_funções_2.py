#scopo 

from calendar import c


def teste (b):
    global a
    a=8
    b+=4
    c=2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
print(f'A vale {a} antes da função')
teste(a)
print(f'A depois da função vale {a}')

#retorno de valores

def somar(d=0,e=0, f = 0):
    s = d + e +f
    return s


resp = somar(3 , 2 , 5)
print(f'{resp}')
print(somar(3,2,5))

