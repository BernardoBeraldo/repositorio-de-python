# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input('digite a largura da parede  em metros : '))
altura = float(input('digite a altura  da parede em metros : '))
# para pintar 2m² de parede vai 1  litro de pinta #
base = (altura * largura)
tinta = (2 * base ) / 2
print('Para pintar uma parede {} m² voce presisa de {} litros de pintas'.format(base, tinta))