# -*- coding: utf8 -*-

import numpy as np

# f - campana de gauss
def f(x):
    return np.exp(-(x - 1) ** 2) # x^2 => x ** 2

x = np.linspace(-1, 1, 20)
y = f(x)

import matplotlib.pyplot as plt

# TODO: Dibujar la gráfica de (x, y)
plt.plot(x, y)
plt.show()

N = 100
h = 0.05
xn = np.ones(1) * 0.001

for i in range(N):
    fp = (f(xn + h) - f(xn)) / h
    xn = xn - f(xn) / fp

print(xn)
print(f(xn))

# TODO: Dibujar la gráfica de (xn, f(xn))
