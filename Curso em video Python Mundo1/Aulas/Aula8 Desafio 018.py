# Lendo um valor de um numero e mostrando seu seno, cosseno e tangente
import math
n1 = float(input('Digite um angulo: '))
n = math.radians(n1)
print('o seno é {:.2f}, o cosseno é {:.2f} e tangente é {:.2f}'.format(math.sin(n), math.cos(n), math.tan(n)))
