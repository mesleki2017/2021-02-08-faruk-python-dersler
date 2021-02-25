
def en_buyuk_sayiyi_bul(liste, tarama_index_araligi):
    en_buyuk_sayi = 0
    for i in range(0, tarama_index_araligi):
        if liste[i] > en_buyuk_sayi:
            en_buyuk_sayi = liste[i]
            index = i
    return en_buyuk_sayi, index


#liste1 = [38, 99, 888, 787, 98, 1555]

#print(en_buyuk_sayiyi_bul(liste1, 0))
