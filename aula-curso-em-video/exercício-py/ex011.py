altura = float(input('digite a altura  da parede em metros : '))
largura = float(input('digite a largura da parede  em metros : '))
# para pintar 2m² de parede vai 1  litro de pinta #
base = (altura * largura)
tinta = (2 * base ) / 2
print('Para pintar uma parede {} m² voce presisa de {} litros de pintas'.format(base, tinta))