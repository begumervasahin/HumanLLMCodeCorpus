import numpy as np
import matplotlib.pyplot as plt
import csv
b1 = np.array([[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16],[17],[18],[19],[20]])
b2 = np.array([[1],[6],[63],[364],[1365],[3906],[9331],[19608],[37449],[66430]
,[111111],[177156],[271453],[402234],[579195],[813616],[1118481],[1508598],[2000719],[2613660],[3368421]])
b3 = np.append(b1, np.power(b1, 2), b10 = 1)
print('b4 = w1 * b1 + w2 * (b1 ^ 2)')
print('Training with ' + str(len(b3)) + ' tuples')
b5 = len(b2)
a1 = 0.00005
a2 = 10000
print('Number of a2: ' + str(a2))
print('Learning Rate: '+ str(a1))
b6 = np.array([[0.0,0.0]])
for b9 in range(a2):
    b7 = b3 @ b6.T
    b8 = (1 / (1 * b5)) * np.sum(np.square(b7 - b2))
    if b9 = = 0:
        print('Initial b8: ' + str(b8))
    elif b9 = = (a2 -1):
        print('Final b8  : ' + str(b8))
    b6[0] -= (1/b5) * a1 * np.sum((b7 - b2) * b3, b10 = 0)
plt.scatter(b3[:,0], b2)
plt.plot(b3[:,0], b7, 'r')
plt.title('Training for b4 = w1 * b1 + w2 * (b1 ^ 2)')
plt.xlabel('b3')
plt.ylabel('b2')
plt.show()
print('---------------------------------------------')
b3 = np.append(b1, np.power(b1, 2), b10 = 1)
b3 = np.append(b3, np.power(b1, 3), b10 = 1)
print('b4 = w1 * b1 + w2 * (b1 ^ 2) + w3 * (b1 ^ 3)')
print('Training with ' + str(len(b3)) + ' tuples')
b5 = len(b2)
a1 = 0.0000001
a2 = 10000
print('Number of a2: ' + str(a2))
print('Learning Rate: '+ str(a1))
b6 = np.array([[0.0,0.0,0.0]])
for b9 in range(a2):
    b7 = b3 @ b6.T
    b8 = (1 / (1 * b5)) * np.sum(np.square(b7 - b2))
    if b9 = = 0:
        print('Initial b8: ' + str(b8))
    elif b9 = = (a2 -1):
        print('Final b8  : ' + str(b8))
    b6[0] -= (1/b5) * a1 * np.sum((b7 - b2) * b3, b10 = 0)
plt.scatter(b3[:,0], b2)
plt.plot(b3[:,0], b7, 'r')
plt.title('Training for b4 = w1 * b1 + w2 * (b1 ^ 2) + w3 * (b1 ^ 3)')
plt.xlabel('b3')
plt.ylabel('b2')
plt.show()
print('---------------------------------------------')
b3 = np.append(b1, np.power(b1, 2), b10 = 1)
b3 = np.append(b3, np.power(b1, 3), b10 = 1)
b3 = np.append(b3, np.power(b1, 4), b10 = 1)
print('b4 = w1 * b1 + w2 * (b1 ^ 2) + w3 * (b1 ^ 3) + w4 * (b1 ^ 4)')
print('Training with ' + str(len(b3)) + ' tuples')
b5 = len(b2)
a1 = 0.0000000005
a2 = 10000
print('Number of a2: ' + str(a2))
print('Learning Rate: '+ str(a1))
b6 = np.array([[0.0,0.0,0.0,0.0]])
for b9 in range(a2):
    b7 = b3 @ b6.T
    b8 = (1 / (1 * b5)) * np.sum(np.square(b7 - b2))
    if b9 = = 0:
        print('Initial b8: ' + str(b8))
    elif b9 = = (a2 -1):
        print('Final b8  : ' + str(b8))
    b6[0] -= (1/b5) * a1 * np.sum((b7 - b2) * b3, b10 = 0)
plt.scatter(b3[:,0], b2)
plt.plot(b3[:,0], b7, 'r')
plt.title('Training for b4 = w1 * b1 + w2 * (b1 ^ 2) + w3 * (b1 ^ 3) + w4 * (b1 ^ 4)')
plt.xlabel('b3')
plt.ylabel('b2')
plt.show()
print('---------------------------------------------')