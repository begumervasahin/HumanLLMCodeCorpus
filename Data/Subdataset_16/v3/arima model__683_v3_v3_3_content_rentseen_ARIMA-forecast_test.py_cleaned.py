import numpy as np
import matplotlib.pyplot as plt
def fonk1(means, lows, highs):
    return [(mean - low, high - mean) for mean, low, high in zip(means, lows, highs)]
def fonk2():
    b1 = [0.946601801623, 0.947113559077, 0.948454096069]
    b2 = [0.810084820106, 0.767802605805, 0.76494951005]
    b3 = [1.0, 1.0, 1.0]
    b4 = fonk1(b1, b2, b3)
    b5 = [0.955477854026, 0.953211106968, 0.953266175663]
    b6 = [0.616405792127, 0.515454403091, 0.435178540951]
    b7 = [1.0, 1.0, 1.0]
    b8 = fonk1(b5, b6, b7)
    b9 = [0.953938547729, 0.952260320505, 0.95265016232]
    b10 = [0.615834126982, 0.515247980872, 0.436673392773]
    b11 = [1.0, 1.0, 1.0]
    b12 = fonk1(b9, b10, b11)
    return (b1, b4), (b5, b8), (b9, b12)
def fonk3():
    (b1, b4), (b5, b8), (b9, b12) = fonk2()
    a1 = 3
    b13 = np.arange(a1)
    a2 = 0.2
    plt.bar(b13 + 0.2, b1, a2, b14 = 'r', yerr=np.transpose(b4), capsize=5, label='CAVMP')
    plt.bar(b13 + 0.4, b5, a2, b14 = 'b', yerr=np.transpose(b8), capsize=5, label='CAstatic')
    plt.bar(b13 + 0.6, b9, a2, b14 = 'g', yerr=np.transpose(b12), capsize=5, label='Static')
    plt.ylabel('Utilization')
    plt.xlabel('Scale of Cloud (Racks)')
    plt.title('Load Balance Comparison')
    plt.xticks(b13 + a2 / 2 + 0.4, ['2x2', '4x4', '8x8'])
    plt.yticks(np.arange(0, 1.5, 0.2))
    plt.legend()
    plt.show()
if b15 = = "__main__":
    fonk3()