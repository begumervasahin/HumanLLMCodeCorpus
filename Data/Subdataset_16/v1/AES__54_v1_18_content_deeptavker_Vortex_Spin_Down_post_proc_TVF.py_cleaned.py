import matplotlib.pyplot as plt
from pysph.solver.utils import get_files, load
import numpy as np
vmax_a, KE_a, b1 = [], [], []
vmax_b, KE_b, b2 = [], [], []
vmax_c, KE_c, b3 = [], [], []
def fonk1(path):
    b4 = load(path)['arrays']['fluid']
    b11, b5 = b4.b11, b4.b5
    b6 = np.max((b11**2 + b5**2)**0.5)
    b7 = (b5**2 + b11**2)**0.5
    b8 = np.average(b4.b12 * 0.5 * b7 * b7)
    return b6, b8
norm_a, b8 = fonk1('TVFoutput/a/vortex_spin_down_output/vortex_spin_down_0.hdf5')
norm_b, b9 = fonk1('TVFoutput/b/vortex_spin_down_output/vortex_spin_down_0.hdf5')
norm_c, b9 = fonk1('TVFoutput/c/vortex_spin_down_output/vortex_spin_down_0.hdf5')
def fonk2(path, b6, KE_list, vmax_list, time_list):
    for fname in get_files(path):
        b10 = load(fname)
        b11 = b10['arrays']['fluid'].b11
        b5 = b10['arrays']['fluid'].b5
        b7 = (b11**2 + b5**2)**0.5
        b12 = b10['arrays']['fluid'].b12
        KE_list.append(np.average(0.5 * b12 * b7 * b7) / b8)
        b13 = np.max((b11**2 + b5**2)**0.5)
        vmax_list.append(b13 / b6)
        time_list.append(b10['solver_data']['t'])
fonk2('TVFoutput/a/vortex_spin_down_output/', norm_a, KE_a, vmax_a, b1)
fonk2('TVFoutput/b/vortex_spin_down_output/', norm_b, KE_b, vmax_b, b2)
fonk2('TVFoutput/c/vortex_spin_down_output/', norm_c, KE_c, vmax_c, b3)
plt.plot(b1, vmax_a, b14 = 'C = 1.25 (TVF)')
plt.plot(b2, vmax_b, b14 = 'C = 2.5 (TVF)')
plt.plot(b3, vmax_c, b14 = 'C = 5 (TVF)')
plt.title('(TVF) Variation of normalized velocity with time')
plt.xlabel('Time(s)')
plt.ylabel('Normalized Velocity')
plt.legend()
plt.savefig('results_TVF_VMAX.png')
plt.clf()
plt.plot(b1, KE_a, b14 = 'C = 1.25 (TVF)')
plt.plot(b2, KE_b, b14 = 'C = 2.5 (TVF)')
plt.plot(b3, KE_c, b14 = 'C = 5 (TVF)')
plt.title('(TVF) Variation of Average Kinetic Energy with time')
plt.xlabel('Time(s)')
plt.ylabel('Normalized Average Kinetic Energy')
plt.legend()
plt.savefig('results_TVF_KE.png')