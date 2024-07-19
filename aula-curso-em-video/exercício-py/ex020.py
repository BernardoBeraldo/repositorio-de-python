#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a1 = (input('aluno 1 ; '))
a2 = (input('aluno 2 ; '))
a3 = (input('aluno 3 ; '))
a4 = (input('aluno 4 ; '))
lista = [a1,a2,a3,a4]
random.shuffle(lista)
print('a order de apresentaçâo ')
print(lista)
