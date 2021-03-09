#https://stackoverflow.com/questions/43326680/what-are-the-differences-between-add-axes-and-add-subplot

import matplotlib.pyplot as plt
import numpy as np

# Some example data to display
x = np.linspace(0, 4 * np.pi, 400)
y = np.sin(x ** 2)

fig = plt.figure()


ax = fig.add_axes([0,0,1,1])




ax.plot(np.sin(x))


plt.show()