'''
   Faça um programa que solicite um valor n inteiro positivo e 
   imprima na tela o seguinte padrão:

   para n = 4

   o programa deverá imprimir

   1
   2 2
   3 3 3
   4 4 4 4
'''
import sys

num = int(input("Digite um número inteiro positivo: "))

if num <= 0:
    sys.exit("Número inválido")
else:
    for i in range(1, num + 1 ):
        print(" ")
        for j in range(1, i+1):
            print(i, end=" ")