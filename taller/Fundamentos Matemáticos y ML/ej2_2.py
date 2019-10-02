# -*- coding: utf8 -*-
# pip install --upgrade matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

N = 100
M = 200

u = np.linspace(-1, 1, M)
v = np.linspace(-5, 5, N)

X, Y = np.meshgrid(u, v)

A = X * Y + np.cos(X) * np.sin(Y)
# A = np.exp(-X**2 -Y**2)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(X, Y, A, cmap="rainbow")
plt.show()