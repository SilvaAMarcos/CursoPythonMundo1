c1 = float(input('Digite o primeiro cateto: '))
c2 = float(input('Digite o segundo cateto '))
h = ((c1 * c1) + (c2 * c2)) ** 0.5
print('A hipotenusa é {:.2f} '.format(h))

'''
import math
c1 = float(input('Digite o primeiro cateto: '))
c2 = float(input('Digite o segundo cateto '))
h = math.hypot(c1, c2)
print('A hipotenusa é {:.2f} '.format(h))
'''