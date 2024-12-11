import numpy as np
import matplotlib.pyplot as plt
a1 = 4
b1 = (0.001567,0.003833,0.006130,0.007508)
b2 = (0.001109,0.001981,0.005481,0.005547)
fig, b3 = plt.subplots()
b4 = np.arange(a1)
a2 = 0.35
a3 = 0.8
b5 = plt.bar(b4, b1, a2,
                 b6 = a3,
                 b7 = 'white',
                 b8 = 'ECC',edgecolor='black', hatch="*")
b9 = plt.bar(b4 + a2, b2, a2,
                 b6 = a3,
                 b7 = 'white',
                 b8 = 'Hessian',edgecolor='black', hatch="
plt.ylabel('time taken in secs')
plt.xlabel('file size in bits')
plt.title('ECC vs Hessian Curve')
plt.xticks(b4 + a2, (1,8,10,12))
plt.legend()
plt.show()