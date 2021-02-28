# import pandas library
import pandas as pd

print("eeee")
# dictionary with list object in values
dict111 = {
    'isim': ['Ahmet', 'Mehmet', 'Ali', 'Fatma'],
    'yas': [23, 21, 22, 21],
    'universite': ['gazi', 'odtu', 'itu', 'selcuk'],
}

# creating a Dataframe object
#df = pd.DataFrame(dict111,columns = ['Name','Age','University'], index = ['a', 'b', 'c', 'd'])
df = pd.DataFrame(dict111)

print("kkk", df)
