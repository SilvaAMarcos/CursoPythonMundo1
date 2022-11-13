var = str(input('Digite um nome: ')).strip().upper()

print('O nome digitado tem {} caracteres "A"'.format(var.count('A')))
print('Aparece a esquerda na posição: {}'.format(var.find('A')+1))
print('Aparece a direita na posição: {}'.format(var.rfind('A')))
