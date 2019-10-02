# -*- coding: utf8 -*-
import numpy as np
from math import cos, sin

N = 100
M = 200

u = np.linspace(-1, 1, M)
v = np.linspace(-5, 5, N)

A = np.zeros((N, M))

for i in range(0, N):
    for j in range(0, M):
        A[i][j] = v[i] * u[j] - cos(u[j]) * sin(v[i])

import matplotlib.pyplot as plt

plt.contourf(u, v, A, cmap="rainbow")
plt.show()