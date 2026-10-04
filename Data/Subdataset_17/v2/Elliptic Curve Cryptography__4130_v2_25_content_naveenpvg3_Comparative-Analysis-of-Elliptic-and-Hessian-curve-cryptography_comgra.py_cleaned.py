import numpy as np
import matplotlib.pyplot as plt
file_sizes = ['1 bit', '8 bits', '10 bits', '12 bits']
ecc_time = [0.001567, 0.003833, 0.006130, 0.007508]
hes_time = [0.001109, 0.001981, 0.005481, 0.005547]
n_groups = len(file_sizes)
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
bars_ecc = ax.bar(index, ecc_time, bar_width,
                  alpha=opacity,
                  color='white',
                  edgecolor='black',
                  label='ECC',
                  hatch='*')
bars_hes = ax.bar(index + bar_width, hes_time, bar_width,
                  alpha=opacity,
                  color='white',
                  edgecolor='black',
                  label='Hessian',
                  hatch='
ax.set_xlabel('File Size')
ax.set_ylabel('Time Taken (secs)')
ax.set_title('ECC vs Hessian Curve Performance')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(file_sizes)
ax.legend()
plt.show()