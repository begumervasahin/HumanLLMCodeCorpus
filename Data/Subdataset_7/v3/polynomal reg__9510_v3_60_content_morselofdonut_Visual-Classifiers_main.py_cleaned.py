import numpy as np
import matplotlib.pyplot as plt
x, b1 = np.loadtxt('dataset.csv', delimiter=',', unpack=True)
b2 = np.polyfit(x, b1, 15)
b3 = [(x_val, abs(y_val - np.polyval(b2, x_val))) for x_val, y_val in zip(x, b1)]
b4 = []
for x_val in set(x):
    b5 = [dist for val, dist in b3 if val == x_val]
    b6 = np.mean(b5)
    b4.append((x_val, b6))
fig, b7 = plt.subplots(nrows=2, ncols=1, figsize=(18, 9))
ax1, b8 = b7
ax1.set_title("Value Classifier")
b9 = ['g' if y_val > np.polyval(b2, x_val) else 'r' for x_val, y_val in zip(x, b1)]
ax1.scatter(x, b1, b10 = 2, marker='o', c=b9)
ax1.plot(x, np.polyval(b2, x), 'b')
b8.set_title("Average Distance Classifier")
b11 = ['r' if abs(np.polyval(b2, x_val) - y_val) > max_dist else 'g' for x_val, y_val in zip(x, b1) for value, max_dist in b4 if x_val == value]
b8.scatter(x, b1, b10 = 2, marker='o', c=b11)
b8.plot(x, np.polyval(b2, x), 'k', b12 = 1)
plt.tight_layout()
plt.show()