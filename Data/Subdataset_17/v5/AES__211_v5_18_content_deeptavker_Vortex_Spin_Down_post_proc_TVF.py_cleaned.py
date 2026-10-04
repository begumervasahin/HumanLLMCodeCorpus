import matplotlib.pyplot as plt
from pysph.solver.utils import get_files, load
import numpy as np
data_a = {"vmax": [], "KE": [], "time": []}
data_b = {"vmax": [], "KE": [], "time": []}
data_c = {"vmax": [], "KE": [], "time": []}
def load_initial_data(path):
    data = load(path)['arrays']['fluid']
    u, v = data.u, data.v
    norm = np.max(np.sqrt(u**2 + v**2))
    vmag = np.sqrt(u**2 + v**2)
    KEnorm = np.average(data.m * 0.5 * vmag**2)
    return norm, KEnorm
def process_files(path, norm, data_dict, KEnorm):
    for fname in get_files(path):
        pa = load(fname)
        fluid = pa['arrays']['fluid']
        u, v = fluid.u, fluid.v
        vmag = np.sqrt(u**2 + v**2)
        m = fluid.m
        data_dict["KE"].append(np.average(0.5 * m * vmag**2) / KEnorm)
        data_dict["vmax"].append(np.max(vmag) / norm)
        data_dict["time"].append(pa['solver_data']['t'])
def plot_data(data_dicts, labels, vmax_file, ke_file):
    for data, label in zip(data_dicts, labels):
        plt.plot(data["time"], data["vmax"], label=label)
    plt.title('(TVF) Variation of normalized velocity with time')
    plt.xlabel('Time(s)')
    plt.ylabel('Normalized Velocity')
    plt.legend()
    plt.savefig(vmax_file)
    plt.clf()
    for data, label in zip(data_dicts, labels):
        plt.plot(data["time"], data["KE"], label=label)
    plt.title('(TVF) Variation of Average Kinetic Energy with time')
    plt.xlabel('Time(s)')
    plt.ylabel('Normalized Average Kinetic Energy')
    plt.legend()
    plt.savefig(ke_file)
    plt.clf()
norm_a, KEnorm = load_initial_data('TVFoutput/a/vortex_spin_down_output/vortex_spin_down_0.hdf5')
norm_b, _ = load_initial_data('TVFoutput/b/vortex_spin_down_output/vortex_spin_down_0.hdf5')
norm_c, _ = load_initial_data('TVFoutput/c/vortex_spin_down_output/vortex_spin_down_0.hdf5')
process_files('TVFoutput/a/vortex_spin_down_output/', norm_a, data_a, KEnorm)
process_files('TVFoutput/b/vortex_spin_down_output/', norm_b, data_b, KEnorm)
process_files('TVFoutput/c/vortex_spin_down_output/', norm_c, data_c, KEnorm)
labels = ['C = 1.25 (TVF)', 'C = 2.5 (TVF)', 'C = 5 (TVF)']
plot_data([data_a, data_b, data_c], labels, 'results_TVF_VMAX.png', 'results_TVF_KE.png')