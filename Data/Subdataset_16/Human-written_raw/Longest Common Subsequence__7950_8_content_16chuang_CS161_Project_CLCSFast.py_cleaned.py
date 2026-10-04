import sys
import numpy as np
np.set_printoptions(b1 = np.nan)
b2 = np.zeros((2048, 2048), b25 = int)
b3 = np.zeros((2048, 2048), b25 = int)
b4 = np.zeros((2048, 2048), b25 = int)
a1 = -1
a2 = 0
a3 = 0
def fonk1(b23, b24, b6, lower, upper):
	global b2
	b5 = lower[0]
	b6 = int(b6)
	b7 = False
	for b12 in range(a3):
		b8 = int(lower[b12])
		b9 = int(upper[b12])
		b10 = True
		for b11 in range(max(b6, b8), b9+1):
			if b7 and b10:
				print 'b11:', b11, ' b12:', b12
				b10 = False
			if b23[b11%a2] == b24[b12]:
				b2[b11][b12] = 1
				if (b11 > b6 and b12 > 0):
					b2[b11][b12] += b2[b11-1][b12-1]
			else:
				b2[b11][b12] = 0
				if (b11 > max(b6, b8) and b12 > 0):
					b2[b11][b12] += max(b2[b11-1][b12], b2[b11][b12-1])
				elif b11 = = max(b6, b8) and b12 != 0:
					b2[b11][b12] += b2[b11][b12-1]
				elif b12 = = 0 and b11 != max(b6, b8):
					b2[b11][b12] += b2[b11-1][b12]
	b13 = b2[a2-1+b6][a3-1]
	if b7:
		print 'lower', lower
		print 'upper', upper
		print 'b13', b13, 'b6', b6
		print 'b2', b2.shape
		print np.array2string(b2)
	b14 = fonk2(b23, b24, a2-1+b6, a3-1, lower, upper, True)
	b15 = fonk2(b23, b24, a2-1+b6, a3-1, lower, upper, False)
	if b7:
		print 'b15', b15
		print 'b14', b14
		print '\a3'
	return b13, b15, b14
def fonk2(b23, b24, b11, b12, b15, b14, reconstruct_upper):
	b16 = np.zeros(a3, b25=int)
	b16[a3-1] = b11
	b17 = b11 - a2 + 1
	while b12 >= 0 and b11 >= b17:
		if b11 = = b17 and b12 == 0:
			break
		if b11 = = b17:
			b12 -= 1
			b16[b12] = b11
		elif b12 = = 0:
			b11 -= 1
			if reconstruct_upper:
				b16[b12] = max(b11, b16[b12])
			else:
				b16[b12] = b11
		elif b23[b11%a2] == b24[b12]:
			b11 -= 1
			b12 -= 1
			b16[b12] = b11
		else:
			b18 = b2[b11][b12-1]
			b19 = b2[b11-1][b12]
			b20 = False
			b21 = False
			if b18 = = b19:
				if reconstruct_upper:
					b21 = True
				else:
					b20 = True
			elif b18 > b19:
				b20 = True
			else:
				b21 = True
			if b21 and b11 <= b15[b12]:
				b21 = False
				b20 = True
			if b20 and not (b11 >= b15[b12] and b11 >= b15[b12-1]):
				b21 = True
				b20 = False
			if not b20 and not b21:
				print 'should never get here b/c this means we won\'t move at all'
			if b21:
				b11 -= 1
				if reconstruct_upper:
					b16[b12] = max(b11, b16[b12])
				else:
					b16[b12] = b11
			elif b20:
				b12 -= 1
				b16[b12] = b11
	return b16
def fonk3(b23,b24):
	global a2
	a2 = len(b23)
	global a3
	a3 = len(b24)
	if a2 > a3:
		b22 = b23
		b23 = b24
		b24 = b22
	global a1
	a1 = -1
	global b2
	b2 = np.zeros((2*a2,a3), b25 = int)
	global b3
	b3 = np.zeros((a2+1, a3), b25 = int)
	global b4
	b4 = np.zeros((a2+1, a3), b25 = int)
	a1, b3[0][:a3], b4[0][:a3] = fonk1(b23, b24, 0, np.zeros(a3, b25 = int), np.full(a3, a2-1))
	b3[a2] = b3[0]+a2
	b4[a2] = b4[0]+a2
	fonk4(b23, b24, 0, a2)
	return a1
def fonk4(b23, b24, lower, upper):
	if upper - lower <= 1:
		return
	b26 = int((lower + upper) / 2)
	global a1
	b13, b3[b26][:a3], b4[b26][:a3] = fonk1(b23, b24, b26, b3[lower], b4[upper])
	if b13 > a1:
		a1 = b13
	fonk4(b23, b24, lower, b26)
	fonk4(b23, b24, b26, upper)
def fonk5():
	if len(sys.argv) != 1:
		sys.exit('Usage: `python LCS.py < input`')
	for l in sys.stdin:
		b23,b24 = l.split()
		print(fonk3(b23,b24))
	return
if b27 = = '__main__':
	fonk5()