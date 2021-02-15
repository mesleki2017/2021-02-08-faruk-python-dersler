from en_buyuk_sayi import en_buyuk_sayiyi_bul

liste1 = [38, 1555, 888, 787, 98, 99]


def listeyi_buyukten_kucuge_sirala(liste_gir):
    liste_gecici = []
    liste_sirali = []
    liste_gecici = liste1
    for aaa in range(0, len(liste1)):
        enBuyukSAyi = en_buyuk_sayiyi_bul(liste_gecici)
        if enBuyukSAyi != None:
            liste_sirali.append(enBuyukSAyi)
            liste_gecici.remove(enBuyukSAyi)
    return liste_sirali


print("sirasiz liste => ", liste1)
print("sirali liste => ", listeyi_buyukten_kucuge_sirala(liste1))
