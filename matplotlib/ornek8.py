import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def data_olustur(zaman=0):
    cnt = 0
    while cnt < 1000:
        cnt += 1
        zaman += 0.1
        yield zaman, np.sin(2*np.pi*zaman) * np.exp(-zaman/10.)


def baslangic_durumu():
    eksenler.set_ylim(-1.1, 1.1)
    eksenler.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

cizim, eksenler = plt.subplots()
line, = eksenler.plot([], [], lw=2)
eksenler.grid()
xdata, ydata = [], []


def cizime_basla(data):

    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = eksenler.get_xlim()

    if t >= xmax:
        eksenler.set_xlim(xmin, 2*xmax)
        eksenler.figure.canvas.draw()
    line.set_data(xdata, ydata)
	
    return line,

ani = animation.FuncAnimation(cizim, cizime_basla, data_olustur, blit=False, interval=60,
                              repeat=False, init_func=baslangic_durumu)
plt.show()
