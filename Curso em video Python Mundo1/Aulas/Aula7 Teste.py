# nome = input('Muito prazer em conhecer, qual é o seu nome? ')
# print('Prazer em conhecer voce {:=^20}! '.format(nome))


n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
divisao = n1 / n2
multi = n1 * n2
sub = n1 - n2
di = n1 // n2
res = n1 % n2
expo = n1 ** n2
print('A multiplicação é {} , a divisão é {:.3f} , a adição é {} , a divisão inteira é {} '
      ', \n a exponenciação é {} , o resto da divisão é {} e a subtração é {}'
      .format(multi, divisao, soma, di, expo, res, sub))
print('A soma vale {}'.format(n1+n2))


