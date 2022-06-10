km = float(input('Qual a quantidade percorrida? km '))
dia = float(input('Qual a quantidade de dias de permanencia com o veiculo? '))
k = km * 0.15
d = dia * 60
total = k + d
print('Sabendo que foi alugado por {:.0f}dias e rodou {:.2f}km o valor do aluguel fica '
      'em R${:.2f}'
      .format(dia, km, total))
