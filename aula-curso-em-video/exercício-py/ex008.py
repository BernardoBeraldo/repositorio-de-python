# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('digite médida em metros: '))
mm = m * 100
cm = m * 10
m = m 
dm = m * 10
dam = m * 100
hm = m / 1000
km = m / 10000
print('as medidas mm = {} \n cm = {} \n m = {} \n dm = {} \n dam = {} \n hm = {} \n km = {}s '.format(mm, cm, m, dm, dam, hm, km))