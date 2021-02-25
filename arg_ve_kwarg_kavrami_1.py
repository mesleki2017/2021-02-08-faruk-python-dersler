
def arg_ve_kwarg_anlama(*aaa, **bbb):
    print(aaa[0])
    print(aaa[1])
    print(bbb["elma"])
    print(bbb["armut"])


try:
    arg_ve_kwarg_anlama(1, 4, elma=55, armut=33)
    print("1-----------------------------------")
except:
    print("hata1")
    print("1-----------------------------------")


try:
    arg_ve_kwarg_anlama(1, 4, 6, elma=55, armut=33)
    print("2-----------------------------------")
except:
    print("hata2")
    print("2-----------------------------------")

try:
    arg_ve_kwarg_anlama(1, 4, 6, kiraz=55, armut=33)
    print("3-----------------------------------")
except:
    print("hata3")
    print("3-----------------------------------")

try:
    arg_ve_kwarg_anlama(1, 4, 6, 100, "tttt", elma="var", armut="yok")
    print("4-----------------------------------")
except:
    print("hata4")
    print("4-----------------------------------")


def arg_ve_kwarg_listele(*liste_gir, **dictionary_gir):
    for iii in liste_gir:
        print(iii)
    print("++++++++++++++++")
    for ttt in dictionary_gir:
        print(ttt)
    print("++++++++++++++++")
    for ttt in dictionary_gir.values():
        print(ttt)
    print("++++++++++++++++")
    for xxx, yyy in dictionary_gir.items():
        print(xxx, " = ", yyy)


# https://www.w3schools.com/python/gloss_python_loop_dictionary_items.asp
print("-----------------------------------------------------")
arg_ve_kwarg_listele(12, 33, 45, "son1", elma=1, armut=2, kiraz="yok")
