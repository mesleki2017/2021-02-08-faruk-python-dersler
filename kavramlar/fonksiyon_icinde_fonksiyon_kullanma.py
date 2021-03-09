#https://stackoverflow.com/questions/6289646/python-function-as-a-function-argument
def g111(a,b):

    print(a+b)
    
def f111(func,*degerler):
    func(*degerler)
          
f111(g111,5,6)

#veya aynı programi *arg siz yapabiliriz

def t222(a,b):
    print(a+b)

def h222(fonksiyon111,a,b):
    fonksiyon111(a,b)

h222(t222,4,9)