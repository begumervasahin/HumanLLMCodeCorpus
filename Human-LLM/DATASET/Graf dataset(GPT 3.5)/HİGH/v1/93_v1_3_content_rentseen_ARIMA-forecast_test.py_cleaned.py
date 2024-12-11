import numpy as np
import matplotlib.pyplot as plt
b1 = [0.946601801623, 0.947113559077, 0.948454096069]
b2 = [0.810084820106, 0.767802605805, 0.76494951005]
b3 = [1.0, 1.0, 1.0]
b4 = [(b1[i] - b2[i], b3[i] - b1[i]) for i in range(3)]
b5 = [0.955477854026, 0.953211106968, 0.953266175663]
b6 = [0.616405792127, 0.515454403091, 0.435178540951]
b7 = [1.0, 1.0, 1.0]
b8 = [(b5[i] - b6[i], b7[i] - b5[i]) for i in range(3)]
b9 = [0.953938547729, 0.952260320505, 0.95265016232]
b10 = [0.615834126982, 0.515247980872, 0.436673392773]
b11 = [1.0, 1.0, 1.0]
b12 = [(b9[i] - b10[i], b11[i] - b9[i]) for i in range(3)]
a1 = 3
b13 = np.arange(a1)
a2 = 0.2
b14 = plt.bar(b13 + 0.2, b1, a2, color='r', yerr=np.transpose(b4), capsize=5, label='CAVMP')
b15 = plt.bar(b13 + 0.4, b5, a2, color='b', yerr=np.transpose(b8), capsize=5, label='CAstatic')
b16 = plt.bar(b13 + 0.6, b9, a2, color='g', yerr=np.transpose(b12), capsize=5, label='static')
plt.ylabel('Utilization')
plt.xlabel('Scale of Cloud /racks')
plt.title('Load balance')
plt.xticks(b13 + a2 / 2 + 0.4, ('2x2', '4x4', '8x8'))
plt.yticks(np.arange(0, 1.5, 0.2))
plt.legend()
plt.show()