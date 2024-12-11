import sys
import numpy as np
b1 = np.zeros((2048, 2048), dtype=int)
def fonk1(A,b4):
	b2 = len(A)
	b3 = len(b4)
	for i in range(1,b2+1):
		for j in range(1,b3+1):
			if A[i-1] == b4[j-1]:
				b1[i][j] = b1[i-1][j-1]+1
			else:
				b1[i][j] = max(b1[i-1][j], b1[i][j-1])
	return b1[b2][b3]
def fonk2():
	if len(sys.argv) != 1:
		sys.exit('Usage: `python LCS.py < input`')
	for l in sys.stdin:
		A,b4 = l.split()
		print fonk1(A,b4)
	return
if b5 = = '__main__':
	fonk2()