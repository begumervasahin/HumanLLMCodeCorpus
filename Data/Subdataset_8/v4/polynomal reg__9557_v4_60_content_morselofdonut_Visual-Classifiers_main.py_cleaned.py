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
ax2 = plt.subplot2grid((2, 2), (1, 0), rowspan=1, colspan=2)
colors_val = ['r' if b > np.polyval(p15, a) else 'b' for a, b in zip(x, y)]
ax1.scatter(x, y, s=2, marker='o', c=colors_val)
ax1.plot(x, np.polyval(p15, x), 'k', linewidth=1)
ax1.set_title("Value Classifier")
colors_dist = ['r' if abs(np.polyval(p15, a) - b) > max_dist else 'b' for a, b in zip(x, y) for value, max_dist in avg if a == value]
ax2.scatter(x, y, s=2, marker='o', c=colors_dist)
ax2.plot(x, np.polyval(p15, x), 'k', linewidth=1)
ax2.set_title("Average Distance Classifier")
plt.show()