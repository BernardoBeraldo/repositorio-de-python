'''Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.  
 Calcule e mostre o comprimento da hipotenusa.'''
import math
cateto_adjacente = float(input('digite o valor do cateto adjacente : '))
cateto_oposto = float(input('digite o valor do cateto oposto : '))
h = cateto_adjacente * cateto_oposto 
print('a hipotenusa é {}'.format(h,))