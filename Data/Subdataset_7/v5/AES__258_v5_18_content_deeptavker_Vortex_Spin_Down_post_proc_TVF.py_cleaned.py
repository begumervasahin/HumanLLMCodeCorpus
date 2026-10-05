import matplotlib.pyplot as plt
import numpy as np
from pysph.solver.utils import get_files, load
def fonk1(folder):
    b1 = load(f'{folder}/vortex_spin_down_0.hdf5')['arrays']['fluid']
    u, v, b2 = b1.u, b1.v, b1.b2
    b3 = np.max(np.sqrt(u**2 + v**2))
    b4 = np.average(b2 * 0.5 * (u**2 + v**2))
    return b3, b4
def fonk2(folder, b3, b4):
    vmax_list, KE_list, b5 = [], [], []
    for file_name in get_files(folder):
        b6 = load(file_name)
        u, v, b2 = b6['arrays']['fluid'].u, b6['arrays']['fluid'].v, b6['arrays']['fluid'].b2
        b7 = np.sqrt(u**2 + v**2)
        b8 = np.max(b7) / b3
        b9 = np.average(0.5 * b2 * b7**2) / b4
        b10 = b6['solver_data']['t']
        vmax_list.append(b8)
        KE_list.append(b9)
        b5.append(b10)
    return b5, vmax_list, KE_list
def fonk3(b16, b17, b18, b19, b20):
    for data_list, title, filename in zip((b17, b18), b19, b20):
        plt.figure(b11 = (10, 6))
        for b10, b6, scenario in zip(b16, data_list, ['b12 = 1.25 (TVF)', 'b12 = 2.5 (TVF)', 'b12 = 5 (TVF)']):
            plt.plot(b10, b6, b13 = scenario)
        plt.title(title)
        plt.xlabel('Time (s)')
        plt.ylabel(title.split(' ')[-1])
        plt.legend()
        plt.savefig(filename)
        plt.clf()
b14 = [
    'TVFoutput/a/vortex_spin_down_output',
    'TVFoutput/b/vortex_spin_down_output',
    'TVFoutput/c/vortex_spin_down_output'
]
b15 = {}
for folder in b14:
    b3, b4 = fonk1(folder)
    b15[folder] = fonk2(folder, b3, b4)
b16 = [result[0] for result in b15.values()]
b17 = [result[1] for result in b15.values()]
b18 = [result[2] for result in b15.values()]
b19 = ['(TVF) Variation of Normalized Velocity with Time', '(TVF) Variation of Average Kinetic Energy with Time']
b20 = ['results_TVF_VMAX.png', 'results_TVF_KE.png']
fonk3(b16, b17, b18, b19, b20)