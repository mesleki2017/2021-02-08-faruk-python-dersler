import pandas as pd

data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}
print("data type =>", type(data))
print(data)

purchases = pd.DataFrame(data, dtype=float)

print(purchases)

purchases = pd.DataFrame(data, dtype=int)

print(purchases)

purchases = pd.DataFrame(data, index=["aaa", "bbb", "ccc", "ddd"], dtype=float)

print(purchases)
