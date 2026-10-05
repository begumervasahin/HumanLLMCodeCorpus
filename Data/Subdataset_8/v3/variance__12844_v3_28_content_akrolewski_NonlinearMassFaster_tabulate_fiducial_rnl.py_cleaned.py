import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
import nonlinear_mass_faster as nlm
plt.ion()
plt.show()
pk_fiducial = np.loadtxt('pklin/default.txt')
OMEGA_M = 0.3096
DELTA_C = 1.686
DISTANCE_RANGE = np.linspace(0, 5, int(4e4) + 1)
KERNEL_GRID = np.linspace(0, 2, 100)
KERNEL_STEP = KERNEL_GRID[1] - KERNEL_GRID[0]
KERNEL_VALUES = KERNEL_GRID * KERNEL_GRID * nlm.kernel(KERNEL_GRID)
CORRELATION_FUNCTION = nlm.pk_to_xi(pk_fiducial[:, 0], pk_fiducial[:, 1], DISTANCE_RANGE)
INTERPOLATION_FUNCTION = lambda x: np.interp(x, DISTANCE_RANGE, CORRELATION_FUNCTION)
REDSHIFT_VALUES = np.linspace(0, 6, 61)
norm = np.interp(1.0, pk_fiducial[:, 0], pk_fiducial[:, 1], left=np.nan, right=np.nan)
sigma2_norm = nlm.sigma2_prefactor(-2, norm)
with open('fiducial_rnl.txt', 'w') as f:
    for index, redshift in enumerate(REDSHIFT_VALUES):
        growth_factor = nlm.growth_factor(redshift, OMEGA_M)
        rnl_analytic = op.brentq(lambda R: nlm.sigma_pl(sigma2_norm, -2, R) - DELTA_C / growth_factor, 0.01, 8.0)
        if redshift > 5 or rnl_analytic < 0:
            start_point = 0.01
        else:
            start_point = rnl_analytic
        Rnl_fid = op.brentq(lambda R: nlm.sigma_Pk(R, pk_fiducial[:, 0], np.log(pk_fiducial[:, 0]),
                                                   pk_fiducial[:, 1]) - DELTA_C / growth_factor, start_point, 5)
        f.write('%.2f %15.10f\n' % (redshift, Rnl_fid))