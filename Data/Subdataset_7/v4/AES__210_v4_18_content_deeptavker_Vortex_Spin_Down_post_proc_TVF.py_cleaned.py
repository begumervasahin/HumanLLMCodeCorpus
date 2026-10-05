import matplotlib.pyplot as plt
import numpy as np
from pysph.solver.utils import get_files, load
def fonk1(folder):
    vmax_list, KE_list, b1 = [], [], []
    b2 = load(f'{folder}/vortex_spin_down_0.hdf5')['arrays']['fluid']
    u, b3 = b2.u, b2.b3
    b4 = np.max(np.sqrt(u**2 + b3**2))
    b5 = np.average(b2.m * 0.5 * (u**2 + b3**2))
    for file_name in get_files(folder):
        b6 = load(file_name)
        u, b3 = b6['arrays']['fluid'].u, b6['arrays']['fluid'].b3
        b7 = np.sqrt(u**2 + b3**2)
        b8 = np.max(b7) / b4
        b9 = np.average(b6['arrays']['fluid'].m * 0.5 * b7**2) / b5
        b10 = b6['solver_data']['t']
        vmax_list.append(b8)
        KE_list.append(b9)
        b1.append(b10)
    return b1, vmax_list, KE_list
def fonk2(time_lists, vmax_lists, b16):
    b11 = ['C = 1.25 (TVF)', 'C = 2.5 (TVF)', 'C = 5 (TVF)']
    plt.figure(b12 = (10, 6))
    for b10, b8, scenario in zip(time_lists, vmax_lists, b11):
        plt.plot(b10, b8, b13 = scenario)
    plt.title('(TVF) Variation of Normalized Velocity with Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Normalized Velocity')
    plt.legend()
    plt.savefig('results_TVF_VMAX.png')
    plt.clf()
    plt.figure(b12 = (10, 6))
    for b10, b9, scenario in zip(time_lists, b16, b11):
        plt.plot(b10, b9, b13 = scenario)
    plt.title('(TVF) Variation of Average Kinetic Energy with Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Normalized Average Kinetic Energy')
    plt.legend()
    plt.savefig('results_TVF_KE.png')
    plt.clf()
b14 = [
    'TVFoutput/a/vortex_spin_down_output',
    'TVFoutput/b/vortex_spin_down_output',
    'TVFoutput/c/vortex_spin_down_output'
]
b15 = [fonk1(folder) for folder in b14]
time_lists, vmax_lists, b16 = zip(*b15)
fonk2(time_lists, vmax_lists, b16)