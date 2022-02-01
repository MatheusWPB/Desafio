from ast import If
from turtle import end_fill


a = 2*2


if a<=4:
 print (f'syvtvdcged{a}')
else :
 print ('outro valor')
print ('fim')

#ou 

print ('a'if a<=4 else 'aaa')

# estruturas condicionais

b = float (input('digite um valor'))
if b < 8:
 b = input ('um putrp valor')
elif 9<b>15:
 b = input ('digite um valor par')
else:
 print ('tudo certo')

 #mais complexo

c = float (input('digite um valor '))

if c < 8:
 b = input ('um outro valor')
 print (f'seu valor é{b}')
elif 9<c<15:
 d = input ('digite um valor par')
 print (f'seu valor é {d}')
elif c == 40 :
 print ('numero maluco')
else:
 print ('tudo certo')





