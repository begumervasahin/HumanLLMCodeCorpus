import matplotlib.pyplot as plt
from pysph.solver.utils import get_files, load
import numpy as np
vmax_a, KE_a, b1 = [], [], []
vmax_b, KE_b, b2 = [], [], []
vmax_c, KE_c, b3 = [], [], []
def fonk1(path):
    b4 = load(path)['arrays']['b11']
    u, b5 = b4.u, b4.b5
    b6 = np.max(np.sqrt(u**2 + b5**2))
    b7 = np.sqrt(u**2 + b5**2)
    b8 = np.average(b4.b12 * 0.5 * b7**2)
    return b6, b8
norm_a, b8 = fonk1('TVFoutput/a/vortex_spin_down_output/vortex_spin_down_0.hdf5')
norm_b, b9 = fonk1('TVFoutput/b/vortex_spin_down_output/vortex_spin_down_0.hdf5')
norm_c, b9 = fonk1('TVFoutput/c/vortex_spin_down_output/vortex_spin_down_0.hdf5')
def fonk2(path, b6, KE_list, vmax_list, time_list):
    for fname in get_files(path):
        b10 = load(fname)
        b11 = b10['arrays']['b11']
        u, b5 = b11.u, b11.b5
        b7 = np.sqrt(u**2 + b5**2)
        b12 = b11.b12
        KE_list.append(np.average(0.5 * b12 * b7**2) / b8)
        vmax_list.append(np.max(b7) / b6)
        time_list.append(b10['solver_data']['t'])
fonk2('TVFoutput/a/vortex_spin_down_output/', norm_a, KE_a, vmax_a, b1)
fonk2('TVFoutput/b/vortex_spin_down_output/', norm_b, KE_b, vmax_b, b2)
fonk2('TVFoutput/c/vortex_spin_down_output/', norm_c, KE_c, vmax_c, b3)
def fonk3(time_data, vmax_data, KE_data, b14, vmax_file, ke_file):
    for time, vmax, b13 in zip(time_data, vmax_data, b14):
        plt.plot(time, vmax, b13 = b13)
    plt.title('(TVF) Variation of normalized velocity with time')
    plt.xlabel('Time(s)')
    plt.ylabel('Normalized Velocity')
    plt.legend()
    plt.savefig(vmax_file)
    plt.clf()
    for time, KE, b13 in zip(time_data, KE_data, b14):
        plt.plot(time, KE, b13 = b13)
    plt.title('(TVF) Variation of Average Kinetic Energy with time')
    plt.xlabel('Time(s)')
    plt.ylabel('Normalized Average Kinetic Energy')
    plt.legend()
    plt.savefig(ke_file)
    plt.clf()
b14 = ['C = 1.25 (TVF)', 'C = 2.5 (TVF)', 'C = 5 (TVF)']
fonk3(
    [b1, b2, b3],
    [vmax_a, vmax_b, vmax_c],
    [KE_a, KE_b, KE_c],
    b14,
    'results_TVF_VMAX.png',
    'results_TVF_KE.png'
)