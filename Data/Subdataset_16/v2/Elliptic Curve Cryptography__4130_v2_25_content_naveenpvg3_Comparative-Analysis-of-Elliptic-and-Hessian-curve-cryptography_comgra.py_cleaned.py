import numpy as np
import matplotlib.pyplot as plt
b1 = ['1 bit', '8 bits', '10 bits', '12 bits']
b2 = [0.001567, 0.003833, 0.006130, 0.007508]
b3 = [0.001109, 0.001981, 0.005481, 0.005547]
b4 = len(b1)
fig, b5 = plt.subplots()
b6 = np.arange(b4)
a1 = 0.35
a2 = 0.8
b7 = b5.bar(b6, b2, a1,
                  b8 = a2,
                  b9 = 'white',
                  b10 = 'black',
                  b11 = 'ECC',
                  b12 = '*')
b13 = b5.bar(b6 + a1, b3, a1,
                  b8 = a2,
                  b9 = 'white',
                  b10 = 'black',
                  b11 = 'Hessian',
                  b12 = '
b5.set_xlabel('File Size')
b5.set_ylabel('Time Taken (secs)')
b5.set_title('ECC vs Hessian Curve Performance')
b5.set_xticks(b6 + a1 / 2)
b5.set_xticklabels(b1)
b5.legend()
plt.show()