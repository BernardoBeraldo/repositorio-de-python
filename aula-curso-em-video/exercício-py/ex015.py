#Exercício Python 15: 
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e 
# a quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar, sabendo que
# o carro custa R$60 por dia e R$0,15 por Km rodado.
distancia = float(input('Quantos Km foi precorido :  '))
diaria = float(input('Quantos dia voce usou o carro: '))
km = distancia * 0.15
diaria =  diaria * 60
pagar = km + diaria
print('o valor e de {}'.format(pagar))

