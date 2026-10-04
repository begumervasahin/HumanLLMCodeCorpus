import numpy as np
import matplotlib.pyplot as plt
cloud_scales = ['2x2', '4x4', '8x8']
means = {
    "CAVMP": [0.946601801623, 0.947113559077, 0.948454096069],
    "CAstatic": [0.955477854026, 0.953211106968, 0.953266175663],
    "Static": [0.953938547729, 0.952260320505, 0.95265016232]
}
lows = {
    "CAVMP": [0.810084820106, 0.767802605805, 0.76494951005],
    "CAstatic": [0.616405792127, 0.515454403091, 0.435178540951],
    "Static": [0.615834126982, 0.515247980872, 0.436673392773]
}
highs = {
    "CAVMP": [1.0, 1.0, 1.0],
    "CAstatic": [1.0, 1.0, 1.0],
    "Static": [1.0, 1.0, 1.0]
}
def calculate_std(means, lows, highs):
    return [[mean - low for mean, low in zip(means, lows)],
            [high - mean for mean, high in zip(means, highs)]]
std_devs = {
    "CAVMP": calculate_std(means["CAVMP"], lows["CAVMP"], highs["CAVMP"]),
    "CAstatic": calculate_std(means["CAstatic"], lows["CAstatic"], highs["CAstatic"]),
    "Static": calculate_std(means["Static"], lows["Static"], highs["Static"])
}
ind = np.arange(len(cloud_scales))
width = 0.2
fig, ax = plt.subplots()
colors = {"CAVMP": 'r', "CAstatic": 'b', "Static": 'g'}
for i, (strategy, color) in enumerate(colors.items()):
    ax.bar(ind + i * width, means[strategy], width, color=color, yerr=std_devs[strategy], label=strategy)
ax.set_xlabel('Scale of Cloud / Racks')
ax.set_ylabel('Utilization')
ax.set_title('Load Balance Comparison')
ax.set_xticks(ind + width)
ax.set_xticklabels(cloud_scales)
ax.set_yticks(np.arange(0, 1.2, 0.2))
ax.legend()
plt.show()