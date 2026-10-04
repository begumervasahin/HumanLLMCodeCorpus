import numpy as np
import matplotlib.pyplot as plt
ave_cavmp_means = [0.946601801623, 0.947113559077, 0.948454096069]
low_cavmp_means = [0.810084820106, 0.767802605805, 0.76494951005]
high_cavmp_means = [1.0, 1.0, 1.0]
std_cavmp = [(ave_cavmp_means[i] - low_cavmp_means[i], high_cavmp_means[i] - ave_cavmp_means[i]) for i in range(len(ave_cavmp_means))]
ave_castatic_means = [0.955477854026, 0.953211106968, 0.953266175663]
low_castatic_means = [0.616405792127, 0.515454403091, 0.435178540951]
high_castatic_means = [1.0, 1.0, 1.0]
std_castatic = [(ave_castatic_means[i] - low_castatic_means[i], high_castatic_means[i] - ave_castatic_means[i]) for i in range(len(ave_castatic_means))]
ave_static_means = [0.953938547729, 0.952260320505, 0.95265016232]
low_static_means = [0.615834126982, 0.515247980872, 0.436673392773]
high_static_means = [1.0, 1.0, 1.0]
std_static = [(ave_static_means[i] - low_static_means[i], high_static_means[i] - ave_static_means[i]) for i in range(len(ave_static_means))]
N = 3
ind = np.arange(N)
width = 0.2
fig, ax = plt.subplots()
ax.bar(ind + 0.2, ave_cavmp_means, width, color='r', yerr=np.transpose(std_cavmp), capsize=5, label='CAVMP')
ax.bar(ind + 0.4, ave_castatic_means, width, color='b', yerr=np.transpose(std_castatic), capsize=5, label='CAstatic')
ax.bar(ind + 0.6, ave_static_means, width, color='g', yerr=np.transpose(std_static), capsize=5, label='Static')
ax.set_ylabel('Utilization')
ax.set_xlabel('Scale of Cloud (Racks)')
ax.set_title('Load Balance Comparison')
ax.set_xticks(ind + width / 2 + 0.4)
ax.set_xticklabels(('2x2', '4x4', '8x8'))
ax.set_yticks(np.arange(0, 1.5, 0.2))
ax.legend()
plt.show()