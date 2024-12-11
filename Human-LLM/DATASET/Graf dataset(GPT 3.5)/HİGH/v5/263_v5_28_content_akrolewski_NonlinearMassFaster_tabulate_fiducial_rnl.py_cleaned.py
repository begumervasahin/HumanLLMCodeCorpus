import numpy as np
import matplotlib.pyplot as plt
import nonlinear_mass_faster as nlm
import scipy.optimize as op
plt.ion()
plt.show()
b1 = np.loadtxt('pklin/default.txt')
a1 = 0.3096
a2 = 1.686
b2 = np.linspace(0, 5, int(4e4) + 1)
b3 = np.linspace(0, 2, 100)
b4 = b3[1] - b3[0]
b5 = b3 * b3 * nlm.kernel(b3)
b6 = nlm.pk_to_xi(b1[:, 0], b1[:, 1], b2)
b7 = lambda x: np.interp(x, b2, b6)
b8 = np.linspace(0, 6, 61)
b9 = np.interp(1.0, b1[:, 0], b1[:, 1], left=np.nan, right=np.nan)
b10 = nlm.sigma2_prefactor(-2, b9)
with open('fiducial_rnl.txt', 'w') as f:
    for j, z in enumerate(b8):
        b11 = nlm.growth_factor(z, a1)
        b12 = op.brentq(
            lambda R: nlm.sigma_pl(b10, -2, R) - a2 / b11, 0.01, 8.0)
        b13 = 0.01 if z > 5 or b12 < 0 else b12
        b14 = op.brentq(
            lambda R: nlm.sigma_Pk(R, b1[:, 0], np.log(b1[:, 0]), b1[:, 1]) - a2 / b11, 0, 5)
        f.write('%.2f %15.10f\n' % (z, b14))