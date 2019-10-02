# -*- coding: utf8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

fig, ax = plt.subplots()

def update(i):
    a = np.ones(100) * random.random() * 0.5
    b = np.ones(100) * random.random() * 0.5
    c = np.ones(100) * random.random() * 0.5

    x = np.linspace(1, 10, 100)
    y = c * np.sin(b * x - a)

    ax.clear()
    ax.set_xlim(1, 10)
    ax.set_ylim(-1, 1)
    g, = ax.plot(x, y)

    return g, ax

anim = FuncAnimation(fig, update, frames=np.arange(1, 20), interval=200)

# anim.save('line.gif', dpi=80, writer='imagemagick')

plt.show()