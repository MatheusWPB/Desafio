#DICIO E LISTA 
situação = dict()
geral = list()

#Variaveis
alunos =  int(input('Quantos alunos serão avaliados??  '))

#CONTADORES
cont = 0 

#ESTRUTURA 

while cont != alunos:
    situação['nome'] = str(input('Qual nome do aluno?? '))
    situação['nota'] = int(input('Qual a nota desse aluno?? '))
    if situação['nota'] < 5:
        situação ['estado'] = str('reprovado')
    elif situação ['nota'] >= 5:
        situação['estado'] = str('aprovado')
    geral.append(situação.copy())
    situação.clear()
    cont += 1
print(f'A situação dos seus alunos é {geral}')