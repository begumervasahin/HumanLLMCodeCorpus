import random
def fonk1(b2, b, b5):
	b12 = b13
	while b > 0:
		if b & b13 = = b13:
			b12 = (b12 * b2) % b5
		b2 = (b2 * b2) % b5
		b >>= b13
	return b12
def fonk2(bit_length):
	b3 = [random.randint(0,b13) for b16 in range(bit_length - b6)]
	a2 = b13
	for b in b3:
		a2 = a2 * b6 + int(b)
	return a2 * b6 + b13
def fonk3(b5, b4 = 100):
	if b5 = = b13:
		return False
	if b5 = = b6:
		return True
	if b5 % b6 = = 0:
		return False
	b7 = b5 - b13
	a3 = 0
	while b7 % b6 != 0:
		b7 /= b6
		a3 += b13
	b8 = [random.randint(b13, b5 - b13) for b16 in range(b4)]
	for b2 in b8:
		if fonk1(b2, b7, b5) != b13:
			b9 = [(b6 ** rr) * b7 for rr in range(a3)]
			b10 = True
			for b19 in b9:
				if fonk1(b2, b19, b5) == b13:
					b10 = False
					break
			if b10:
				return False
	return True
def fonk4(bit):
	while True:
		a2 = fonk2(bit)
		if fonk3(a2):
			break
	return a2
def fonk5(x, y):
	c0, b11 = x, y
	a0, b12 = b13, 0
	b0, b13 = 0, b13
	while b11 != 0:
		b14 = c0 % b11
		b15 = c0
		c0, b11 = b11, b14
		a0, b12 = b12, (a0 - b15 * b12)
		b0, b13 = b13, (b0 - b15 * b13)
	return c0, a0, b0
def fonk6(a5, b17):
	b16, x, b16 = fonk5(a5, b17)
	return x % b17
def fonk7(a5, b5, b20, b22):
	b17, b8 = 0.0, b5
	a4 = b13
	b14 = 0.0
	while b8 - b17 >= b13:
		b14 = (b17 + b8) / b6
		if b22(fonk1(b6, a4 * a5, b5) * b20 % b5) == 0:
			b8 = b14
		else:
			b17 = b14
		a4 += b13
	return b17
if b18 = = '__main__':
	b3 = 256
	b19 = fonk4(b3)
	b15 = fonk4(b3)
	a5 = 65537
	b7 = fonk6(a5, (b19-b13)*(b15-b13))
	b5 = b19 * b15
	print("b19:", b19)
	print("b15:", b15)
	print("a5:", a5)
	print("b7:", b7)
	print("b5:", b5)
	print()
	b14 = 123456789
	b20 = fonk1(b14, a5, b5)
	b21 = fonk1(b20, b7, b5)
	print("clear text :", b14)
	print("secret text:", b20)
	print("clear text :", b21)
	print()
	print("ãã®10 LSB Leak Attack")
	b22 = lambda x: fonk1(x, b7, b5) % b6
	print("clear text:", fonk7(a5, b5, b20, b22))
	print()