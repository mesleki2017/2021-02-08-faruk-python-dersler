# import pandas library
import pandas as pd

# dictionary with list object in values
dict111 = {
    'isim': ['Ahmet', 'Mehmet', 'Ali', 'Fatma'],
    'yas': [23, 21, 22, 21],
    'universite': ['gazi', 'odtu', 'itu', 'selcuk'],
}

# creating a Dataframe object
df111 = pd.DataFrame(dict111)

print(df111)

print("------------------------------")

df111 = df111.drop([0, 1])

print(df111)

# https://www.w3resource.com/pandas/dataframe/dataframe-drop.php
