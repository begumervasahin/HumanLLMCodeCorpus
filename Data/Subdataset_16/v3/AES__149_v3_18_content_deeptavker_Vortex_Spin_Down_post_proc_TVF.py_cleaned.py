import matplotlib.pyplot as plt
from pysph.solver.utils import get_files, load
import numpy as np
b1 = {"vmax": [], "KE": [], "time": []}
b2 = {"vmax": [], "KE": [], "time": []}
b3 = {"vmax": [], "KE": [], "time": []}
def fonk1(path):
    b4 = load(path)['arrays']['b10']
    u, b5 = b4.u, b4.b5
    b6 = np.max(np.sqrt(u**2 + b5**2))
    b7 = np.sqrt(u**2 + b5**2)
    b8 = np.average(b4.b11 * 0.5 * b7**2)
    return b6, b8
def fonk2(path, b6, KE_list, vmax_list, time_list):
    for fname in get_files(path):
        b9 = load(fname)
        b10 = b9['arrays']['b10']
        u, b5 = b10.u, b10.b5
        b7 = np.sqrt(u**2 + b5**2)
        b11 = b10.b11
        KE_list.append(np.average(0.5 * b11 * b7**2) / b8)
        vmax_list.append(np.max(b7) / b6)
        time_list.append(b9['solver_data']['t'])
def fonk3(time_data, vmax_data, KE_data, labels, vmax_file, ke_file):
    for time, vmax, b12 in zip(time_data, vmax_data, labels):
        plt.plot(time, vmax, b12 = b12)
    plt.title('(TVF) Variation of normalized velocity with time')
    plt.xlabel('Time(s)')
    plt.ylabel('Normalized Velocity')
    plt.legend()
    plt.savefig(vmax_file)
    plt.clf()
    for time, KE, b12 in zip(time_data, KE_data, labels):
        plt.plot(time, KE, b12 = b12)
    plt.title('(TVF) Variation of Average Kinetic Energy with time')
    plt.xlabel('Time(s)')
    plt.ylabel('Normalized Average Kinetic Energy')
    plt.legend()
    plt.savefig(ke_file)
    plt.clf()
norm_a, b8 = fonk1('TVFoutput/a/vortex_spin_down_output/vortex_spin_down_0.hdf5')
norm_b, b13 = fonk1('TVFoutput/b/vortex_spin_down_output/vortex_spin_down_0.hdf5')
norm_c, b13 = fonk1('TVFoutput/c/vortex_spin_down_output/vortex_spin_down_0.hdf5')
fonk2('TVFoutput/a/vortex_spin_down_output/', norm_a, b1["KE"], b1["vmax"], b1["time"])
fonk2('TVFoutput/b/vortex_spin_down_output/', norm_b, b2["KE"], b2["vmax"], b2["time"])
fonk2('TVFoutput/c/vortex_spin_down_output/', norm_c, b3["KE"], b3["vmax"], b3["time"])
fonk3(
    [b1["time"], b2["time"], b3["time"]],
    [b1["vmax"], b2["vmax"], b3["vmax"]],
    [b1["KE"], b2["KE"], b3["KE"]],
    ['b14 = 1.25 (TVF)', 'b14 = 2.5 (TVF)', 'b14 = 5 (TVF)'],
    'results_TVF_VMAX.png',
    'results_TVF_KE.png'
)