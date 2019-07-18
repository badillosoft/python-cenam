import matplotlib.pyplot as plt
import numpy as np
import time

while True:
    x = np.linspace(1, 10, 20)
    y = x + np.random.uniform(-1, 1, 20)
    plt.plot(x, y)
    plt.show()
    time.sleep(1)