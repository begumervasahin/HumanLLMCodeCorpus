import numpy as np
np.set_printoptions(threshold=np.inf)
a = 'ACBBBCDCEDBADBBEABBEDAEADEBAEB'
rotated = 'EADEBAEBACBBBCDCEDBADBBEABBEDA'
b = a + a
for char in b:
    print(char)