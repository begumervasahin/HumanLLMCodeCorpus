import numpy as np
np.set_printoptions(b1 = np.nan)
b2 = 'ACBBBCDCEDBADBBEABBEDAEADEBAEB'
b3 = 'EADEBAEBACBBBCDCEDBADBBEABBEDA'
b4 = b2 + b2
for i in range(len(b4)):
	print b4[i]