#Exercício Python 17: 
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.  
#Calcule e mostre o comprimento da hipotenusa.
import math
ca = float(input('digite o valor do cateto adjacente : '))
co = float(input('digite o valor do cateto oposto : '))
hi = math.hypot(co , ca)
print('a hipotenusa é {}'.format(hi,))