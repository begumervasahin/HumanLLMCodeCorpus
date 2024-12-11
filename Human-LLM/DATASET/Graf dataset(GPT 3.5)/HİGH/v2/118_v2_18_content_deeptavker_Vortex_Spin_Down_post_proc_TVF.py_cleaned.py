import matplotlib.pyplot as plt
import numpy as np
from pysph.solver.utils import get_files, load
def fonk1(folder_path):
    vmax_list, KE_list, b1 = [], [], []
    b2 = load(f'{folder_path}/vortex_spin_down_0.hdf5')['arrays']['fluid']
    u_initial, b3 = b2.u, b2.b7
    b4 = np.max(np.sqrt(u_initial**2 + b3**2))
    b5 = np.average(b2.b9 * 0.5 * (u_initial**2 + b3**2))
    for file_name in get_files(folder_path):
        b6 = load(file_name)
        u, b7 = b6['arrays']['fluid'].u, b6['arrays']['fluid'].b7
        b8 = np.sqrt(u**2 + b7**2)
        b9 = b6['arrays']['fluid'].b9
        b10 = np.average(0.5 * b9 * b8**2) / b5
        b11 = np.max(b8) / b4
        b12 = b6['solver_data']['t']
        KE_list.append(b10)
        vmax_list.append(b11)
        b1.append(b12)
    return b1, vmax_list, KE_list
def fonk2(b12, b6, title, xlabel, ylabel, legend, output_filename):
    plt.figure(b13 = (10, 6))
    for t, d, b14 in zip(b12, b6, legend):
        plt.plot(t, d, b14 = b14)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.savefig(output_filename)
    plt.clf()
time_a, vmax_a, b15 = fonk1('TVFoutput/a/vortex_spin_down_output')
time_b, vmax_b, b16 = fonk1('TVFoutput/b/vortex_spin_down_output')
time_c, vmax_c, b17 = fonk1('TVFoutput/c/vortex_spin_down_output')
fonk2(
    [time_a, time_b, time_c],
    [vmax_a, vmax_b, vmax_c],
    '(TVF) Variation of Normalized Velocity with Time',
    'Time (s)',
    'Normalized Velocity',
    ['b18 = 1.25 (TVF)', 'b18 = 2.5 (TVF)', 'b18 = 5 (TVF)'],
    'results_TVF_VMAX.png'
)
fonk2(
    [time_a, time_b, time_c],
    [b15, b16, b17],
    '(TVF) Variation of Average Kinetic Energy with Time',
    'Time (s)',
    'Normalized Average Kinetic Energy',
    ['b18 = 1.25 (TVF)', 'b18 = 2.5 (TVF)', 'b18 = 5 (TVF)'],
    'results_TVF_KE.png'
)