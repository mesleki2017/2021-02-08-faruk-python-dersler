import matplotlib.pyplot as plt
from matplotlib import animation
from numpy import random
import numpy as np
import matplotlib

liste22 = [64, 34, 25, 12, 22, 11, 90]
liste2 = random.randint(5000, size=(200))

fig = plt.figure()

aaa = len(liste2)
xxx = np.arange(len(liste2))
grafik1 = plt.bar(xxx, liste2)


def bubbleSort(i, arr):
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
                    b.set_height(arr[i])
        return arr


# Driver code to test above

anim = animation.FuncAnimation(fig, bubbleSort, fargs=[
                               liste2], interval=50)

plt.show()
