sal = float(input('Por favor informe o salário do funcionário: '))
saln = sal + (sal * 0.13)
print('O salário R${:.2f} reajustado ficará com o valor de R${:.2f}'.format(sal, saln))