import numpy as np
import matplotlib.pyplot as plt
x, b1 = np.loadtxt('dataset.csv', delimiter=',', unpack=True)
b2 = np.polyfit(x, b1, 15)
b3 = []
for a, b in zip(x, b1):
    b3.append([a, abs(b - np.polyval(b2, a))])
b4 = []
for b6 in set(x):
    b5 = []
    for part_x, part_y in b3:
        if b6 = = part_x:
            b5.append(part_y)
    b4.append([b6, np.mean(b5)])
b7 = plt.figure(figsize=(18, 9))
b8 = plt.subplot2grid((2, 2), (0, 0), rowspan=1, colspan=2)
plt.title("Value Classifier")
b9 = ['g' if b > np.polyval(b2, a) else 'r' for a, b in zip(x, b1)]
b8.scatter(x, b1, b10 = 2, marker='o', c=b9)
b8.plot(x, np.polyval(b2, x), 'b')
b11 = plt.subplot2grid((2, 2), (1, 0), rowspan=1, colspan=2)
plt.title("Average Distance Classifier")
b12 = ['r' if abs(np.polyval(b2, a) - b) > max_dist else 'g' for a, b in zip(x, b1) for value, max_dist in b4 if a == value]
b11.scatter(x, b1, b10 = 2, marker='o', c=b12)
b11.plot(x, np.polyval(b2, x), 'k', b13 = 1)
plt.show()