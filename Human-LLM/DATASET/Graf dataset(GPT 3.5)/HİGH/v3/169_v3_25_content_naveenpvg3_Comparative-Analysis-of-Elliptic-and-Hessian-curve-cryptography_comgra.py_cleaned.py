import numpy as np
import matplotlib.pyplot as plt
a1 = 4
b1 = (0.001567, 0.003833, 0.006130, 0.007508)
b2 = (0.001109, 0.001981, 0.005481, 0.005547)
fig, b3 = plt.subplots()
b4 = np.arange(a1)
a2 = 0.35
a3 = 0.8
b5 = b3.bar(b4, b1, a2, alpha=a3, color='white', edgecolor='black', hatch="*", label='ECC')
b6 = b3.bar(b4 + a2, b2, a2, alpha=a3, color='white', edgecolor='black', hatch="
b3.set_ylabel('Time taken (seconds)')
b3.set_xlabel('File size (bits)')
b3.set_title('ECC vs Hessian Curve')
b3.set_xticks(b4 + a2)
b3.set_xticklabels((1, 8, 10, 12))
b3.legend()
plt.show()