import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn import utils
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import numpy as np
import pandas as pd

time = np.arange(4, 8, 0.01)
dict = {"zaman": time}
data_frame1 = pd.DataFrame(dict)


# daha once egittigimiz model dosyasini cagirma
model = joblib.load("sinus_egri_makina_ogrenmesi_1.joblib")

# model ile tahminde bulunma
# dataframde ki giris verisi 10 dan buyukse yanlis sonuclar veriyor
# cunku modeli egitirken 0 ile 10 arasi datalarla egitim  yapmistik
prediction = model.predict(data_frame1)

# daha once model kayit sirasinda kayit ettigimiz
# encoder dosyasini cagirma buarada classes.npy
lab_enc = preprocessing.LabelEncoder()
lab_enc.classes_ = np.load('classes.npy')

print(lab_enc.inverse_transform((prediction)))
