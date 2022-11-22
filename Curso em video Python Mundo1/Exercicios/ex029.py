vel = int(input('Qual velocidade voce estava mesmo?'))
if vel > 80:
    mul = float((vel - 80) * 7)
    print('Voce estava acima da velocidade... {}Km/h é muito'.format(vel))
    print('A multa é de: R${:2}'.format(mul))
print('... Era Só Isso ...')