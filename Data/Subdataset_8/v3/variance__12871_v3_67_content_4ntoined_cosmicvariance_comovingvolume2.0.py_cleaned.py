import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
import math
def calculate_E(z, omegaM, omegaK, omegaL):
    return (omegaM * (1 + z) ** 3 + omegaK * (1 + z) ** 2 + omegaL) ** 0.5
def inverse_E(z, omegaM, omegaK, omegaL):
    return 1 / calculate_E(z, omegaM, omegaK, omegaL)
def calculate_comoving_distance(z, omegaM, omegaK, omegaL):
    entries = np.rint(z * 100 + 1).astype(int)
    k = entries - 1
    E = calculate_E(z, omegaM, omegaK, omegaL)
    answer_and_error = [quad(inverse_E, 0, c, args=(omegaM, omegaK, omegaL)) for c in np.arange(0, z + 0.01, 0.01)]
    dC = [item[0] for item in answer_and_error]
    dC[0] = 0
    if omegaK > 0:
        dM = math.sinh((omegaK ** 0.5) * dC[k]) / (omegaK ** 0.5)
    elif omegaK < 0:
        dM = math.sin((abs(omegaK) ** 0.5) * dC[k]) / (abs(omegaK) ** 0.5)
    else:
        dM = dC[k]
    dA = dM / (1 + z)
    dVc = (((1 + z) ** 2) * (dA ** 2)) / E
    return dVc
def plot_comoving_volume():
    x = np.arange(0, 5.02, 0.01)
    omega_values = [
        (1, 0, 0),
        (0.05, 0.95, 0),
        (0.2, 0, 0.8)
    ]
    plt.figure()
    for i, (omegaM, omegaK, omegaL) in enumerate(omega_values):
        y = [calculate_comoving_distance(a, omegaM, omegaK, omegaL) for a in x]
        plt.plot(x, y, label=f'Omega values {i+1}')
    plt.axis([0, 5, 0, 1.2])
    plt.legend()
    plt.savefig('comovingvolume.png', dpi=80)
    plt.show()
if __name__ == "__main__":
    plot_comoving_volume()