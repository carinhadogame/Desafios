import numpy as np

# 5x + 3y = 110
# 8x + 2y = 100
A = np.array([[5, 3], [8, 2]])
B = np.array([110, 100])

X = np.linalg.solve(A, B)
x, y = X[0], X[1]

print(f"Taxa por trabalhador (x): {x:.2f} itens/dia")
print(f"Taxa por máquina (y): {y:.2f} itens/dia")

prod_nova = 10 * x + 4 * y
print(f"Produção (10 trab, 4 maq): {prod_nova:.2f} itens")

# Verificação pedida pelo professor
print("\nVerificação:")
print(f"Eq 1: 5*({x:.0f}) + 3*({y:.0f}) = {5*x + 3*y:.0f}")
print(f"Eq 2: 8*({x:.0f}) + 2*({y:.0f}) = {8*x + 2*y:.0f}")