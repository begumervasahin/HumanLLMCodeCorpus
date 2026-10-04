import numpy as np
import matplotlib.pyplot as plt
cloud_scales = ['2x2', '4x4', '8x8']
num_scales = len(cloud_scales)
ave_CAVMP_means = [0.946601801623, 0.947113559077, 0.948454096069]
low_CAVMP_means = [0.810084820106, 0.767802605805, 0.76494951005]
high_CAVMP_means = [1.0, 1.0, 1.0]
ave_CAstatic_means = [0.955477854026, 0.953211106968, 0.953266175663]
low_CAstatic_means = [0.616405792127, 0.515454403091, 0.435178540951]
high_CAstatic_means = [1.0, 1.0, 1.0]
ave_static_means = [0.953938547729, 0.952260320505, 0.95265016232]
low_static_means = [0.615834126982, 0.515247980872, 0.436673392773]
high_static_means = [1.0, 1.0, 1.0]
std_CAVMP = [
    [ave - low for ave, low in zip(ave_CAVMP_means, low_CAVMP_means)],
    [high - ave for ave, high in zip(ave_CAVMP_means, high_CAVMP_means)]
]
std_CAstatic = [
    [ave - low for ave, low in zip(ave_CAstatic_means, low_CAstatic_means)],
    [high - ave for ave, high in zip(ave_CAstatic_means, high_CAstatic_means)]
]
std_static = [
    [ave - low for ave, low in zip(ave_static_means, low_static_means)],
    [high - ave for ave, high in zip(ave_static_means, high_static_means)]
]
ind = np.arange(num_scales)
width = 0.2
fig, ax = plt.subplots()
bars_CAVMP = ax.bar(ind, ave_CAVMP_means, width, color='r', yerr=std_CAVMP, label='CAVMP')
bars_CAstatic = ax.bar(ind + width, ave_CAstatic_means, width, color='b', yerr=std_CAstatic, label='CAstatic')
bars_static = ax.bar(ind + 2 * width, ave_static_means, width, color='g', yerr=std_static, label='Static')
ax.set_xlabel('Scale of Cloud / Racks')
ax.set_ylabel('Utilization')
ax.set_title('Load Balance Comparison')
ax.set_xticks(ind + width)
ax.set_xticklabels(cloud_scales)
ax.set_yticks(np.arange(0, 1.2, 0.2))
ax.legend()
plt.show()