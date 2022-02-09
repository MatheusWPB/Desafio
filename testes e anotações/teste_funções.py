#função

def linha():
    print ('-'*30)

#programa
linha()
print ('deu certooo'.upper())
linha()

#segundo exemplo

#função

def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

#programa

titulo('Curso'.upper())
titulo('python'.upper())

#terceiro exemplo

def soma (a,b):
    """
    -> o programa tem o intuito de somar os indices a e b entre sí

    """
    print(f'A = {a} e B = {b}')
    s = a + b 
    print(f'A soma de A + B = {s}')


#programa

soma(3,5)

#Contador

def contador(*num):
    """
    -> o programa retorna os nomes colocados dentro da lista
    """
    print(num)

contador(2, 5, 4)
contador(4,5)

help(soma)
help(contador)

#parametros opicionais

def somar ( c=0 , d = 0, e = 0):
    p = c + d + e
    print(f'{p}')



somar(2,4,5)

somar (1,2)

#escopo de variaveis
def função():
    n1 = 4
    print(f'N1 dentro vale {n1}')



n1 = 2
print(f'N1 global vale{n1}')
função()


