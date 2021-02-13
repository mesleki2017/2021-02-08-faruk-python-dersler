
import pandas as pd

liste1 = [[12, 33], ["cesur", "bulent"]]
print("data type =>", type(liste1))
print(liste1)
print("----------------------------------------------------------------------------")
datam1 = pd.DataFrame(liste1, dtype=float)
print(datam1)
print("----------------------------------------------------------------------------")
# listeyi daha mantikli hale getirip
liste2 = [["Bulent Cesur", 535], ["Ahmet Aydin", 542]]
datam2 = pd.DataFrame(liste2, dtype=int)
print(datam2)
print("----------------------------------------------------------------------------")
datam3 = pd.DataFrame(liste2, columns=["isim-soyad", "Tel"], dtype=int)
print(datam3)
