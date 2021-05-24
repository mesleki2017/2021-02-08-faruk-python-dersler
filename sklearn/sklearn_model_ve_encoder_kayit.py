import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn import utils
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import numpy

data = pd.read_csv(r"sklearn\file2.csv")

xxx = data.drop(columns="genlik")
yyy = data["genlik"]

# cikisi yani y i, sklearn in istediği formata cevirmek icin
# labelencoder kullaniliyor.
lab_enc = preprocessing.LabelEncoder()
y_encoded = lab_enc.fit_transform(yyy)

# bu labelencode uda daha sonra kullanabilmek icin
# yani egittigimiz modelden data aldigimizda decode edebilmek icin
# kayit etmemiz gerekiyor.
numpy.save('classes.npy', lab_enc.classes_)

# datamizi train ve test olaraj 2 ye boluyoruz 0.8 ve 0.2 oranla
x_train, x_test, y_encoded_train, y_encoded_test = train_test_split(
    xxx, y_encoded, test_size=0.2)

# model objesini olusturup fit ile egitiyoruz
model = DecisionTreeClassifier()
model.fit(x_train, y_encoded_train)

# modeli egittikten sonra joblib dosyasi olarak kayit ettik
# daha sonra bu modeli kullanabilmek icin. yani her seferinde
# modeli egitmemize gerek yok
joblib.dump(model, "sinus_egri_makina_ogrenmesi_1.joblib")

prediction = model.predict(x_test)

# -----------------------------------------
# print(prediction)
# score = accuracy_score(y_encoded_test, prediction)
# print(score)
# -----------------------------------------

# tahminleri inverse.transforme ile decode ediyoruz
print(lab_enc.inverse_transform((prediction)))
