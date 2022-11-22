sal = int(input('Qual o seu salario? '))
if sal > 1250:
    nsal = (sal + (sal * 0.10))
    print('O aumento vai ser de R${:.2f}'.format(nsal))
else:
    nsal2 = (sal + (sal * 0.15))
    print('O aumento vai ser de R${:.2f}'.format(nsal2))
print('----- Fim Execução -----')