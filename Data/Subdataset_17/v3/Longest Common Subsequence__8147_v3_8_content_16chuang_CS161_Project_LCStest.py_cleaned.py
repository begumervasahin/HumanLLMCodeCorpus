import numpy as np
np.set_printoptions(threshold=np.inf)
original_string = 'ACBBBCDCEDBADBBEABBEDAEADEBAEB'
rotated_string = 'EADEBAEBACBBBCDCEDBADBBEABBEDA'
doubled_string = original_string * 2
for character in doubled_string:
    print(character)