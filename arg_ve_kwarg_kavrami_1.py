
def arg_ve_kwarg_anlama(*aaa, **bbb):
    print(aaa[0])
    print(aaa[1])
    print(bbb["elma"])
    print(bbb["armut"])


try:
    arg_ve_kwarg_anlama(1, 4, elma=55, armut=33)
    print("1--------------1---------------------")
except:
    print("hata1")
    print("--------------1---------------------")


try:
    arg_ve_kwarg_anlama(1, 4, 6, elma=55, armut=33)
    print("--------------2---------------------")
except:
    print("hata2")
    print("--------------2---------------------")

try:
    arg_ve_kwarg_anlama(1, 4, 6, kiraz=55, armut=33)
    print("--------------3---------------------")
except:
    print("hata3")
    print("--------------3---------------------")

try:
    arg_ve_kwarg_anlama(1, 4, 6, 100, "tttt", elma="var", armut="yok")
    print("--------------4---------------------")
except:
    print("hata4")
    print("--------------4---------------------")
