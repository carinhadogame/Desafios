import numpy as np

A = []
print("Digite os valores da matriz A (3x3):")
for i in range(3):
    linha = [
        float(input(f"A[{i}][0]: ")), 
        float(input(f"A[{i}][1]: ")), 
        float(input(f"A[{i}][2]: "))
    ]
    A.append(linha)

B = []
print("\nDigite os valores do vetor B:")
for i in range(3):
    B.append(float(input(f"B[{i}]: ")))

A = np.array(A)
B = np.array(B)

try:
    det = np.linalg.det(A)
    # Verifica se o determinante é muito próximo de zero
    if abs(det) < 1e-10: 
        print("\nErro: Determinante zero. Sistema não tem solução única.")
    else:
        X = np.linalg.solve(A, B)
        print("\nMatriz A:")
        print(A)
        print("\nVetor B:", B)
        print("\nSolução:")
        print(f"x = {X[0]:.2f}, y = {X[1]:.2f}, z = {X[2]:.2f}")
except np.linalg.LinAlgError:
    print("\nErro ao resolver: Matriz singular.")