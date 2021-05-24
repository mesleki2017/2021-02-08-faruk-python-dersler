import pandas as pd

from sklearn.tree import DecisionTreeClassifier

from sklearn import preprocessing
from sklearn import utils

data = pd.read_csv(r"sklearn\file1.csv")


x = data.drop(columns="genlik")
y = data["genlik"]
lab_enc = preprocessing.LabelEncoder()
encoded = lab_enc.fit_transform(y)
print(y)
print(encoded)
model = DecisionTreeClassifier()
model.fit(x, encoded)
prediction = model.predict([[2, 2]])

print(lab_enc.inverse_transform((prediction)))
