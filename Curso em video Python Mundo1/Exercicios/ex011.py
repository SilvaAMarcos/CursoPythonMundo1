alt = float(input('Qual a Altura da parede? '))
lar = float(input('Qual a Largura da parede? '))
area = alt * lar
quant = area / 2
print('A área da sua parede é de {:.2f}m² e gasta {:.2f}L de tinta !!!'.format(area, quant))