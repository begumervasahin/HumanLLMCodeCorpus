import matplotlib.pyplot as plt
from pysph.solver.utils import get_files, load
import numpy as np
def fonk1(folder):
    b1 = []
    b2 = []
    b3 = []
    b4 = load(f'{folder}/vortex_spin_down_0.hdf5')['arrays']['fluid']
    b9, b5 = b4.b9, b4.b5
    b6 = np.max(np.sqrt(b9**2 + b5**2))
    b7 = np.average(b4.b11 * 0.5 * (b9**2 + b5**2))
    for fname in get_files(folder):
        b8 = load(fname)
        b9 = b8['arrays']['fluid'].b9
        b5 = b8['arrays']['fluid'].b5
        b10 = np.sqrt(b9**2 + b5**2)
        b11 = b8['arrays']['fluid'].b11
        b12 = np.average(0.5 * b11 * b10**2) / b7
        b13 = np.max(b10) / b6
        b14 = b8['solver_data']['t']
        b2.append(b12)
        b1.append(b13)
        b3.append(b14)
    return b3, b1, b2
time_a, vmax_a, b15 = fonk1('TVFoutput/a/vortex_spin_down_output')
time_b, vmax_b, b16 = fonk1('TVFoutput/b/vortex_spin_down_output')
time_c, vmax_c, b17 = fonk1('TVFoutput/c/vortex_spin_down_output')
plt.plot(time_a, vmax_a)
plt.plot(time_b, vmax_b)
plt.plot(time_c, vmax_c)
plt.title('(TVF) Variation of normalized velocity with b14')
plt.xlabel('Time(s)')
plt.ylabel('Normalized Velocity')
plt.legend(['b18 = 1.25 (TVF)', 'b18 = 2.5 (TVF)', 'b18 = 5 (TVF)'])
plt.savefig('results_TVF_VMAX.png')
plt.clf()
plt.plot(time_a, b15)
plt.plot(time_b, b16)
plt.plot(time_c, b17)
plt.title('(TVF) Variation of Average Kinetic Energy with b14')
plt.xlabel('Time(s)')
plt.ylabel('Normalized Average Kinetic Energy')
plt.legend(['b18 = 1.25 (TVF)', 'b18 = 2.5 (TVF)', 'b18 = 5 (TVF)'])
plt.savefig('results_TVF_KE.png')