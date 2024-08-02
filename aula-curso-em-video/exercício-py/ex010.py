# Exercício Python 10: 
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
n = float(input('digite um valor em real: '))
d = n / 5.44
e = n / 5.91
print('o valor  em real  {} em dolar {}'.format(n,d))
print('o valor em real {} em euro {}'.format(n,e))