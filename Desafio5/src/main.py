import numpy as np
import random

# Exercicio 1: Matriz 3x3 com numeros aleatorios
print("Exercicio 1 - Matriz Aleatoria:")
matriz1 = []
for i in range(3):
    linha = []
    for j in range(3):
        n = random.randint(1, 10)
        linha.append(n) 
    matriz1.append(linha) 

for l in matriz1:
    print(l)

# Exercicio 2: Somar duas matrizes de vendas
print("\nExercicio 2 - Soma de Vendas:")
vendas1 = [[10, 20], [30, 40]]
vendas2 = [[5, 5], [10, 10]]
resultado_soma = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        
        resultado_soma[i][j] = vendas1[i][j] + vendas2[i][j]
print("Soma total:", resultado_soma)

# Exercicio 3: Media de notas usando NumPy
print("\nExercicio 3 - Media de Alunos:")

notas = np.array([[7.0, 8.0, 9.0], [5.0, 6.0, 7.0]])
media_aluno1 = (notas[0][0] + notas[0][1] + notas[0][2]) / 3 
media_aluno2 = (notas[1][0] + notas[1][1] + notas[1][2]) / 3
print("Media do Aluno 1:", round(media_aluno1, 2))
print("Media do Aluno 2:", round(media_aluno2, 2))

# Exercicio 4: Ver se o determinante e zero
print("\nExercicio 4 - Determinante:")
matriz_det = np.array([[2, 4], [1, 3]])
valor_det = np.linalg.det(matriz_det) 
print("O determinante deu:", round(valor_det, 2))
if valor_det != 0:
    print("Como nao e zero, a matriz tem inversa.") 

# Exercicio 5: Transposta e total de estoque
print("\nExercicio 5 - Transposta e Estoque:")
estoque = np.array([[10, 20, 30], [5, 10, 15]])
transposta = estoque.T 
print("Matriz Transposta:\n", transposta)