#sistema de repetição

#simples 

b = int(input('digite um valor: '))
a = int(input ('digite um valor para a: '))
c = int(input('quantas repetições: '))
s=0
for c in range (0,b):
    if c<10:
        a = a + 1
    s += c      
print (f'valor de a: {a}, valor de c: {c}, e a somatoria igual a: {s}')        