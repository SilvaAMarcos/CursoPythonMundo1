# import math importando toda a biblioteca math
import random
from math import sqrt, floor  # importando apenas sqrt e floor
# import emoji
num = float(input('Digite um numero: '))
nran = random.randint(1, 29)
raiz = sqrt(num)
# raiz = math.sqrt(num)
print('A raiz de seu numero é {:.2f}'.format(raiz))
print('A raiz de seu numero arredondado para baixo é {:.2f}'.format(floor(raiz)))
print('Olha que legal o numero aleatório da biblioteca ramdom: {}'.format(nran))
# print(emoji.emojize("Olá mundo :earth_americas:", use_aliases=True))
