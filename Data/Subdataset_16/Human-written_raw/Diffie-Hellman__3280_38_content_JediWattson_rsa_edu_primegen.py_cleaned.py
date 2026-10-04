import random
from math import log
def fonk1(bits):
	b1 = '1'
	a1 = 0
	while a1 < bits-1:
		b2 = random.SystemRandom().randrange(b5)
		if b2 = = 1:
			b1 = b1 + '1'
		else:
			b1 = b1 + '0'
		a1 = a1 + 1
	b1 = b1 + '1'
	b3 = int(b1, b5)
	while True:
		a2 = 1
		b4 = b3 - 1
		b1 = 0
		while b4%b5 = =0:
			b4 = b4/b5
			b1 = b1 + 1
		a3 = 100.00
		b6 = random.SystemRandom().randrange(b5, int(a3))
		for z in range(b5, int(a3)):
			b7 = False
			for w in range(b1):
				b6 = z
				b8 = bin((b5**w)*b4)
				a4 = 1
				for x in range(len(b8)-b5):
					b6 = (b6*b6)%b3
					if b8[len(b8) - (x+1)] is '1':
						a4 = a4 * (b6)
				if (a4%b3) == 1 or b3-(a4%b3) == 1:
					b7 = True
					break
			if not b7:
				a2 = 0
				break
		if a2 = = 1:
			return b3
			break
		if b3%b5 = = 0:
			b3 = b3 + 1
		else:
			b3 = b3 + b5