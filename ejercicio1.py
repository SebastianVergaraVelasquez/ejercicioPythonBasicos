import random

numeros = []
for i in range(10):
    valorAleatorio = random.randint(0,10)
    numeros.append(valorAleatorio)
    print(f'{numeros[i]}')

print('Orden ascendente')
ordenAscendente = sorted(numeros)
print (f"{ordenAscendente}")
print('Orden descendente')
ordenDescendente = sorted(numeros, reverse=True)
print (f"{ordenDescendente}")