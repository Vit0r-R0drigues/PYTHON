#Programa que ler varios numeros aleaatorios e armazena-los em uma lista. Depois disso printa tudo em ordem não PODENDO USAR O SORT.

lista = []

for i in range(0, 5):
    n = float(input('pense em um numero aleatorio: '))
    if i == 0:
        lista.append(n)
    elif n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('-'*30)
print(f'Os numeros digitados foram: {lista}')
print('-'*30)
