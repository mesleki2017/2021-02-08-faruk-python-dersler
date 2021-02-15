# https://jakevdp.github.io/PythonDataScienceHandbook/05.06-linear-regression.html
# begendim

from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

# https://matplotlib.org/3.1.1/gallery/style_sheets/ggplot.html
# https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html
plt.style.use('dark_background')
plt.grid()

poly_model = make_pipeline(PolynomialFeatures(7),
                           LinearRegression())

rng = np.random.RandomState(1)
x_train = 10 * rng.rand(50)
y_train = np.sin(x_train) + 0.1 * rng.randn(50)
plt.scatter(x_train, y_train, color='red')  # scatter nokta nokta cizim demek

print("----------------------------------------------------------------")
# model egitme fit ile
poly_model.fit(x_train[:, np.newaxis], y_train)

print("----------------------------------------------------------------")
xfit = np.linspace(0, 10, 20)
print(xfit)
print(xfit[:, np.newaxis])
yfit = poly_model.predict(xfit[:, np.newaxis])
plt.plot(xfit, yfit, color='blue')

print("----------------------------------------------------------------")
# xfit[:, np.newaxis] analamadigim icin  asagidaki kod yazdim
# bir yukarda xfit linspacele olusturulup xfit[:, np.newaxis] ile uygun formata donusturuluyor
# uygun format asagida elle yazdigim xxxfit format imis
xxxfit = [[0.], [1.], [2.], [3.], [4.], [5.],
          [6.], [7.], [8.], [9.], [10.], [11.]]
yyyyfit = poly_model.predict(xxxfit)
plt.plot(xxxfit, yyyyfit, color='darkorange')

print("----------------------------------------------------------------")
plt.show()
