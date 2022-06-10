import math
# calculando a hipotenusa
a = float(input('cateto adjacente: '))
o = float(input('cateto oposto: '))
h = math.sqrt(math.pow(a, 2) + math.pow(o, 2))
print('a hipotenusa é: {:.2f}'.format(h))