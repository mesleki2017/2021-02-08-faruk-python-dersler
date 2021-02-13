import pandas as pd
import quandl

dataframe1 = quandl.get("LBMA/GOLD")

print(dataframe1)

dataframe1.to_csv("altin_fiyat.csv", encoding='utf-8', index=True)
