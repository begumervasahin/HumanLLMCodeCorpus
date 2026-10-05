import matplotlib.pyplot as plt
import numpy as np
from pysph.solver.utils import get_files, load
def process_simulation_data(folder_path):
    vmax_list, KE_list, time_list = [], [], []
    initial_data = load(f'{folder_path}/vortex_spin_down_0.hdf5')['arrays']['fluid']
    u_initial, v_initial = initial_data.u, initial_data.v
    initial_norm = np.max(np.sqrt(u_initial**2 + v_initial**2))
    initial_KEnorm = np.average(initial_data.m * 0.5 * (u_initial**2 + v_initial**2))
    for file_name in get_files(folder_path):
        data = load(file_name)
        u, v = data['arrays']['fluid'].u, data['arrays']['fluid'].v
        vmag = np.sqrt(u**2 + v**2)
        m = data['arrays']['fluid'].m
        KE = np.average(0.5 * m * vmag**2) / initial_KEnorm
        vmax = np.max(vmag) / initial_norm
        time = data['solver_data']['t']
        KE_list.append(KE)
        vmax_list.append(vmax)
        time_list.append(time)
    return time_list, vmax_list, KE_list
def plot_data(time, data, title, xlabel, ylabel, legend, output_filename):
    plt.figure(figsize=(10, 6))
    for t, d, label in zip(time, data, legend):
        plt.plot(t, d, label=label)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.savefig(output_filename)
    plt.clf()
time_a, vmax_a, KE_a = process_simulation_data('TVFoutput/a/vortex_spin_down_output')
time_b, vmax_b, KE_b = process_simulation_data('TVFoutput/b/vortex_spin_down_output')
time_c, vmax_c, KE_c = process_simulation_data('TVFoutput/c/vortex_spin_down_output')
plot_data(
    [time_a, time_b, time_c],
    [vmax_a, vmax_b, vmax_c],
    '(TVF) Variation of Normalized Velocity with Time',
    'Time (s)',
    'Normalized Velocity',
    ['C = 1.25 (TVF)', 'C = 2.5 (TVF)', 'C = 5 (TVF)'],
    'results_TVF_VMAX.png'
)
plot_data(
    [time_a, time_b, time_c],
    [KE_a, KE_b, KE_c],
    '(TVF) Variation of Average Kinetic Energy with Time',
    'Time (s)',
    'Normalized Average Kinetic Energy',
    ['C = 1.25 (TVF)', 'C = 2.5 (TVF)', 'C = 5 (TVF)'],
    'results_TVF_KE.png'
)