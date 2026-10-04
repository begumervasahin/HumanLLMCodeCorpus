import numpy as np
import matplotlib.pyplot as plt
def fonk1(means, lows, highs):
    return [(means[i] - lows[i], highs[i] - means[i]) for i in range(len(means))]
def fonk2(b15, b14, means, std, a2, b1, label, offset):
    b15.bar(b14 + offset, means, a2, b1 = b1, yerr=np.transpose(std), capsize=5, label=label)
b2 = [0.946601801623, 0.947113559077, 0.948454096069]
b3 = [0.810084820106, 0.767802605805, 0.76494951005]
b4 = [1.0, 1.0, 1.0]
b5 = fonk1(b2, b3, b4)
b6 = [0.955477854026, 0.953211106968, 0.953266175663]
b7 = [0.616405792127, 0.515454403091, 0.435178540951]
b8 = [1.0, 1.0, 1.0]
b9 = fonk1(b6, b7, b8)
b10 = [0.953938547729, 0.952260320505, 0.95265016232]
b11 = [0.615834126982, 0.515247980872, 0.436673392773]
b12 = [1.0, 1.0, 1.0]
b13 = fonk1(b10, b11, b12)
a1 = 3
b14 = np.arange(a1)
a2 = 0.2
fig, b15 = plt.subplots()
fonk2(b15, b14, b2, b5, a2, 'r', 'CAVMP', 0.2)
fonk2(b15, b14, b6, b9, a2, 'b', 'CAstatic', 0.4)
fonk2(b15, b14, b10, b13, a2, 'g', 'Static', 0.6)
b15.set_ylabel('Utilization')
b15.set_xlabel('Scale of Cloud (Racks)')
b15.set_title('Load Balance Comparison')
b15.set_xticks(b14 + a2 / 2 + 0.4)
b15.set_xticklabels(['2x2', '4x4', '8x8'])
b15.set_yticks(np.arange(0, 1.5, 0.2))
b15.legend()
plt.show()