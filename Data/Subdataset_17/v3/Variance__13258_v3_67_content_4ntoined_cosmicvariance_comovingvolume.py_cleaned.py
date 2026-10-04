import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.integrate import quad
def calculate_xE(z, omegaM, omegaK, omegaL):
    return (omegaM * (1 + z)**3 + omegaK * (1 + z)**2 + omegaL)**0.5
def inverse_xE(z, omegaM, omegaK, omegaL):
    return 1 / calculate_xE(z, omegaM, omegaK, omegaL)
def calculate_dVc(z, omegaM, omegaK, omegaL):
    entries = int(z * 100 + 1)
    E = calculate_xE(z, omegaM, omegaK, omegaL)
    answer_and_error = [quad(inverse_xE, 0, c, args=(omegaM, omegaK, omegaL)) for c in np.arange(0, z, 0.01)]
    dC = [answer[0] for answer in answer_and_error]
    if omegaK > 0:
        dM = math.sinh((omegaK**0.5) * dC[-1]) / (omegaK**0.5)
    elif omegaK < 0:
        dM = math.sin((abs(omegaK)**0.5) * dC[-1]) / (abs(omegaK)**0.5)
    else:
        dM = dC[-1]
    dA = dM / (1 + z)
    dVc = (((1 + z)**2) * (dA**2)) / E
    return dVc
cosmological_params = [
    {'omegaM': 1, 'omegaK': 0, 'omegaL': 0},
    {'omegaM': 0.05, 'omegaK': 0.95, 'omegaL': 0},
    {'omegaM': 0.2, 'omegaK': 0, 'omegaL': 0.8}
]
redshift_range = np.arange(0, 5.02, 0.01)
dVc_arrays = []
for params in cosmological_params:
    dVc_arrays.append([calculate_dVc(z, **params) for z in redshift_range])
plt.figure(figsize=(10, 6))
for i, dVc_array in enumerate(dVc_arrays):
    plt.plot(redshift_range, dVc_array, label=f'Case {i + 1}')
plt.xlabel('Redshift (z)')
plt.ylabel('Comoving Volume Element (dVc)')
plt.title('Ploot Function for Different Cosmological Parameters')
plt.legend()
plt.axis([0, 5, 0, 1.2])
plt.grid(True)
plt.show()