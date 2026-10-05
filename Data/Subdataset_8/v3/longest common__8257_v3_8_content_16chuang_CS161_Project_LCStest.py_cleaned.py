
import numpy as np
np.set_printoptions(threshold=np.nan)
original_string = 'ACBBBCDCEDBADBBEABBEDAEADEBAEB'
rotated_string = 'EADEBAEBACBBBCDCEDBADBBEABBEDA'
doubled_string = original_string + original_string
for char in doubled_string:
    print(char)