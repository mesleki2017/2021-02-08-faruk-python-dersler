import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


df = pd.read_csv('altin_fiyat.csv')


x = df['Date']
y = df["USD (AM)"]

# # plot
plt.plot(x, y)
# # beautify the x-labels
plt.gcf().autofmt_xdate()

plt.show()
