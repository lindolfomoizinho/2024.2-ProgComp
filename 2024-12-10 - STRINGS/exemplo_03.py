'''
   EXEMPLO 03:
   Fazer um programa em que o usuário informe uma string e em seguida
   o programa informe quantas palavras existem na string digitada
'''

frase = input("Informe uma frase: ")

posicao = 0
palavras = 0

while posicao < len(frase):
   if frase[posicao] == " " and frase[posicao - 1] != " ":
      palavras += 1
   posicao += 1  
   
if frase[-1] != " ": palavras += 1

print(f"A quantidade de palavras é {palavras}")