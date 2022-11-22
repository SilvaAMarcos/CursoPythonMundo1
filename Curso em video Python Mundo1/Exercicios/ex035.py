# programa le tres retas e verifica qual é a hipotenusa e atibui os outros dois como catetos
# pra verificar se pode ser um tiangulo
r1 = int(input('Qual o valor da primeira reta? '))
r2 = int(input('Qual o valor da segunda reta? '))
r3 = int(input('Qual o valor da terceira reta? '))

hip = r1
cat1 = r2
cat2 = r3
if r2 > hip:
    hip = r2
    cat1 = r1
    cat2 = r3
if r3 > hip:
    hip = r3
    cat1 = r1
    cat2 = r2

if (cat1 ^ 2) + (cat2 ^ 2) == hip ^ 2:
    print('Ele pode ser um triagulo')
else:
    print('Ele não pode ser um triangulo')
print('----- Fim Execução -----')
