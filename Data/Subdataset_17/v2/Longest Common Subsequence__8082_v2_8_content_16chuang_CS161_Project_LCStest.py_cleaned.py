import numpy as np
np.set_printoptions(threshold=np.inf)
original_string = 'ACBBBCDCEDBADBBEABBEDAEADEBAEB'
rotated_string = 'EADEBAEBACBBBCDCEDBADBBEABBEDA'
concatenated_string = original_string + original_string
for char in concatenated_string:
    print(char)