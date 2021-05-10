# -*- coding: utf8 -*-

import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


df = pd.read_csv('data/dolarkur.csv')

print(df.head())
print(df["Geçerli Olduğu Tarih"])
# print(df["USD (AM)"])

# https://stackoverflow.com/questions/42372617/how-to-plot-csv-data-using-matplotlib-and-pandas-in-python
df['Geçerli Olduğu Tarih'] = df['Geçerli Olduğu Tarih'].map(lambda x: datetime.strptime(str(x), '%d.%m.%Y'))

x = df['Geçerli Olduğu Tarih']
y = df["Döviz Alış"]

# # plot
plt.grid()
plt.plot(x, y)
# # beautify the x-labels
plt.gcf().autofmt_xdate()

plt.show()