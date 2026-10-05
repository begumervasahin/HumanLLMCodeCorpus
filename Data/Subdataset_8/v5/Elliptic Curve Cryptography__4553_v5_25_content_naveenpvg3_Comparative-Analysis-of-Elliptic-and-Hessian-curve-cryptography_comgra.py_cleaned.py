
import numpy as np
import matplotlib.pyplot as plt
file_sizes = (1, 8, 10, 12)
ecc_times = (0.001567, 0.003833, 0.006130, 0.007508)
hes_times = (0.001109, 0.001981, 0.005481, 0.005547)
fig, ax = plt.subplots()
index = np.arange(len(file_sizes))
bar_width = 0.35
opacity = 0.8
rects1 = ax.bar(index, ecc_times, bar_width, alpha=opacity, color='white', edgecolor='black', hatch="*", label='ECC')
rects2 = ax.bar(index + bar_width, hes_times, bar_width, alpha=opacity, color='white', edgecolor='black', hatch="
ax.set_ylabel('Time taken (seconds)')
ax.set_xlabel('File size (bits)')
ax.set_title('ECC vs Hessian Curve')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(file_sizes)
ax.legend()
plt.show()