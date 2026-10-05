import numpy as np
import matplotlib.pyplot as plt
x, y = np.loadtxt('dataset.csv', delimiter=',', unpack=True)
coefficients = np.polyfit(x, y, 15)
distances = []
for x_val, y_val in zip(x, y):
    distance = abs(y_val - np.polyval(coefficients, x_val))
    distances.append([x_val, distance])
averages = []
for x_value in set(x):
    x_distances = [dist for val, dist in distances if val == x_value]
    avg_distance = np.mean(x_distances)
    averages.append([x_value, avg_distance])
fig = plt.figure(figsize=(18, 9))
ax1 = plt.subplot2grid((2, 2), (0, 0), rowspan=1, colspan=2)
ax1.set_title("Value Classifier")
value_colors = ['g' if y_val > np.polyval(coefficients, x_val) else 'r' for x_val, y_val in zip(x, y)]
ax1.scatter(x, y, s=2, marker='o', c=value_colors)
ax1.plot(x, np.polyval(coefficients, x), 'b')
ax2 = plt.subplot2grid((2, 2), (1, 0), rowspan=1, colspan=2)
ax2.set_title("Average Distance Classifier")
distance_colors = ['r' if abs(np.polyval(coefficients, x_val) - y_val) > max_dist else 'g' for x_val, y_val in zip(x, y) for value, max_dist in averages if x_val == value]
ax2.scatter(x, y, s=2, marker='o', c=distance_colors)
ax2.plot(x, np.polyval(coefficients, x), 'k', linewidth=1)
plt.show()