# https://scikit-learn.org/stable/auto_examples/linear_model/plot_bayesian_ridge_curvefit.html
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import BayesianRidge


def func(x): return np.sin(2*np.pi*x)


print("func = ", func(3))
# #############################################################################
# Generate sinusoidal data with noise
x_train = np.linspace(0., 1., 100)
y_train = func(x_train)
x_test = [2, 3]
# #############################################################################
# Fit by cubic polynomial
n_order = 3
X_train = np.vander(x_train, n_order + 1, increasing=True)
X_test = np.vander(x_test, n_order + 1, increasing=True)
# #############################################################################
print(X_test)

reg = BayesianRidge(tol=1e-6, fit_intercept=False, compute_score=True)
init = [1., 1e-3]
reg.set_params(alpha_init=init[0], lambda_init=init[1])
reg.fit(X_train, y_train)
ymean, ystd = reg.predict(X_test, return_std=True)
print(ymean, "----", ystd)
