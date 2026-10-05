import pickle
import matplotlib.pyplot as plt
import numpy as np
from math import log
from keys500 import key
b1 = len(key)
with open('RB500.pickle', 'rb') as handle:
    [pairs, pair_found, total_key_find_good] = pickle.load(handle)
b2 = np.zeros(len(pairs))
for i in range(len(pairs)):
    b2[i] = sum(pair_found <= i)
b3 = b2  * 1.0 / b1
b4 = range(1,len(pairs)+1)
with open('RB500Struct.pickle', 'rb') as handle:
    [pairs, pair_found, total_key_find_good] = pickle.load(handle)
b2 = np.zeros(len(pairs))
for i in range(len(pairs)):
    b2[i] = sum(pair_found <= i)
b5 = b2  * 1.0 / b1
b6 = range(1,len(pairs)+1)
w, b7 = plt.figaspect(0.5)
plt.figure(b8 = (w, b7))
plt.plot(b4, b3, 'b-', b9 = 'i.i.d pairs')
plt.plot(b6, b5, 'r--', b9 = 'structured pairs')
plt.legend(b10 = 'upper left')
plt.ylabel('Attack Success Probability')
plt.xlabel('Number of Plaintext Pairs')
plt.savefig('RB.png', b11 = 600, format='png')
plt.show()