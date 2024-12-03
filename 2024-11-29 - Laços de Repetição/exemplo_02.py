'''
   Fazer um programa que fique lendo números inteiros solicitados ao usuário.

   Quando o usuário digitar 0, o programa deve finalizar e imprimir a soma de 
   todos os números digitados bem como a média aritmética.

   O valor 0 não deve entrar na média.
'''

count = 0
m = 0
while True:
   n = int(input("Digite um número diferente de 0: "))
   if n == 0:
      break
   m += n
   count += 1
print(f"A soma de todos os número foi {m} e a média aritimética é {m/count}")
