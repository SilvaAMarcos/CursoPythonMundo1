n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print('O maior é {}'.format(maior))

menor = n1

if n2 < menor:
   menor = n2
if n3 < menor:
    menor = n3
print('E o menor é {}'.format(menor))
print('----- Fim Execução -----')

