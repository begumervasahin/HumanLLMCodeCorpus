import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
import nonlinear_mass_faster as nlm
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
    for index, redshift in enumerate(b8):
        b11 = nlm.b11(redshift, a1)
        b12 = op.brentq(lambda R: nlm.sigma_pl(b10, -2, R) - a2 / b11, 0.01, 8.0)
        if redshift > 5 or b12 < 0:
            a3 = 0.01
        else:
            a3 = b12
        b13 = op.brentq(lambda R: nlm.sigma_Pk(R, b1[:, 0], np.log(b1[:, 0]),
                                                   b1[:, 1]) - a2 / b11, a3, 5)
        f.write('%.2f %15.10f\n' % (redshift, b13))