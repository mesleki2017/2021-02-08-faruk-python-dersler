import matplotlib.pyplot as plt
from matplotlib import animation
from numpy import random
import numpy as np
import matplotlib
from en_buyuk_sayi1 import en_buyuk_sayiyi_bul

liste22 = [64, 34, 25, 12, 22, 11, 90]
liste2 = random.randint(5000, size=(40))
liste1 = liste2


fig, ax = plt.subplots(2, 2)

aaa = len(liste2)
xxx = np.arange(len(liste2))
grafik1 = ax[1, 0].bar(xxx, liste2)
grafik2 = ax[0, 0].bar(xxx, liste1)


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                for i, b in enumerate(grafik1):
                    # b.set_height(arr[i])
                    b.set_height(i*10)


def deneme1(listegir):
    global aaa
    if aaa == 1:
        return

    enBuyukSAyi = en_buyuk_sayiyi_bul(listegir, aaa)

    aaa = aaa-1

    gecici1 = listegir[aaa]
    listegir[aaa] = enBuyukSAyi[0]
    listegir[enBuyukSAyi[1]] = gecici1

    for i, bc in enumerate(grafik2):
        bc.set_height(listegir[i])

# Driver code to test above


def deneme2(i, listegir1, listegir2):
    deneme1(listegir1)
    bubbleSort(listegir2)


anim = animation.FuncAnimation(fig, deneme2, fargs=[
                               liste1, liste2], interval=500)


plt.show()
