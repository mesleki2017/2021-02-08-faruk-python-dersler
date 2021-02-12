

liste1 = [38, 1555, 888, 787, 98, 99]


def en_buyuk_sayiyi_bul(liste):
    en_buyuk_sayi = 0
    for i in range(0, len(liste)):
        if liste[i] > en_buyuk_sayi:
            en_buyuk_sayi = liste[i]
    return en_buyuk_sayi


print(en_buyuk_sayiyi_bul(liste1))
