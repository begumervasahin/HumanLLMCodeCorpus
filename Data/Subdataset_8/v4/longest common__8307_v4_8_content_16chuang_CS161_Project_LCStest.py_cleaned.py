import numpy as np
np.set_printoptions(threshold=np.nan)
original = 'ACBBBCDCEDBADBBEABBEDAEADEBAEB'
rotated = 'EADEBAEBACBBBCDCEDBADBBEABBEDA'
duplicated = original + original
for char in duplicated:
    print(char)