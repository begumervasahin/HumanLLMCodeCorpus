import numpy as np
import matplotlib.pyplot as plt
a1 = 4
b1 = [1, 8, 10, 12]
b2 = (0.001567, 0.003833, 0.006130, 0.007508)
b3 = (0.001109, 0.001981, 0.005481, 0.005547)
fig, b4 = plt.subplots()
b5 = np.arange(a1)
a2 = 0.35
a3 = 0.8
b6 = b4.bar(b5, b2, a2,
                  b7 = a3,
                  b8 = 'white',
                  b9 = 'black',
                  b10 = 'ECC',
                  b11 = '*')
b12 = b4.bar(b5 + a2, b3, a2,
                  b7 = a3,
                  b8 = 'white',
                  b9 = 'black',
                  b10 = 'Hessian',
                  b11 = '
b4.set_xlabel('File Size (bits)')
b4.set_ylabel('Time Taken (secs)')
b4.set_title('ECC vs Hessian Curve Performance')
b4.set_xticks(b5 + a2 / 2)
b4.set_xticklabels(b1)
b4.legend()
plt.show()