#https://stackoverflow.com/questions/8954746/python-arguments-as-a-dictionary

#For non-keyworded arguments, use a single *, and for keyworded arguments, use a **.
#Non-keyworded arguments would be unpacked to a tuple and keyworded arguments would be unpacked to a dictionary

def test(*xxx, **yyy):
    print (xxx)
    print (yyy)

test(1, 2, a=3, b=4)
