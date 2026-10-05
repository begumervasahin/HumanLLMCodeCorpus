import numpy as np
import matplotlib.pyplot as plt
import nonlinear_mass_faster as nlm
import scipy.optimize as op
plt.ion()
plt.show()
pk_fiducial = np.loadtxt('pklin/default.txt')
om_fid = 0.3096
delta_c = 1.686
rs = np.linspace(0, 5, int(4e4) + 1)
y = np.linspace(0, 2, 100)
dy = y[1] - y[0]
ysqkernel = y * y * nlm.kernel(y)
cflinr_fid = nlm.pk_to_xi(pk_fiducial[:, 0], pk_fiducial[:, 1], rs)
interp_cf_lin_fid = lambda x: np.interp(x, rs, cflinr_fid)
zs = np.linspace(0, 6, 61)
norm = np.interp(1.0, pk_fiducial[:, 0], pk_fiducial[:, 1], left=np.nan, right=np.nan)
sigma2_norm = nlm.sigma2_prefactor(-2, norm)
with open('fiducial_rnl.txt', 'w') as f:
    for j, z in enumerate(zs):
        Dz_fid = nlm.growth_factor(z, om_fid)
        rnl_analytic = op.brentq(
            lambda R: nlm.sigma_pl(sigma2_norm, -2, R) - delta_c / Dz_fid, 0.01, 8.0)
        start = 0.01 if z > 5 or rnl_analytic < 0 else rnl_analytic
        Rnl_fid = op.brentq(
            lambda R: nlm.sigma_Pk(R, pk_fiducial[:, 0], np.log(pk_fiducial[:, 0]), pk_fiducial[:, 1]) - delta_c / Dz_fid, 0, 5)
        f.write('%.2f %15.10f\n' % (z, Rnl_fid))