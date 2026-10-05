import numpy as np
import matplotlib.pyplot as plt
import timeit
import nonlinear_mass_faster as nlm
import scipy.optimize as op
from scipy.special import gamma
import math
plt.ion()
plt.show()
b1 = np.loadtxt('pklin/default.txt')
a1 = 0.3096
a2 = 1.686
b2 = np.linspace(0,5,4e4+1)
b3 = np.linspace(0,2,100)
b4 = b3[1]-b3[0]
b5 = b3 * b3 * nlm.kernel(b3)
b6 = nlm.pk_to_xi(b1[:,0], b1[:,1], b2)
b7 = lambda x: np.interp(x, b2, b6)
b8 = np.linspace(0,6,61)
b9 = np.interp(1.0, b1[:,0], b1[:,1], left=np.nan, right=np.nan)
b10 = nlm.sigma2_prefactor(-2, b9)
b11 = open('fiducial_rnl.txt','w')
b11.write('
for j,z in enumerate(b8):
	b12 = nlm.growth_factor(z, a1)
	b13 = op.brentq(lambda R: nlm.sigma_pl(b10, -2, R) - a2/b12, 0.01, 8.0)
	if z > 5 or b13 < 0:
		a3 = 0.01
	else:
		a3 = b13
	b14 = op.brentq(lambda R: nlm.sigma_Pk(R,b1[:,0],np.log(b1[:,0]),b1[:,1]) - a2/b12, 0, 5)
	b11.write('%.2f %15.10f\n' % (z, b14))
b11.close()