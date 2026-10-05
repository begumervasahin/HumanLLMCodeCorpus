import matplotlib.pyplot as plt
from pysph.solver.utils import get_files, load
import numpy as np
def process_files(folder):
    vmax_list = []
    KE_list = []
    time_list = []
    initial_data = load(f'{folder}/vortex_spin_down_0.hdf5')['arrays']['fluid']
    u, v = initial_data.u, initial_data.v
    norm = np.max(np.sqrt(u**2 + v**2))
    KEnorm = np.average(initial_data.m * 0.5 * (u**2 + v**2))
    for fname in get_files(folder):
        data = load(fname)
        u = data['arrays']['fluid'].u
        v = data['arrays']['fluid'].v
        vmag = np.sqrt(u**2 + v**2)
        m = data['arrays']['fluid'].m
        KE = np.average(0.5 * m * vmag**2) / KEnorm
        vmax = np.max(vmag) / norm
        time = data['solver_data']['t']
        KE_list.append(KE)
        vmax_list.append(vmax)
        time_list.append(time)
    return time_list, vmax_list, KE_list
time_a, vmax_a, KE_a = process_files('TVFoutput/a/vortex_spin_down_output')
time_b, vmax_b, KE_b = process_files('TVFoutput/b/vortex_spin_down_output')
time_c, vmax_c, KE_c = process_files('TVFoutput/c/vortex_spin_down_output')
plt.plot(time_a, vmax_a)
plt.plot(time_b, vmax_b)
plt.plot(time_c, vmax_c)
plt.title('(TVF) Variation of normalized velocity with time')
plt.xlabel('Time(s)')
plt.ylabel('Normalized Velocity')
plt.legend(['C = 1.25 (TVF)', 'C = 2.5 (TVF)', 'C = 5 (TVF)'])
plt.savefig('results_TVF_VMAX.png')
plt.clf()
plt.plot(time_a, KE_a)
plt.plot(time_b, KE_b)
plt.plot(time_c, KE_c)
plt.title('(TVF) Variation of Average Kinetic Energy with time')
plt.xlabel('Time(s)')
plt.ylabel('Normalized Average Kinetic Energy')
plt.legend(['C = 1.25 (TVF)', 'C = 2.5 (TVF)', 'C = 5 (TVF)'])
plt.savefig('results_TVF_KE.png')