# https://www.youtube.com/watch?v=lN5jesocJjk&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v&index=3

import pandas as pd
import quandl
import math
import numpy as np
# https://stackoverflow.com/questions/30667525/importerror-no-module-named-sklearn-cross-validation
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

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

# print(df.head())

# video part4----------------------------------------------------------------------------------------------------

print("-----------------------------------------------------------------------")
X = np.array(df.drop(["label"], 1))
y = np.array(df["label"])
print(X)
print("-----------------------------------------------------------------------")


X = preprocessing.scale(X)
print(X)
#X = X[:-forecast_out+1]
df.dropna(inplace=True)
y = np.array(df["label"])

print(len(X), len(y))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)

# video part5----------------------------------------------------------------------------------------------------
# https://www.youtube.com/watch?v=QLVMqwpOLPk&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v&index=5
