'''
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostreExercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

 * O nome com todas as letras maiúsculas e minúsculas.
 Quantas letras ao todo (sem considerar espaços).
 Quantas letras tem o primeiro nome.

 '''
nome = str(input('digite um nome : ')).strip()
print('seu nome em maiúscula {}'.format(nome.upper()))
print('seu nome em minúsculas {}'.format(nome.lower()))
print('seu nome tem {} caracteres'.format(len(nome)-nome.count(' ')))
print('o seu primeiro nome tem {} letras '.format(nome.find(' '))),