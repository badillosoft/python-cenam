# -*- coding: utf8 -*-

# Las matrices tienen dos dimensiones (alto y ancho)
# Las dimensiones en numpy se consideran como la figura del arreglo
# En numpy todos los objetos son arreglos re-figurados por dimensión

import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(A)

# np.arange(1, 7) -> [1, 2, 3, 4, 5, 6]
# .reshape((2, 3)) -> [[1, 2, 3], [4, 5, 6]]
A = np.arange(1, 7).reshape((2, 3))

print(A)

A = np.ones((4, 7))

print(A)

print(A.shape) # (4, 7) significa 2 dimensiones de tamaño 4 y 7

# Pregunta:

# Dada una imagen de canales de color RGB de 28x28 pixeles
# 1. ¿Cuántas dimensiones tiene? R: 3 dimensiones
# 2. ¿Cada dimensión que tamaño tendría? R: (28, 28, 3)
# 3. Crea un objeto equivalente a la imagen con numpy

I = np.random.randint(0, 256, (28, 28, 3))

print(I)

import matplotlib.pyplot as plt

plt.imshow(I)
plt.show()

R = I[:,:,0]
rows, cols = R.shape
Rp = np.zeros(I.shape)
for row in range(rows):
    for col in range(cols):
        Rp[row][col] = np.array([R[row][col], 0, 0])
G = I[:,:,1]
Gp = np.zeros(I.shape)
for row in range(rows):
    for col in range(cols):
        Gp[row][col] = np.array([0, G[row][col], 0])
B = I[:,:,2]
Bp = np.zeros(I.shape)
for row in range(rows):
    for col in range(cols):
        Bp[row][col] = np.array([0, 0, B[row][col]])
    
Xp = np.zeros(I.shape)
for row in range(rows):
    for col in range(cols):
        r = R[row][col]
        g = G[row][col]
        b = B[row][col]
        pixel = int(512 * r / (1 + g + b))
        Xp[row][col] = np.array(pixel)

plt.imshow(Rp)
plt.show()
plt.imshow(Gp)
plt.show()
plt.imshow(Bp)
plt.show()
plt.imshow(Xp)
plt.show()

