import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


df = pd.read_csv('altin_fiyat.csv')
# print(df["Date"])
# print(df["USD (AM)"])

# https://stackoverflow.com/questions/42372617/how-to-plot-csv-data-using-matplotlib-and-pandas-in-python
df['Date'] = df['Date'].map(
    lambda x: datetime.strptime(str(x), '%Y-%m-%d'))

x = df['Date']
y = df["USD (AM)"]

# # plot
plt.grid()
plt.plot(x, y)
# # beautify the x-labels
plt.gcf().autofmt_xdate()

plt.show()
