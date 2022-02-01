#sistema de repetição

#Mais² complexo

cont = 1

while cont <= 10:
    print(cont,', ',end = '')
    cont += 1
print ('Acabou')    

#Mais³ complexo

n = s = cont = 0
while n != 999:
    n =  int(input('Digite um número'))
    cont += 10
    s += n
s -= 999
print (f'A soma vale {s}')


#Mais4 complexo

n = s = cont = 0
while True:
    n =  int(input('Digite um número  '))
    if n == 999:
        break
    cont += 10
    s += n
s -= 999
print (f'A soma vale {s}, {cont}')
