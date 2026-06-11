import numpy as np

# Foco no Ingrediente X:
# 60x + 40y = 26
# 50x + 30y = 20
A = np.array([[60, 40], [50, 30]])
B = np.array([26, 20])

X = np.linalg.solve(A, B)
x, y = X[0], X[1]

print(f"Ingrediente X no composto A: {x:.2f} unid/L")
print(f"Ingrediente X no composto B: {y:.2f} unid/L")

unidades_x = 70 * x + 50 * y
print(f"\nQtd de X em 70L de A e 50L de B: {unidades_x:.2f} unidades")