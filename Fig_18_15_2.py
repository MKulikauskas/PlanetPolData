#_author_: Matas Kulikauskas

#imports:
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

plt.grid(True)

xnewone = np.linspace(49.1025641, 95.76923077, num=100000,
endpoint=True)
f1 = interp1d(x=[49.1025641, 60.38461538, 71.66666667, 83.84615385,
95.76923077], y=[4.2, 6.311111111, 7.377777778, 7.6,
7.533333333], kind='cubic')
#yerr=[0.555555556, 0.666666667, 0.622222222, 0.533333333, 0.4]
plt.plot(xnewone, f1(xnewone))

xnewtwo = np.linspace(48.97435897, 95.76923077, num=100000,
endpoint=True)
f2 = interp1d(x=[48.97435897, 60.38461538, 71.66666667, 83.71794872,
95.76923077], y=[2.866666667, 4.333333333, 5.4, 6,
6.088888889], kind='cubic')
#yerr=[0.288888889, 0.555555556, 0.6, 0.46666666666666, 0.377777778]
plt.plot(xnewtwo, f2(xnewtwo))


xnewthree = np.linspace(48.97435897, 95.8974359, num=100000,
endpoint=True)
f3 = interp1d(x=[48.97435897, 60.51282051, 71.79487179, 83.84615385,
95.8974359], y=[2.2, 2.8, 3.866666667, 4.933333333,
5.377777778], kind='cubic')
#yerr=[0.33333333, 0.377777778, 0.355555555, 0.311111111, 0.222222222]
plt.plot(xnewthree, f3(xnewthree))


plt.show()
