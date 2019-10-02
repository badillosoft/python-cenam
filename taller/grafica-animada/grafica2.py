# -*- coding: utf8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import random

fig = plt.figure()

def update(i):
    N = 100
    M = 200

    a = (i - 1)

    u = np.linspace(-1, 1, M)
    v = np.linspace(-5, 5, N)

    X, Y = np.meshgrid(u, v)

    A = X * Y + a * np.cos(X) * np.sin(Y)
    # A = np.exp(-X**2 -Y**2)

    ax = plt.axes(projection='3d')

    g = ax.plot_surface(X, Y, A, cmap="rainbow")

    return g, ax

anim = FuncAnimation(fig, update, frames=np.arange(1, 20), interval=200)

# anim.save('line.gif', dpi=80, writer='imagemagick')

plt.show()