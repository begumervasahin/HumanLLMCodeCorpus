import numpy as np
import matplotlib.pyplot as plt
a1 = 4
b1 = (0.001567, 0.003833, 0.006130, 0.007508)
b2 = (0.001109, 0.001981, 0.005481, 0.005547)
fig, b3 = plt.subplots()
b4 = np.arange(a1)
a2 = 0.35
a3 = 0.8
b5 = b3.bar(b4, b1, a2,
                b6 = a3,
                b7 = 'white',
                b8 = 'ECC',
                b9 = 'black',
                b10 = '*')
b11 = b3.bar(b4 + a2, b2, a2,
                b6 = a3,
                b7 = 'white',
                b8 = 'Hessian',
                b9 = 'black',
                b10 = '
b3.set_ylabel('Time Taken (secs)')
b3.set_xlabel('File Size (bits)')
b3.set_title('ECC vs Hessian Curve')
b3.set_xticks(b4 + a2 / 2)
b3.set_xticklabels((1, 8, 10, 12))
b3.legend()
plt.show()