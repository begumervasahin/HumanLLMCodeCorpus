import matplotlib.pyplot as plt
import numpy as np
from pysph.solver.utils import get_files, load
def load_initial_data(folder):
    initial_data = load(f'{folder}/vortex_spin_down_0.hdf5')['arrays']['fluid']
    u, v, m = initial_data.u, initial_data.v, initial_data.m
    max_velocity_norm = np.max(np.sqrt(u**2 + v**2))
    average_KE_norm = np.average(m * 0.5 * (u**2 + v**2))
    return max_velocity_norm, average_KE_norm
def process_simulation_data(folder, max_velocity_norm, average_KE_norm):
    vmax_list, KE_list, time_list = [], [], []
    for file_name in get_files(folder):
        data = load(file_name)
        u, v, m = data['arrays']['fluid'].u, data['arrays']['fluid'].v, data['arrays']['fluid'].m
        vmag = np.sqrt(u**2 + v**2)
        vmax = np.max(vmag) / max_velocity_norm
        KE = np.average(0.5 * m * vmag**2) / average_KE_norm
        time = data['solver_data']['t']
        vmax_list.append(vmax)
        KE_list.append(KE)
        time_list.append(time)
    return time_list, vmax_list, KE_list
def plot_data(time_lists, vmax_lists, KE_lists, titles, filenames):
    for data_list, title, filename in zip((vmax_lists, KE_lists), titles, filenames):
        plt.figure(figsize=(10, 6))
        for time, data, scenario in zip(time_lists, data_list, ['C = 1.25 (TVF)', 'C = 2.5 (TVF)', 'C = 5 (TVF)']):
            plt.plot(time, data, label=scenario)
        plt.title(title)
        plt.xlabel('Time (s)')
        plt.ylabel(title.split(' ')[-1])
        plt.legend()
        plt.savefig(filename)
        plt.clf()
folders = [
    'TVFoutput/a/vortex_spin_down_output',
    'TVFoutput/b/vortex_spin_down_output',
    'TVFoutput/c/vortex_spin_down_output'
]
results = {}
for folder in folders:
    max_velocity_norm, average_KE_norm = load_initial_data(folder)
    results[folder] = process_simulation_data(folder, max_velocity_norm, average_KE_norm)
time_lists = [result[0] for result in results.values()]
vmax_lists = [result[1] for result in results.values()]
KE_lists = [result[2] for result in results.values()]
titles = ['(TVF) Variation of Normalized Velocity with Time', '(TVF) Variation of Average Kinetic Energy with Time']
filenames = ['results_TVF_VMAX.png', 'results_TVF_KE.png']
plot_data(time_lists, vmax_lists, KE_lists, titles, filenames)