pre = float(input('Qual o valor do produto? ' ))
des = pre * 0.05
new = pre - des
print('O valor do produto atual é R${:.2f} com desconto fica no valor de: R${:.2f}'.format(pre, new))
