import sys
import numpy as np
b1 = np.zeros((2048, 2048), dtype=int)
def fonk1(A,b7):
	b2 = len(A)
	b3 = len(b7)
	for i in range(1,b2+1):
		for j in range(1,b3+1):
			if A[i-1] == b7[j-1]:
				b1[i][j] = b1[i-1][j-1]+1
			else:
				b1[i][j] = max(b1[i-1][j], b1[i][j-1])
	return b1[b2][b3]
def fonk2(A, b7):
	b4 = fonk1(A, b7)
	for i in range(0, len(A)):
		b5 = A[i:] + A[:i];
		b6 = fonk1(b5, b7)
		if b6 > b4:
			b4 = b6
	return b4
def fonk3():
	if len(sys.argv) != 1:
		sys.exit('Usage: `python LCS.py < input`')
	for l in sys.stdin:
		A,b7 = l.split()
		print (fonk2(A, b7))
	return
if b8 = = '__main__':
	fonk3()