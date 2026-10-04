import numpy as np
import matplotlib.pyplot as plt
def fonk1(means, lows, highs):
    b1 = [mean - low for mean, low in zip(means, lows)]
    b2 = [high - mean for mean, high in zip(means, highs)]
    return [b1, b2]
b3 = {
    'CAVMP': {
        'means': [0.946601801623, 0.947113559077, 0.948454096069],
        'lows': [0.810084820106, 0.767802605805, 0.76494951005],
        'highs': [1.0, 1.0, 1.0],
        'b8': 'r',
        'label': 'CAVMP'
    },
    'CAstatic': {
        'means': [0.955477854026, 0.953211106968, 0.953266175663],
        'lows': [0.616405792127, 0.515454403091, 0.435178540951],
        'highs': [1.0, 1.0, 1.0],
        'b8': 'b',
        'label': 'CAstatic'
    },
    'Static': {
        'means': [0.953938547729, 0.952260320505, 0.95265016232],
        'lows': [0.615834126982, 0.515247980872, 0.436673392773],
        'highs': [1.0, 1.0, 1.0],
        'b8': 'g',
        'label': 'Static'
    }
}
b4 = ['2x2', '4x4', '8x8']
a1 = 0.2
b5 = np.arange(len(b4))
fig, b6 = plt.subplots()
for idx, (strategy, config) in enumerate(b3.items()):
    b7 = fonk1(config['means'], config['lows'], config['highs'])
    b6.bar(b5 + idx * a1, config['means'], a1, b8 = config['b8'],
           b9 = b7, label=config['label'])
b6.set_xlabel('Scale of Cloud / Racks')
b6.set_ylabel('Utilization')
b6.set_title('Load Balance Comparison')
b6.set_xticks(b5 + a1)
b6.set_xticklabels(b4)
b6.set_yticks(np.arange(0, 1.2, 0.2))
b6.legend()
plt.show()