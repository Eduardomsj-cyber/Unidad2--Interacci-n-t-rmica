import numpy as np

# Definir la matriz A de coeficientes
A = np.array([
    [2, -3, 4, -1, 5, -1, 2, -1, 3, -2],
    [-3, 2, 5, -1, 4, 2, -3, 1, -2, 5],
    [4, -1, 3, 2, -3, 1, -2, 5, -4, 1],
    [-1, 5, -2, 3, 4, -1, 2, -3, 1, -5],
    [3, -2, 5, -1, 4, 2, -3, 1, -5, 2],
    [-2, 4, -3, 1, 5, -1, 2, -4, 3, -1],
    [5, -1, 2, -3, 4, 1, -2, 3, -1, 4],
    [1, -3, 4, -2, 5, -1, 2, -1, 4, -3],
    [2, 3, -1, 4, -2, 5, -3, 1, -2, 1],
    [-3, 2, 4, -1, 3, -2, 5, -1, 1, -4]
])

# Definir el vector b de resultados
b = np.array([11, -10, 8, -6, 7, -3, 9, -5, 6, -8])

# Resolver el sistema de ecuaciones
x = np.linalg.solve(A, b)

# Mostrar los resultados
print("Las soluciones para las incógnitas son:")
for i in range(len(x)):
    print(f"x{i+1} = {x[i]}")
