#_author_: Matas Kulikauskas

#imports:
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

plt.title('Figure 18.15 (Earthshine)')
plt.xlabel('Earth phase angle (deg.)')
plt.ylabel('Polarization degree (%)')

vx1 = [49.1025641, 60.38461538, 71.66666667, 83.84615385, 95.76923077]
vy1 = [4.2, 6.311111111, 7.377777778, 7.6, 7.533333333]
yerr1 = [0.555555556, 0.666666667, 0.622222222, 0.533333333, 0.4]

plt.errorbar(vx1, vy1, yerr1, fmt='o', capsize=5)

vx2 = [48.97435897, 60.38461538, 71.66666667, 83.71794872, 95.76923077]
vy2 = [2.866666667, 4.333333333, 5.4, 6, 6.088888889]
yerr2 = [0.288888889, 0.555555556, 0.6, 0.46666666666666, 0.377777778]

plt.errorbar(vx2, vy2, yerr2, fmt='^', capsize=5)

vx3 = [48.97435897, 60.51282051, 71.79487179, 83.84615385, 95.8974359]
vy3 = [2.2, 2.8, 3.866666667, 4.933333333, 5.377777778]
yerr3 = [0.33333333, 0.377777778, 0.355555555, 0.311111111, 0.222222222]

plt.errorbar(vx3, vy3, yerr3, fmt='s', capsize=5)

lx1 = [49.1025641, 60.38461538, 71.66666667, 83.84615385, 95.76923077]
ly1 = [4.2, 6.311111111, 7.377777778, 7.6, 7.533333333]

xnewone = np.linspace(49.1025641, 95.76923077, num=100000,
endpoint=True)
f1 = interp1d(lx1, ly1, kind='cubic')
plt.plot(xnewone, f1(xnewone))

lx2 = [48.97435897, 60.38461538, 71.66666667, 83.71794872, 95.76923077]
ly2 = [2.866666667, 4.333333333, 5.4, 6, 6.088888889]

xnewtwo = np.linspace(48.97435897, 95.76923077, num=100000,
endpoint=True)
f2 = interp1d(lx2, ly2, kind='cubic')
plt.plot(xnewtwo, f2(xnewtwo))

lx3 = [48.97435897, 60.51282051, 71.79487179, 83.84615385, 95.8974359]
ly3 = [2.2, 2.8, 3.866666667, 4.933333333, 5.377777778]

xnewthree = np.linspace(48.97435897, 95.8974359, num=100000,
endpoint=True)
f3 = interp1d(lx3, ly3, kind='cubic')
plt.plot(xnewthree, f3(xnewthree))

a = np.asarray([vx1, vy1])
b = np.asarray([yerr1])
c = np.asarray([vx2, vy2])
d = np.asarray([yerr2])
e = np.asarray([vx3, vy3])
f = np.asarray([yerr3])
g = np.asarray([lx1, ly1])
h = np.asarray([lx2, ly2])
i = np.asarray([lx3, ly3])

np.savetxt("18_15_csv's/18_15_eb1.csv", a , delimiter=",", fmt='%f')
np.savetxt("18_15_csv's/18_15_yerr1.csv", b, delimiter=",", fmt='%f')
np.savetxt("18_15_csv's/18_15_eb2.csv", c , delimiter=",", fmt='%f')
np.savetxt("18_15_csv's/18_15_yerr2.csv", d, delimiter=",", fmt='%f')
np.savetxt("18_15_csv's/18_15_eb3.csv", e , delimiter=",", fmt='%f')
np.savetxt("18_15_csv's/18_15_yerr3.csv", f, delimiter=",", fmt='%f')
np.savetxt("18_15_csv's/18_15_l1.csv", g , delimiter=",", fmt='%f')
np.savetxt("18_15_csv's/18_15_l2.csv", h, delimiter=",", fmt='%f')
np.savetxt("18_15_csv's/18_15_l3.csv", i, delimiter=",", fmt='%f')

plt.axvline(x=90)

plt.show()
