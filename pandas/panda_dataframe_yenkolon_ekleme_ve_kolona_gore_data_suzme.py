import pandas as pd

data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}
print("data type =>", type(data))
print(data)

df = pd.DataFrame(data, dtype=float)

print(df)

# dataframe e yeni kolon ekleme,ilk data bu bilgiler yoktu
df["armut"] = [88, 33, 55, 66]
print(df)

# dataframe den istenilen kolonlari suzme
print(df[["apples", "armut"]])
