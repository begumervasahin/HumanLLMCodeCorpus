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
def process_files(path, norm, KE_list, vmax_list, time_list):
    for fname in get_files(path):
        pa = load(fname)
        fluid = pa['arrays']['fluid']
        u, v = fluid.u, fluid.v
        vmag = np.sqrt(u**2 + v**2)
        m = fluid.m
        KE_list.append(np.average(0.5 * m * vmag**2) / KEnorm)
        vmax_list.append(np.max(vmag) / norm)
        time_list.append(pa['solver_data']['t'])
def plot_data(time_data, vmax_data, KE_data, labels, vmax_file, ke_file):
    for time, vmax, label in zip(time_data, vmax_data, labels):
        plt.plot(time, vmax, label=label)
    plt.title('(TVF) Variation of normalized velocity with time')
    plt.xlabel('Time(s)')
    plt.ylabel('Normalized Velocity')
    plt.legend()
    plt.savefig(vmax_file)
    plt.clf()
    for time, KE, label in zip(time_data, KE_data, labels):
        plt.plot(time, KE, label=label)
    plt.title('(TVF) Variation of Average Kinetic Energy with time')
    plt.xlabel('Time(s)')
    plt.ylabel('Normalized Average Kinetic Energy')
    plt.legend()
    plt.savefig(ke_file)
    plt.clf()
norm_a, KEnorm = load_initial_data('TVFoutput/a/vortex_spin_down_output/vortex_spin_down_0.hdf5')
norm_b, _ = load_initial_data('TVFoutput/b/vortex_spin_down_output/vortex_spin_down_0.hdf5')
norm_c, _ = load_initial_data('TVFoutput/c/vortex_spin_down_output/vortex_spin_down_0.hdf5')
process_files('TVFoutput/a/vortex_spin_down_output/', norm_a, data_a["KE"], data_a["vmax"], data_a["time"])
process_files('TVFoutput/b/vortex_spin_down_output/', norm_b, data_b["KE"], data_b["vmax"], data_b["time"])
process_files('TVFoutput/c/vortex_spin_down_output/', norm_c, data_c["KE"], data_c["vmax"], data_c["time"])
plot_data(
    [data_a["time"], data_b["time"], data_c["time"]],
    [data_a["vmax"], data_b["vmax"], data_c["vmax"]],
    [data_a["KE"], data_b["KE"], data_c["KE"]],
    ['C = 1.25 (TVF)', 'C = 2.5 (TVF)', 'C = 5 (TVF)'],
    'results_TVF_VMAX.png',
    'results_TVF_KE.png'
)