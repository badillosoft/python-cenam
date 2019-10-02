# -*- coding: utf8 -*-
import numpy as np

# TODO: Crear un vector `u` con 20 entradas entre (-1, 1)
u = np.linspace(-1, 1, 20)

# TODO: Crear un vector `v` con 10 entradas entre (-5, 5)
v = np.linspace(-5, 5, 10)

# TODO: Crear una matriz `A` de 10x20 con la siguiente ecuación:

# A[i][j] = v[i] * u[j] - cos(u[j]) * sin(v[i])
# para `i` los índices de 0 a 9 y `j` los índices de 0 a 19

# A se conoce como la matriz cruzada de la malla de la función f(vi, uj)
# descrita por Aij

A = np.zeros((10, 20)) # Creamos una matriz vacía de 10x20

from math import cos, sin

for i in range(0, 10): # 1 Eje de la matriz 10x20 (10)
    for j in range(0, 20): # 2 Eje de la matriz 10x20 (20)
        A[i][j] = v[i] * u[j] - cos(u[j]) * sin(v[i])

print(u)
print(v)
print(A)

import matplotlib.pyplot as plt

plt.contourf(u, v, A)

plt.show()