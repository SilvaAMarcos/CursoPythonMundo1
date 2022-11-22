import random

num = random.randint(1, 5)
nuser = int(input('Em qual numero de 1 a 5 estou pensando?'))


if nuser == num:
    print('Voce acertou em cheio, meus parabéns!!!')
else:
    print('Tente mais uma vez, na proxima vai dar certo.')
print('Obrigado por jogar... eu pensei em {}'.format(num))
