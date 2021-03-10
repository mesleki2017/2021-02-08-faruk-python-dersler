import dis

def test(*xxx, **yyy):
    print (xxx)
    print (yyy)

test(1, 2, a=3, b=4)

print(dis.dis(test))