# bu ornek iki kutle arasindaki cekimi newton kutle cekim yasasina gore hesapliyor
# ve grafik ciziyor
import matplotlib.pyplot as plt

def draw_graph(x, y):
	plt.plot(x, y, marker='o')
	plt.xlabel('mesfe/metre')
	plt.ylabel('kutle cekim kuvveti / newton')
	plt.title('kutle cekim kuvveti mesafe iliskisi')
	plt.show()

def grafik():
	# 100 den baslayarak 10 de bir nokta olustur 501 e kadar
	# 100 metrede 150 metrede 200 metrede gibi
	r = range(100, 501, 10)
	# F listesini bosal F
	F = []
	# kutle cekim sabiti, G
	G = 6.674*(10**-11)
	# iki kutle kg olarak
	m1 = 0.5
	m2 = 1.5
	# kuvveti hesapla ve  F listesine ekle,
	# niye liste diyor bilmiyorum
	for dist in r:
		force = G*(m1*m2)/(dist**2)
		F.append(force)
		
	draw_graph(r, F)

	

grafik()