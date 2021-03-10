
#https://www.python-course.eu/recursive_functions.php
#https://towardsdatascience.com/dont-use-recursion-in-python-any-more-918aad95094c
#https://stackoverflow.com/questions/30214531/basics-of-recursion-in-python

# faktoriyal alma fonksiyonunu recursive mantigi ile yapma
def fonksiyonumuz111(n):
    # n=1 ise fonksiyondan cik
    if n == 1:
        print (n)
        return 1

    # Recursive  demek tekrar return ile fonksiyona donmek demek
    # n 1 degilse n-1 yapip fonnksiyonu tekrar calistir
    else:
        print (n)
        return n * fonksiyonumuz111(n-1)

print(fonksiyonumuz111(5))

print("------------------------------------------------------")
#baska bir ornek

def liste_topla(liste,index,sonuc):
    if index==len(liste):
        return sonuc
    return liste_topla(liste,index+1,sonuc+liste[index])

liste1=[12,3,5]

print(liste_topla(liste1,0,0))
