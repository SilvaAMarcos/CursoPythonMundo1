viagem = int(input('Quantos Km foi a sua viagem? '))
if viagem <= 200:
    n1 = viagem * 0.5
    print('O valor da viagem de {}Km é R${:.2f}'.format(viagem, n1))
else:
    n2 = viagem * 0.45
    print('O valor da viagem de {}Km é R${:.2f}'.format(viagem, n2))
print('----- Fim Execução -----')
