
def deneme(*aaa, **bbb):
    print(aaa[0])
    print(aaa[1])
    print(bbb["elma"])
    print(bbb["armut"])


try:
    deneme(1, 4, elma=55, armut=33)
    print("1-----------------------------------")
except:
    print("hata1")
    print("1-----------------------------------")


try:
    deneme(1, 4, 6, elma=55, armut=33)
    print("2-----------------------------------")
except:
    print("hata2")
    print("2-----------------------------------")

try:
    deneme(1, 4, 6, kiraz=55, armut=33)
    print("3-----------------------------------")
except:
    print("hata3")
    print("3-----------------------------------")

try:
    deneme(1, 4, 6, 100, "tttt", elma="var", armut="yok")
    print("4-----------------------------------")
except:
    print("hata4")
    print("4-----------------------------------")

# https://www.w3schools.com/python/gloss_python_loop_dictionary_items.asp


def deneme2(*zzz, **rrr):
    for iii in zzz:
        print(iii)
    print("++++++++++++++++")
    for ttt in rrr:
        print(ttt)
    print("++++++++++++++++")
    for ttt in rrr.values():
        print(ttt)
    print("++++++++++++++++")
    for xxx, yyy in rrr.items():
        print(xxx, " = ", yyy)


print("-----------------------------------------------------")
deneme2(12, 33, 45, "son1", elma=1, armut=2, kiraz="yok")
