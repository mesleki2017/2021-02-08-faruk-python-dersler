import pandas as pd
import quandl

# quandl bir online data sagliyici
# https://www.quandl.com/data/LBMA/GOLD-Gold-Price-London-Fixing

dataframe1 = quandl.get("LBMA/GOLD")

print(dataframe1)


# https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file
dataframe1.to_csv("altin_fiyat.csv", encoding='utf-8', index=True)
