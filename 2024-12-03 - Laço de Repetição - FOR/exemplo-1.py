'''
   Exemplo 01: Laço de Repetição com For
'''

multiplicador = int(input('Digite o multiplicador: '))

print(f'Tabuada de {multiplicador}:')

for multiplicando in range(1,11):
   print(f'{multiplicador} x {multiplicando} = {multiplicador * multiplicando}')
   multiplicando += 1

print('Fim da tabuada.')