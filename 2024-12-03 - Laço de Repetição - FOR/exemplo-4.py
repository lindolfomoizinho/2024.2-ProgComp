'''
    Exemplo 04: Faça um progama que solicite ao usuário um valor 
    inteiro positivo (n) e imprima os n primeiros números inteiros primos.
'''
import sys

n = int(input("Dígite um número inteiro maior que 0: "))

if n <= 0:
    sys.exit("O número digitado é inválido")
else:
    count = 0  
    num = 2 

    while count < n:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
            count += 1
        num += 1