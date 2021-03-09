import matplotlib.pyplot as plt
import numpy as np

fig11,a =  plt.subplots(2,2)

x = np.arange(1,5,0.1)

a[0][0].plot(x,x*x)
a[0][0].set_title('square')

a[0][1].plot(x,np.sqrt(x))
a[0][1].set_title('square root')

a[1][0].plot(x,np.exp(x))
a[1][0].set_title('exp')

a[1][1].plot(x,np.log10(x))
a[1][1].set_title('log')

plt.show()