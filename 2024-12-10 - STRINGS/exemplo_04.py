'''
   EXEMPLO 04:
   Fazer um programa em que o usuário informe uma palavra e em seguida
   o programa exiba a palavra invertida e diga se ela é um palíndromo ou não.
'''

palavra = input("Informe uma palavra: ")

palavraInv = ""
for i in range(len(palavra)-1, -1, -1):
    palavraInv += palavra[i]
     

if palavra == palavraInv: print(f"A palavra {palavra} é um palindromo")

else: print(f"A palavra {palavra} não é um palindromo")
