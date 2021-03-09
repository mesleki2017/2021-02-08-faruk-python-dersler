import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

N = 15

A = np.random.rand(N,N)
im = plt.imshow(A)

def updatefig(*args):
    im.set_array(np.random.rand(N,N))
    return im,

ani = animation.FuncAnimation(fig, updatefig, frames=10, interval=200, blit=True) 

plt.show()