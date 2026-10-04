import numpy as np
import matplotlib.pyplot as plt
def calculate_error_bars(means, lows, highs):
    lower_errors = [mean - low for mean, low in zip(means, lows)]
    upper_errors = [high - mean for mean, high in zip(means, highs)]
    return [lower_errors, upper_errors]
strategies = {
    'CAVMP': {
        'means': [0.946601801623, 0.947113559077, 0.948454096069],
        'lows': [0.810084820106, 0.767802605805, 0.76494951005],
        'highs': [1.0, 1.0, 1.0],
        'color': 'r',
        'label': 'CAVMP'
    },
    'CAstatic': {
        'means': [0.955477854026, 0.953211106968, 0.953266175663],
        'lows': [0.616405792127, 0.515454403091, 0.435178540951],
        'highs': [1.0, 1.0, 1.0],
        'color': 'b',
        'label': 'CAstatic'
    },
    'Static': {
        'means': [0.953938547729, 0.952260320505, 0.95265016232],
        'lows': [0.615834126982, 0.515247980872, 0.436673392773],
        'highs': [1.0, 1.0, 1.0],
        'color': 'g',
        'label': 'Static'
    }
}
cloud_scales = ['2x2', '4x4', '8x8']
bar_width = 0.2
ind = np.arange(len(cloud_scales))
fig, ax = plt.subplots()
for idx, (strategy, config) in enumerate(strategies.items()):
    error_bars = calculate_error_bars(config['means'], config['lows'], config['highs'])
    ax.bar(ind + idx * bar_width, config['means'], bar_width, color=config['color'],
           yerr=error_bars, label=config['label'])
ax.set_xlabel('Scale of Cloud / Racks')
ax.set_ylabel('Utilization')
ax.set_title('Load Balance Comparison')
ax.set_xticks(ind + bar_width)
ax.set_xticklabels(cloud_scales)
ax.set_yticks(np.arange(0, 1.2, 0.2))
ax.legend()
plt.show()