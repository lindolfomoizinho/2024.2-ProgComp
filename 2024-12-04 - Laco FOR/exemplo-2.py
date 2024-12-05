'''
   Faça um programa que solicite ao usuário um valor n inteiro positivo e 
   imprima os n primeiros trios de valores que formam um triângulo pitagórico.
'''
import sys

num = int(input("Digite um número inteiro positivo: "))

if num <= 0:
    sys.exit("Número inválido")
else:
    count = 0
    a = 1
    while count < num:
        b = a
        while b <= 100:
            c = b
            while c <= 100:
                if a**2 + b**2 == c**2:
                    print(f"A = {a}, B={b} e C={c}")
                    count += 1
                    if count == num : break
                c += 1
            if count == num : break
            b += 1
        if count == num: break
        a += 1
