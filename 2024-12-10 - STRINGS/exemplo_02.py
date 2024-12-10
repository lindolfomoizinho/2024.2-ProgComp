'''
   EXEMPLO 02:
   Fazer um programa em que o usuário informe uma string e em seguida
   o programa informe quantas vogais existem na string digitada
'''
frase = input("Informe uma frase: ")

qtVog = 0

for letra in frase:
    if letra.lower() in "aeiou":
        qtVog += 1

print(f"A quantidade de vogais é {qtVog}")