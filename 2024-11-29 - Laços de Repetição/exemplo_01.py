'''
   Fazer um programa que fique solicitando ao usuário para digitar um número
   inteiro e informe se o número é par ou ímpar. 
   
   O programa só deve encerrar quando o usuário digitar o número 0.

'''
while True:
   n = int(input("Digite um número inteiro: "))
   if n == 0: break
   elif n % 2 == 0:
       print(f"O {n} é um número par")
   else: print(f"O {n} é um número impar")