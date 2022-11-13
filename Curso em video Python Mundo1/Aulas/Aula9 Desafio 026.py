frase = str(input('Digite uma frase: '))
print('A frase tem {} letras "a"'.format(frase.count('a'))) #conta a quantidade de letras
print('A primeira letra a está é a {} '.format(frase.find('a'))) #procura a primeira letra a esquerda
print('A ultima letra a é {} '.format(frase.rfind('a')))  # procura a primeira letra a direita
