import calendar
ano = int(input('Qual ano deseja verificar se é bissexto? '))
mes = 2
fistday, ndaysmonth = calendar.monthrange(ano, mes)
if ndaysmonth == 29:
    print('o ano de {} é bissexto!'.format(ano))
else:
    print('o ano de {} não é bissexto!'.format(ano))
print('----- Fim Execução -----')