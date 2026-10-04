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
def fonk2(path, b6, data_dict, b8):
    for fname in get_files(path):
        b9 = load(fname)
        b10 = b9['arrays']['b10']
        u, b5 = b10.u, b10.b5
        b7 = np.sqrt(u**2 + b5**2)
        b11 = b10.b11
        data_dict["KE"].append(np.average(0.5 * b11 * b7**2) / b8)
        data_dict["vmax"].append(np.max(b7) / b6)
        data_dict["time"].append(b9['solver_data']['t'])
def fonk3(data_dicts, b14, vmax_file, ke_file):
    for b4, b12 in zip(data_dicts, b14):
        plt.plot(b4["time"], b4["vmax"], b12 = b12)
    plt.title('(TVF) Variation of normalized velocity with time')
    plt.xlabel('Time(s)')
    plt.ylabel('Normalized Velocity')
    plt.legend()
    plt.savefig(vmax_file)
    plt.clf()
    for b4, b12 in zip(data_dicts, b14):
        plt.plot(b4["time"], b4["KE"], b12 = b12)
    plt.title('(TVF) Variation of Average Kinetic Energy with time')
    plt.xlabel('Time(s)')
    plt.ylabel('Normalized Average Kinetic Energy')
    plt.legend()
    plt.savefig(ke_file)
    plt.clf()
norm_a, b8 = fonk1('TVFoutput/a/vortex_spin_down_output/vortex_spin_down_0.hdf5')
norm_b, b13 = fonk1('TVFoutput/b/vortex_spin_down_output/vortex_spin_down_0.hdf5')
norm_c, b13 = fonk1('TVFoutput/c/vortex_spin_down_output/vortex_spin_down_0.hdf5')
fonk2('TVFoutput/a/vortex_spin_down_output/', norm_a, b1, b8)
fonk2('TVFoutput/b/vortex_spin_down_output/', norm_b, b2, b8)
fonk2('TVFoutput/c/vortex_spin_down_output/', norm_c, b3, b8)
b14 = ['C = 1.25 (TVF)', 'C = 2.5 (TVF)', 'C = 5 (TVF)']
fonk3([b1, b2, b3], b14, 'results_TVF_VMAX.png', 'results_TVF_KE.png')