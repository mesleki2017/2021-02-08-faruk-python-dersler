<<<<<<< HEAD
import matplotlib.pyplot as plt
from matplotlib import animation
from numpy import random
import numpy as np
import matplotlib

from en_buyuk_sayi1 import en_buyuk_sayiyi_bul


# iste1 = [38, 2150, 888, 787, 98, 99, 786, 200, 2000]
liste2 = random.randint(5000, size=(200))
=======
#https://stackoverflow.com/questions/43326680/what-are-the-differences-between-add-axes-and-add-subplot

import matplotlib.pyplot as plt
import numpy as np

# Some example data to display
x = np.linspace(0, 4 * np.pi, 400)
y = np.sin(x ** 2)
>>>>>>> ff56ef3fc11c6ac6620e142e52452911473cc4d7

fig = plt.figure()


<<<<<<< HEAD
aaa = len(liste2)
xxx = np.arange(len(liste2))
bbb = np.zeros(len(liste2), dtype=int)
grafik1 = plt.bar(xxx, liste2)


# i neden var bilmiyorum i olmadan calismiyor
def deneme1(i, listegir):
    global aaa
    if aaa == 1:
        return

    enBuyukSAyi = en_buyuk_sayiyi_bul(listegir, aaa)

    aaa = aaa-1

    gecici1 = listegir[aaa]
    listegir[aaa] = enBuyukSAyi[0]
    listegir[enBuyukSAyi[1]] = gecici1

    for i, b in enumerate(grafik1):
        b.set_height(listegir[i])


anim = animation.FuncAnimation(fig, deneme1, fargs=[
                               liste2], interval=50)

plt.show()
=======
ax = fig.add_axes([0,0,1,1])




ax.plot(np.sin(x))


plt.show()
>>>>>>> ff56ef3fc11c6ac6620e142e52452911473cc4d7
