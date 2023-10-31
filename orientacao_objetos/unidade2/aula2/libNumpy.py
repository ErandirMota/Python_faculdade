import numpy as np

numeros = [10, 12, 3, 4, 5, 6, 7, 8]

soma = 0

for n in numeros:
  soma += n

media = soma / len(numeros)
print("Média na mão:", media)

array_numeros = np.array(numeros)

media = np.mean(array_numeros)
print("Média com numpy:", media)