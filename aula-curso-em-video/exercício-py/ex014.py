#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
temperaturac = float(input('digite uma temperatura em °c :  '))
tFahrenheit = temperaturac * 1.8 + 32
tkelvin = temperaturac + 273.15

print('A temperatura em °c {} ,°f {} e  K{}: '.format(temperaturac, tFahrenheit, tkelvin))