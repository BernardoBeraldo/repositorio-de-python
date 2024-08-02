#Exercício Python 12: 
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.# 
preço = float(input('digite o valor de um  produto R$  '))
novo = preço - (preço * 5 / 100)
print('o valor de do produto é de R$ {:.2f} e com o descosconto custara  5% R${:.2f/} '.format(preço, novo ))