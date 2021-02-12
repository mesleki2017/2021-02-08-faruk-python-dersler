import numpy as np

list1 = [1, 2, 3, 4, 5, 6]
list2 = [10, 9, 8, 7, 6, 5]

try:
    print(list1*list2)
except:
    print("hata olustu")
    print("python listeleri direkt olarak carpilamaz")
    print("fakat bu listeleri numpt array cevirip bu carpmayi yapabiliriz")

print("----------------------------------------------------------------")
# Convert list1 into a NumPy array
a1 = np.array(list1)

# Convert list2 into a NumPy array
a2 = np.array(list2)

print(a1*a2)
