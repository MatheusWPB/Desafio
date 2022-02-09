def voto(a):
    data = int(input('Qual ano estamos?? '))
    idade = data - a
    if idade < 17:
        print (f'sua idade é {idade}: não pode votar')
    elif 17 <= idade < 18:
        print (f'sua idade é {idade}: voto opcional')
    if 18 <= idade <65:
        print (f'sua idade é {idade}: voto obrigatorio')
    if idade > 65:
        print (f'sua idade é {idade}: voto opcional')



#programa principal

a = int(input('em que ano voceê nasceu?? '))

#saida 

voto(a)