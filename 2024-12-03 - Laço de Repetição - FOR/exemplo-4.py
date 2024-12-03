'''
    Exemplo 04: Faça um progama que solicite ao usuário um valor 
    inteiro positivo (n) e imprima os n primeiros números inteiros primos.
'''
import sys

n = int(input("Dígite um número inteiro maior que 0: "))

if n <= 0:
    sys.exc_info("O número digitado é inválido")

for atual in range(1, n + 1):
    for numero in range(atual, atual + 1):
        if atual % numero != 0:
            print(numero)
            break