import random
import numpy as np


print("--- Metodo 1: Usando a biblioteca random ---")
matriz = []
linhas = 3
colunas = 3

for i in range(linhas):
    nova_linha = []
    for j in range(colunas):
        n_aleatorio = random.randint(0, 9)
        nova_linha.append(n_aleatorio)
    matriz.append(nova_linha)

for linha in matriz:
    print(linha)

print("\n" + "-"*30 + "\n")

 
print("--- Metodo 2: Usando NumPy ---")

min_v = 0
max_v = 10 

matriz_np = np.random.randint(min_v, max_v, size=(3, 3))

print(matriz_np)