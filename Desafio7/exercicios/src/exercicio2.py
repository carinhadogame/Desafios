import numpy as np

A = np.array([[4, 2, 3], 
              [3, 3, 2], 
              [5, 1, 4]])
B = np.array([150, 140, 160])

if abs(np.linalg.det(A)) < 1e-10:
    print("A matriz não pode ser invertida.")
else:
    X = np.linalg.solve(A, B)
    x, y, z = X[0], X[1], X[2]
    
    print(f"Trabalhador (x): {x:.2f}")
    print(f"Máquina (y): {y:.2f}")
    print(f"Hora (z): {z:.2f}")
    
    prod = 6 * x + 3 * y + 5 * z
    print(f"\nProdução (6 trab, 3 maq, 5h): {prod:.2f} itens")