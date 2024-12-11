
import numpy as np
import matplotlib.pyplot as plt
b1 = (1, 8, 10, 12)
b2 = (0.001567, 0.003833, 0.006130, 0.007508)
b3 = (0.001109, 0.001981, 0.005481, 0.005547)
fig, b4 = plt.subplots()
b5 = np.arange(len(b1))
a1 = 0.35
a2 = 0.8
b6 = b4.bar(b5, b2, a1, alpha=a2, color='white', edgecolor='black', hatch="*", label='ECC')
b7 = b4.bar(b5 + a1, b3, a1, alpha=a2, color='white', edgecolor='black', hatch="
b4.set_ylabel('Time taken (seconds)')
b4.set_xlabel('File size (bits)')
b4.set_title('ECC vs Hessian Curve')
b4.set_xticks(b5 + a1 / 2)
b4.set_xticklabels(b1)
b4.legend()
plt.show()