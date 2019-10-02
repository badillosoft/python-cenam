# -*- coding:utf8 -*-

import numpy as np

# Vector de N entradas de 0 a N - 1
x = np.arange(10)
print(x)

# Vector de A hasta B - 1 (A=20, B=30)
x = np.arange(20, 30)
print(x)

# Vector de N entradas de ceros
x = np.zeros(10)
print(x)

# Vector de N entradas de unos
x = np.ones(10)
print(x)

# Vector de N entradas aleatorias entre 0 y menor a 1
x = np.random.rand(10)
print(x)

# Vector de N entradas aleatorias uniformes entre A y B (B exclusivo)
x = np.random.uniform(5, 9, 10) # A=5, B=9, N=10
print(x)

# Vector de N entradas aleatorias bajo una distribución normal
# centrada en Mu con Desviación Tetha
x = np.random.normal(3, 2, 10) # Mu=3, Tetha=2, N=10
print(x)

print(np.mean(x))
print(np.std(x))

# Vector de N entradas igualmente distribuidas (equidistantes) entre sí
x = np.linspace(-10, 10, 11) # A=-10, B=10, N=11
print(x)

# Vector de N entradas a partir de una lista de python
x = np.array([1, 4, 6, 8, 10])
print(x)

# Operaciones entre arreglos

a = np.array([1., 2., 3.])
b = np.array([4., 6., 9.])

# Operaciones entrada-entrada (operaciones directas)
print(a + b)
print(a - b)
print(a * b)
print(a / b) # Cuidado con números enteros

# Operación vector-escalar
print(10 * a)
print(a * 10)
print(a / 10)

# Operaciones matemáticas entre vectores

a = np.array([1, 2, 3])
b = np.array([1, -2, 3])

print(np.dot(a, b)) # cos(t) = a . b / (|a| * |b|)

print(np.linalg.norm(a)) # raíz de a[0]^2 + a[1]^2 + a[2]^2
print(np.linalg.norm(b))

import math

t = math.acos(np.dot(a, b) / ( np.linalg.norm(a) * np.linalg.norm(b) ))
print(t * 180 / math.pi)

# https://docs.scipy.org/doc/numpy/reference/routines.linalg.html

# Funciones matemáticas en vectores

t = np.linspace(-np.pi, np.pi, 21)

x = np.cos(t)
y = np.sin(t)

print(t)
print(x)
print(y)

import matplotlib.pyplot as plt

fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(nrows=2, ncols=2)

ax1.plot(t, x)
ax2.plot(t, y)
ax3.plot(x, y)

plt.show()

t = np.linspace(0, 2 * np.pi, 100)

I = np.ones(100)

a = 30
x = 2 * a * (I - np.cos(t)) * np.cos(t)
y = 2 * a * (I - np.cos(t)) * np.sin(t)

plt.clf()

fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(nrows=2, ncols=2)

ax1.plot(t, x)
ax2.plot(t, y)
ax3.plot(x, y)

plt.show()