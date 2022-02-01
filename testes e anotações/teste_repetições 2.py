#sistema de repetição

#complexas

a = int(input('digite uma valor: '))
y = 0
s = 0

while y != a :
    y = y +1
    print (f'{y}')
    s += y
print(f'valor {y},somatoria {s}')

#mais complexos

#Numeros impares e Pares 

n = 1
par = impar =0

while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print (f'Seu valor digitado foi {n} numeo pares {par} numeros impares {impar}')





