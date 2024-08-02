#Exercício Python 13: 
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salário = float(input('digite o valor do salário em R$ : '))
novo = salário + (salário * 15 / 100)
print('O valor de novo salario é {:.2f}'.format(novo))