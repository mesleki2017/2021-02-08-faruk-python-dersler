

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

print("-----------------------------------------------------")

arg_ve_kwarg_listele(12, 33, 45, "son1", elma=[
                     1, "a101"], armut=2, kiraz="yok")
