import matplotlib.pyplot as plt
from pysph.solver.utils import get_files, load
import numpy as np
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []
b7 = []
b8 = []
b9 = []
b10 = load('TVFoutput/a/vortex_spin_down_output/vortex_spin_down_0.hdf5')['arrays']['fluid']
b20, b11 = b10.b20, b10.b11
b12 = np.max((b20**2 + b11**2)**0.5)
b13 = (b11**2 + b20**2)**0.5
b14 = np.average(b10.b21*0.5*b13*b13)
b15 = load('TVFoutput/b/vortex_spin_down_output/vortex_spin_down_0.hdf5')['arrays']['fluid']
b20, b11 = b15.b20, b15.b11
b16 = np.max((b20**2 + b11**2)**0.5)
b17 = load('TVFoutput/c/vortex_spin_down_output/vortex_spin_down_0.hdf5')['arrays']['fluid']
b20, b11 = b17.b20, b17.b11
b18 = np.max((b20**2 + b11**2)**0.5)
for fname in get_files('TVFoutput/a/vortex_spin_down_output/'):
    b19 = load(fname)
    b20 = b19['arrays']['fluid'].b20
    b11 = b19['arrays']['fluid'].b11
    b13 = (b20**2 + b11**2)**0.5
    b21 = b19['arrays']['fluid'].b21
    b2.append(np.average(0.5*b21*b13*b13)/b14)
    b22 = np.max((b20**2 + b11**2)**0.5)
    b1.append(b22/b12)
    b7.append(b19['solver_data']['t'])
for fname in get_files('TVFoutput/b/vortex_spin_down_output/'):
    b19 = load(fname)
    b20 = b19['arrays']['fluid'].b20
    b11 = b19['arrays']['fluid'].b11
    b22 = np.max((b20**2 + b11**2)**0.5)
    b3.append(b22/b16)
    b8.append(b19['solver_data']['t'])
    b13 = (b20**2 + b11**2)**0.5
    b21 = b19['arrays']['fluid'].b21
    b4.append(np.average(0.5*b21*b13*b13)/b14)
for fname in get_files('TVFoutput/c/vortex_spin_down_output/'):
    b19 = load(fname)
    b20 = b19['arrays']['fluid'].b20
    b11 = b19['arrays']['fluid'].b11
    b22 = np.max((b20**2 + b11**2)**0.5)
    b5.append(b22/b18)
    b9.append(b19['solver_data']['t'])
    b13 = (b20**2 + b11**2)**0.5
    b21 = b19['arrays']['fluid'].b21
    b6.append(np.average(0.5*b21*b13*b13/b14))
plt.plot(b7, b1)
plt.plot(b8, b3)
plt.plot(b9, b5)
plt.title('(TVF) Variation of normalized velocity with time')
plt.xlabel('Time(s)')
plt.ylabel('Normalized Velocity')
plt.legend(['b23 = 1.25 (TVF)', 'b23 = 2.5 (TVF)', 'b23 = 5 (TVF)'])
plt.savefig('results_TVF_VMAX.png')
plt.clf()
plt.plot(b7, b2)
plt.plot(b8, b4)
plt.plot(b9, b6)
plt.title('(TVF) Variation of Average Kinetic Energy with time')
plt.xlabel('Time(s)')
plt.ylabel('Normalized Average Kinetic Energy')
plt.legend(['b23 = 1.25 (TVF)', 'b23 = 2.5 (TVF)', 'b23 = 5 (TVF)'])
plt.savefig('results_TVF_KE.png')