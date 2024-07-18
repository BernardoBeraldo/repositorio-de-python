#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
num = float(input('digite um numero com ponto (ex 4.5 458.6): '))
num_inteiro = trunc(num)
print('O numero {} e sua  porção Inteirado numero  é {}'.format(num, num_inteiro))