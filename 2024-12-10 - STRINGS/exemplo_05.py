'''
   EXEMPLO 05:
   Fazer um programa em que o usuário informe uma string e depois uma palavra
   e em seguida o programa informe se a palavra informada está na string informada
'''

frase = input("Digite uma frase: ")

palavra = input("Digite uma palavra: ")

if palavra in frase: print(f"A string {palavra} está na frase: {frase}")
else : print(f"A string {palavra} não está na frase: {frase}")