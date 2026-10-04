import numpy as np
import matplotlib.pyplot as plt
b1 = ['2x2', '4x4', '8x8']
b2 = {
    "CAVMP": [0.946601801623, 0.947113559077, 0.948454096069],
    "CAstatic": [0.955477854026, 0.953211106968, 0.953266175663],
    "Static": [0.953938547729, 0.952260320505, 0.95265016232]
}
b3 = {
    "CAVMP": [0.810084820106, 0.767802605805, 0.76494951005],
    "CAstatic": [0.616405792127, 0.515454403091, 0.435178540951],
    "Static": [0.615834126982, 0.515247980872, 0.436673392773]
}
b4 = {
    "CAVMP": [1.0, 1.0, 1.0],
    "CAstatic": [1.0, 1.0, 1.0],
    "Static": [1.0, 1.0, 1.0]
}
def fonk1(b2, b3, b4):
    return [[mean - low for mean, low in zip(b2, b3)],
            [high - mean for mean, high in zip(b2, b4)]]
b5 = {
    "CAVMP": fonk1(b2["CAVMP"], b3["CAVMP"], b4["CAVMP"]),
    "CAstatic": fonk1(b2["CAstatic"], b3["CAstatic"], b4["CAstatic"]),
    "Static": fonk1(b2["Static"], b3["Static"], b4["Static"])
}
b6 = np.arange(len(b1))
a1 = 0.2
fig, b7 = plt.subplots()
b8 = {"CAVMP": 'r', "CAstatic": 'b', "Static": 'g'}
for i, (strategy, b9) in enumerate(b8.items()):
    b7.bar(b6 + i * a1, b2[strategy], a1, b9 = b9, yerr=b5[strategy], label=strategy)
b7.set_xlabel('Scale of Cloud / Racks')
b7.set_ylabel('Utilization')
b7.set_title('Load Balance Comparison')
b7.set_xticks(b6 + a1)
b7.set_xticklabels(b1)
b7.set_yticks(np.arange(0, 1.2, 0.2))
b7.legend()
plt.show()