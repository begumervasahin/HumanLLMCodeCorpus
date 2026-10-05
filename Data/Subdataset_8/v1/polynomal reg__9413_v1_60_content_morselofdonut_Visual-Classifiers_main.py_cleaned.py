import numpy as np
import matplotlib.pyplot as plt
x, y = np.loadtxt('dataset.csv', delimiter=',', unpack=True)
p15 = np.polyfit(x, y, 15)
distances = []
for a, b in zip(x, y):
    distances.append([a, abs(b - np.polyval(p15, a))])
avg = []
for dist_value in set(x):
    avg_part = []
    for part_x, part_y in distances:
        if dist_value == part_x:
            avg_part.append(part_y)
    avg.append([dist_value, np.mean(avg_part)])
fig = plt.figure(figsize=(18, 9))
ax1 = plt.subplot2grid((2, 2), (0, 0), rowspan=1, colspan=2)
plt.title("Value Classifier")
colors_val = ['g' if b > np.polyval(p15, a) else 'r' for a, b in zip(x, y)]
ax1.scatter(x, y, s=2, marker='o', c=colors_val)
ax1.plot(x, np.polyval(p15, x), 'b')
ax2 = plt.subplot2grid((2, 2), (1, 0), rowspan=1, colspan=2)
plt.title("Average Distance Classifier")
colors_dist = ['r' if abs(np.polyval(p15, a) - b) > max_dist else 'g' for a, b in zip(x, y) for value, max_dist in avg if a == value]
ax2.scatter(x, y, s=2, marker='o', c=colors_dist)
ax2.plot(x, np.polyval(p15, x), 'k', linewidth=1)
plt.show()