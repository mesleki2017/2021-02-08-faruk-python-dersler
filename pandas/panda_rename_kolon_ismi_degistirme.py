# import pandas library
import pandas as pd

# dictionary den pandas dataframe olusturma
dict111 = {
    'isim': ['Ahmet', 'Mehmet', 'Ali', 'Fatma'],
    'yas': [23, 21, 22, 21],
    'universite': ['gazi', 'odtu', 'itu', 'selcuk'],
}

# dataframe olusturma
df111 = pd.DataFrame(dict111)

print(df111)

print("--------------------------------------------- \n")

df111 = df111.rename(columns={"isim": "isimler", "yas": "yaslar"})

print(df111)

# https://stackoverflow.com/questions/11346283/renaming-columns-in-pandas
