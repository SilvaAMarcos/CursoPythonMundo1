from math import radians, sin, cos, tan
ang = float(input('Informe o angulo '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O angulo {:.0f}º representado em seno é {:.3f} em cosseno é {:.3f} '
      'e tangente é {:.3f} '
      .format(ang, sen, cos, tan))
