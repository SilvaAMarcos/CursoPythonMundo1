import random
n1 = str(input('Qual o primeiro aluno '))
n2 = str(input('Qual o segundo aluno '))
n3 = str(input('Qual o terceiro aluno '))
n4 = str(input('Qual o quarto aluno '))
lista = [n1, n2, n3, n4]
esc = random.choice(lista)
print('O aluno escolhido é {} '.format(esc))
