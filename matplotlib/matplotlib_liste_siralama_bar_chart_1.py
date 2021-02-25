import matplotlib.pyplot as plt
from matplotlib import animation
from numpy import random
import numpy as np
from time import sleep
import matplotlib
from en_buyuk_sayi1 import en_buyuk_sayiyi_bul


matplotlib.use('TKAgg')

liste1 = [38, 2150, 888, 787, 98, 99, 786, 200, 2000]

fig = plt.figure()
win = fig.canvas.manager.window


def deneme(i, listegir):
    x = np.arange(6)
    listegir[0] = listegir[0]+50
    grafik1 = plt.bar(x, listegir)
    print(listegir)


aaa = len(liste1)
xxx = np.arange(len(liste1))
bbb = np.zeros(len(liste1), dtype=int)


def deneme1(i, listegir):
    global aaa
    global xxx
    global bbb
    if aaa == 1:
        return
    enBuyukSAyi = en_buyuk_sayiyi_bul(listegir, aaa)
    print("enBuyukSAyi =>", enBuyukSAyi, "  aaa =>", aaa)
    if enBuyukSAyi[0] == None:
        print("ok")

    aaa = aaa-1

    gecici1 = listegir[aaa]
    listegir[aaa] = enBuyukSAyi[0]
    listegir[enBuyukSAyi[1]] = gecici1

    grafik1 = plt.bar(xxx, listegir)
    grafik1 = plt.bar(xxx, bbb)
    print(listegir)


anim = animation.FuncAnimation(fig, deneme1, fargs=[
                               liste1], blit=False, frames=4, interval=1000)

print("sssssssssssssssssssssssssss")
plt.show()
