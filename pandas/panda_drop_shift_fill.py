import pandas as pd

# Create a DataFrame from List of Dicts
data = [{'elma': 1, 'armut': 2}, {'karpuz': 5,
                                  'armut': 10, "elma": 20}, {"aaa": 11, "bbb": 22}]
print(type(data))
print(type(data[0]))

print("---------------------------------------------------")
df = pd.DataFrame(data)
print(df)
print("---------------------------------------------------")

df.fillna(-9999, inplace=True)
print(df)
print("---------------------------------------------------")

# https://www.geeksforgeeks.org/python-pandas-dataframe-shift/
# karpuz kolonu degerlerini yukardan asagi shift kadar kaydirip
# yeni kolon olan label a atar
df["label"] = df["karpuz"].shift(2)
print(df)
print("---------------------------------------------------")

# https://www.w3resource.com/pandas/dataframe/dataframe-dropna.php
df.dropna(inplace=True)
print(df)
print("---------------------------------------------------")
