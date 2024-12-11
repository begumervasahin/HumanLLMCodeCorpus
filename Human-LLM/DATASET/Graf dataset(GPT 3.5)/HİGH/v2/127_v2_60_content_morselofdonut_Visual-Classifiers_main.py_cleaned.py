import numpy as np
import matplotlib.pyplot as plt
x, b1 = np.loadtxt('dataset.csv', delimiter=',', unpack=True)
b2 = np.polyfit(x, b1, 15)
b3 = []
for x_val, y_val in zip(x, b1):
    b4 = abs(y_val - np.polyval(b2, x_val))
    b3.append([x_val, b4])
b5 = []
for x_value in set(x):
    b6 = [dist for val, dist in b3 if val == x_value]
    b7 = np.mean(b6)
    b5.append([x_value, b7])
b8 = plt.figure(figsize=(18, 9))
b9 = plt.subplot2grid((2, 2), (0, 0), rowspan=1, colspan=2)
b9.set_title("Value Classifier")
b10 = ['g' if y_val > np.polyval(b2, x_val) else 'r' for x_val, y_val in zip(x, b1)]
b9.scatter(x, b1, b11 = 2, marker='o', c=b10)
b9.plot(x, np.polyval(b2, x), 'b')
b12 = plt.subplot2grid((2, 2), (1, 0), rowspan=1, colspan=2)
b12.set_title("Average Distance Classifier")
b13 = ['r' if abs(np.polyval(b2, x_val) - y_val) > max_dist else 'g' for x_val, y_val in zip(x, b1) for value, max_dist in b5 if x_val == value]
b12.scatter(x, b1, b11 = 2, marker='o', c=b13)
b12.plot(x, np.polyval(b2, x), 'k', b14 = 1)
plt.show()