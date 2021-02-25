import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.gca()

x = np.arange(5)
y = np.random.rand(5)

bars = ax.bar(x, y, color='grey', linewidth=4.0)

bars.remove()
x2 = np.arange(10)
y2 = np.random.rand(10)
ax.bar(x2, y2)
plt.show()
