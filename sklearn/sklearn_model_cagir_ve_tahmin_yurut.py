import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn import utils
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import numpy

# daha once egittigimiz model dosyasini cagirma
model = joblib.load(r"sklearn\sinus_egri_makina_ogrenmesi_1.joblib")

# model ile tahminde bulunma
prediction = model.predict([[3], [3.1]])


lab_enc = preprocessing.LabelEncoder()
# daha once model kayit sirasinda kayit ettigimiz
# encoder dosyasini cagirma buarada classes.npy
lab_enc.classes_ = numpy.load('classes.npy')


print(lab_enc.inverse_transform((prediction)))
