import random
# escolhe um aluno aleatóriamente
a = str(input('1º aluno '))
b = str(input('2º aluno '))
c = str(input('3º aluno '))
d = str(input('4º aluno '))
todos = ([a, b, c, d])
print(random.choice(todos))
