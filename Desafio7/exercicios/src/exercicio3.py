import numpy as np

# 50x + 20y = 30
# 30x + 30y = 12
A = np.array([[50, 20], [30, 30]])
B = np.array([30, 12])

X = np.linalg.solve(A, B)
farinha_pao = X[0]
acucar_bolo = X[1]

print(f"Farinha por pão: {farinha_pao:.2f} kg")
print(f"Açúcar por bolo: {acucar_bolo:.2f} kg")

gasto_farinha = 40 * farinha_pao + 25 * acucar_bolo 
gasto_acucar = 40 * farinha_pao + 25 * acucar_bolo 

print(f"\nPara 40 pães e 25 bolos:")
print(f"Farinha necessária: {gasto_farinha:.2f} kg")
print(f"Açúcar necessário: {gasto_acucar:.2f} kg")