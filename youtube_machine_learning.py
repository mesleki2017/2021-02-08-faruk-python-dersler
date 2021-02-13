# https://www.youtube.com/watch?v=lN5jesocJjk&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v&index=3

import pandas as pd
import quandl
import math

#dataframe1 = quandl.get("WIKI/GOOGL")
df = pd.read_csv('google_stock_price.csv')

# dataframe onizleme
# print(df.head())

# data suzme
#print(df[["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume"]])

# df deki diger datalari kullanmigacayiz o yuzden df ye suzdugumuz kolonlari tekrar atadik
df = df[["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume"]]

# df de yeni bir kolon tanimlayip hisse en yuksekfiyat ile kapanis fiyati arasindaki farki yuzde olarak atayalim
df["HL_PCT"] = (df["Adj. High"]-df["Adj. Close"])/df["Adj. Close"]*100.0
print(df.head())


# df de yeni bir kolon tanimlayip hisse acilis fiyatı-kapanis fiyati arasindaki farki yuzde olarak atayalim
df["PCT_change"] = (df["Adj. Close"]-df["Adj. Open"])/df["Adj. Open"]*100.0
print(df.head())

# tekrar dataframe istedigimiz datalara indirgeyelim
# df =df ile suzlmus datayi df ye atamis oluyoruz
df = df[["Adj. Close", "HL_PCT", "PCT_change", "Adj. Volume"]]
print(df.head())

# degisken olusturduk
forecast_col = "Adj. Close"

# bos veri leri -9999 sayisi ile doldurmak
df.fillna(-9999, inplace=True)

# bu kismi anlamadim
forecast_out = int(math.ceil(0.01*len(df)))
print("forecast_out => ", forecast_out)

# yeni bir kolon ekliyoruz ve shift ne ise yariyor bilmiyorum
df["label"] = df[forecast_col].shift(-forecast_out)

df.dropna(inplace=True)

print(df.head())
