import matplotlib.pyplot as plt

grafik_datam = open('matplotlib/data1.txt','r').read()

noktalar = grafik_datam.split('\n')
#'\n' new line demek veya enter la bir alt satira gecmis olmak demek

print (noktalar)

#['1,5', '2,7', '8,99', '6,7', '99,10', '12,5']
#suanda noktalar da olan data

for nokta in noktalar:
    print (nokta ," noktalarimiz belli ancak formatlari =>", type(nokta))

#bu string formatindaki noktalai integera cevirmemiz gerekiyor
#vede x ekseni ve y ekseni olarak ayirmamiz gerekiyor

xekseni=[]
yekseni=[]

for nokta in noktalar:

    xy=nokta.split(",")

    print (xy[0],"---",xy[1])
    
    xekseni.append(xy[0])
    yekseni.append(xy[1])

print (xekseni)
print (yekseni)
print(type(xekseni[0]))
#degerler strinde olsa matplotlib cizimi yapabildi
#illaki sayiya cevirmeye gerek yok mu ?


plt.plot(xekseni,yekseni)

plt.show()