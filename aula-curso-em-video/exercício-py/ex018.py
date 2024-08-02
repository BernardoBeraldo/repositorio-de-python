#Exercício Python 18:
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
num = float(input('digite um numero '))
con = math.cos(num)
sen = math.sin(num)
tan = math.tan(num)
print('os valores de cos: {:.3f} sin: {:.3f} tan: {:.3f}'.format(con, sen, tan))