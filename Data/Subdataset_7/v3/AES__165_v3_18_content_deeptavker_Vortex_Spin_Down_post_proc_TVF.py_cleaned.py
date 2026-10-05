import matplotlib.pyplot as plt
import numpy as np
from pysph.solver.utils import get_files, load
def fonk1(u, v, b1 = False, b3=None, b4=None):
    b2 = np.sqrt(u**2 + v**2)
    if b1:
        b3 = np.max(b2)
        b4 = np.average(0.5 * b2**2)
        return b3, b4
    else:
        b5 = np.max(b2) / b3
        b6 = np.average(0.5 * b2**2) / b4
        return b5, b6
def fonk2(folder_path):
    vmax_list, KE_list, b7 = [], [], []
    b8 = load(f'{folder_path}/vortex_spin_down_0.hdf5')['arrays']['fluid']
    b3, b4 = fonk1(b8.u, b8.v, b1=True)
    for file_name in get_files(folder_path):
        b9 = load(file_name)
        vmax, b10 = fonk1(b9['arrays']['fluid'].u, b9['arrays']['fluid'].v, b3=b3, b4=b4)
        b11 = b9['solver_data']['t']
        KE_list.append(b10)
        vmax_list.append(vmax)
        b7.append(b11)
    return b7, vmax_list, KE_list
def fonk3(time_lists, data_lists, title, xlabel, ylabel, legends, output_filename):
    plt.figure(b12 = (10, 6))
    for b11, b9, legend in zip(time_lists, data_lists, legends):
        plt.plot(b11, b9, b13 = legend)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.savefig(output_filename)
    plt.close()
b14 = [
    'TVFoutput/a/vortex_spin_down_output',
    'TVFoutput/b/vortex_spin_down_output',
    'TVFoutput/c/vortex_spin_down_output'
]
time_lists, vmax_lists, b15 = zip(*(fonk2(folder) for folder in b14))
b16 = ['C = 1.25 (TVF)', 'C = 2.5 (TVF)', 'C = 5 (TVF)']
fonk3(
    time_lists,
    vmax_lists,
    '(TVF) Variation of Normalized Velocity with Time',
    'Time (s)',
    'Normalized Velocity',
    b16,
    'results_TVF_VMAX.png'
)
fonk3(
    time_lists,
    b15,
    '(TVF) Variation of Average Kinetic Energy with Time',
    'Time (s)',
    'Normalized Average Kinetic Energy',
    b16,
    'results_TVF_KE.png'
)