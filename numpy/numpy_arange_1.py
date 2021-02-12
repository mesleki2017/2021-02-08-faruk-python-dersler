
import numpy as np
import math

print("math.pi =>", math.pi)
print("np.pi   =>", np.pi)

print("------------------------------------------------------")
# arange(start=None, stop=None, step=None, dtype=None,*, like=None)

zaman_orneklemi = np.arange(start=-10, stop=10, step=1)
print(zaman_orneklemi)

print("------------------------------------------------------")

genlik = np.sin(zaman_orneklemi)
print(genlik)

print("------------------------------------------------------")
