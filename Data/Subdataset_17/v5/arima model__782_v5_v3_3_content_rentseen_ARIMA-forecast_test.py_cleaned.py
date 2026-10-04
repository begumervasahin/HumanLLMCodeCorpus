import numpy as np
import matplotlib.pyplot as plt
def calculate_std(means, lows, highs):
    return [(means[i] - lows[i], highs[i] - means[i]) for i in range(len(means))]
def plot_bars(ax, ind, means, std, width, color, label, offset):
    ax.bar(ind + offset, means, width, color=color, yerr=np.transpose(std), capsize=5, label=label)
cavmp_means = [0.946601801623, 0.947113559077, 0.948454096069]
cavmp_lows = [0.810084820106, 0.767802605805, 0.76494951005]
cavmp_highs = [1.0, 1.0, 1.0]
std_cavmp = calculate_std(cavmp_means, cavmp_lows, cavmp_highs)
castatic_means = [0.955477854026, 0.953211106968, 0.953266175663]
castatic_lows = [0.616405792127, 0.515454403091, 0.435178540951]
castatic_highs = [1.0, 1.0, 1.0]
std_castatic = calculate_std(castatic_means, castatic_lows, castatic_highs)
static_means = [0.953938547729, 0.952260320505, 0.95265016232]
static_lows = [0.615834126982, 0.515247980872, 0.436673392773]
static_highs = [1.0, 1.0, 1.0]
std_static = calculate_std(static_means, static_lows, static_highs)
N = 3
ind = np.arange(N)
width = 0.2
fig, ax = plt.subplots()
plot_bars(ax, ind, cavmp_means, std_cavmp, width, 'r', 'CAVMP', 0.2)
plot_bars(ax, ind, castatic_means, std_castatic, width, 'b', 'CAstatic', 0.4)
plot_bars(ax, ind, static_means, std_static, width, 'g', 'Static', 0.6)
ax.set_ylabel('Utilization')
ax.set_xlabel('Scale of Cloud (Racks)')
ax.set_title('Load Balance Comparison')
ax.set_xticks(ind + width / 2 + 0.4)
ax.set_xticklabels(['2x2', '4x4', '8x8'])
ax.set_yticks(np.arange(0, 1.5, 0.2))
ax.legend()
plt.show()