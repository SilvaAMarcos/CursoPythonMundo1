v = float(input('Digita os metros logo: '))
km = v / 1000
hm = v / 100
dam = v / 10
dm = v * 10
print('O valor {:.2f} convertido em CM fica: {:.0f}cm \nE convertido em MM fica: {:.0f}mm'.format(v, v*100, v*1000))
print('Outros valores: km{:.3f} hm{:.2f} dam{:.2f} dm{:.2f}'.format(km, hm, dam, dm))
