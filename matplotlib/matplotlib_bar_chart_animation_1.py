import matplotlib.pyplot as plt
from matplotlib import animation
from numpy import random
import numpy as np


def barlist():
    y = random.randint(100, size=(40))
    return y


fig = plt.figure()

n = 100  # Number of frames
x = np.linspace(0, 39, 40)
barcollection = plt.bar(x, barlist())


def animate(i):
    y = barlist()
    for i, b in enumerate(barcollection):
        b.set_height(y[i])
        print(i)
    print("---------------------------")


anim = animation.FuncAnimation(fig, animate, repeat=False, blit=False, frames=3,
                               interval=1000)

print("sssssssssssssssssssssssssss")
plt.show()
