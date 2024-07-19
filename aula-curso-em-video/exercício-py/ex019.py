#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
a1 = str(input('digite o nome de um aluno; '))
a2 = str(input('digite o nome de um aluno; '))
a3 = str(input('digite o nome de um aluno; '))
a4 =  str(input('digite o nome de um aluno; '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno sortiado foi {}'.format(escolhido))