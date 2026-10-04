import numpy as np
import matplotlib.pyplot as plt
b1 = ['2x2', '4x4', '8x8']
b2 = len(b1)
b3 = [0.946601801623, 0.947113559077, 0.948454096069]
b4 = [0.810084820106, 0.767802605805, 0.76494951005]
b5 = [1.0, 1.0, 1.0]
b6 = [0.955477854026, 0.953211106968, 0.953266175663]
b7 = [0.616405792127, 0.515454403091, 0.435178540951]
b8 = [1.0, 1.0, 1.0]
b9 = [0.953938547729, 0.952260320505, 0.95265016232]
b10 = [0.615834126982, 0.515247980872, 0.436673392773]
b11 = [1.0, 1.0, 1.0]
b12 = [
    [ave - low for ave, low in zip(b3, b4)],
    [high - ave for ave, high in zip(b3, b5)]
]
b13 = [
    [ave - low for ave, low in zip(b6, b7)],
    [high - ave for ave, high in zip(b6, b8)]
]
b14 = [
    [ave - low for ave, low in zip(b9, b10)],
    [high - ave for ave, high in zip(b9, b11)]
]
b15 = np.arange(b2)
a1 = 0.2
fig, b16 = plt.subplots()
b17 = b16.bar(b15, b3, a1, color='r', yerr=b12, label='CAVMP')
b18 = b16.bar(b15 + a1, b6, a1, color='b', yerr=b13, label='CAstatic')
b19 = b16.bar(b15 + 2 * a1, b9, a1, color='g', yerr=b14, label='Static')
b16.set_xlabel('Scale of Cloud / Racks')
b16.set_ylabel('Utilization')
b16.set_title('Load Balance Comparison')
b16.set_xticks(b15 + a1)
b16.set_xticklabels(b1)
b16.set_yticks(np.arange(0, 1.2, 0.2))
b16.legend()
plt.show()