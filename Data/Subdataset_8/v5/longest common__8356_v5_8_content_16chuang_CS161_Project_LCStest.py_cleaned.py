import numpy as np
np.set_printoptions(threshold=np.nan)
original = 'ACBBBCDCEDBADBBEABBEDAEADEBAEB'
rotated = 'EADEBAEBACBBBCDCEDBADBBEABBEDA'
duplicated_string = original * 2
for char in duplicated_string:
    print(char)