from random import randint
import time

lista = [] 



while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    r = str(input('Deseja continuar? [S/N] ')).upper()
    if r in 'Nn':
        break

lista.sort()

aleatorio = randint(0, len(lista))

print('-='*30)  
print(f'{"Processando...":^60}')
print('-='*30)
time.sleep(2)

print(f'A lista completa é {lista}')

print(f'A lista completa é {lista}')

print('-='*30)
print('Números na lista com suas colocações:')
for i, num in enumerate(lista):
    print(f'{i + 1}º: {num}')

if aleatorio in lista:
    print(f'O número {aleatorio} está contido dentro da lista na posição {lista.index(aleatorio) + 1}')
else:
    print(f'O número {aleatorio} não está contido dentro da lista')




