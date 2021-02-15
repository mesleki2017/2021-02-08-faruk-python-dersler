import pandas as pd
df = pd.DataFrame({'harf': ["a", "b", "c"], 'sayi': [4, 5, 6]})

# pandas ta satir secme
satir0 = df.loc[[1]]
print(satir0)
print("-------------------------")

# pandas ta satir secme diger yontem
satir1 = df[1:2]
print(satir1)
print("-------------------------")

# pandas ta kolonu listeye atama
liste1 = df['harf'].tolist()
print(type(liste1), liste1)
print("-------------------------")

# pandasta satiri listeye atama
liste2 = df[1:2].values.tolist()
print(type(liste2), liste2)


# https://stackoverflow.com/questions/16096627/selecting-a-row-of-pandas-series-dataframe-by-integer-index
