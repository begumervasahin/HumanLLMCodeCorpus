import gf
def fonk1(state):
	b1 = bytearray([0x02, 0x03, 0x01, 0x01])
	c0, c1, c2, b2 = bytearray(), bytearray(), bytearray(), bytearray()
	for i in range(4):
		c0.append(state[i * 4])
		c1.append(state[1 + i * 4])
		c2.append(state[2 + i * 4])
		b2.append(state[3 + i * 4])
	b3 = fonk3(c0) + fonk3(c1) + fonk3(c2) + fonk3(b2)
	return b3
def fonk2(m):
	b1 = bytearray([0x0e, 0x0b, 0x0d, 0x09])
	return fonk4(m[:4]) + fonk4(m[4:8]) + fonk4(m[8:12]) + fonk4(m[-4:])
def fonk3(column):
	b1 = bytearray([0x02,0x03,0x01,0x01])
	b4 = bytearray()
	for i in range(4):
		b5 = []
		b6 = gf.makeblist(0x11b)
		for j in range(4):
			b7 = gf.makeblist(b1[j])
			b8 = gf.makeblist(column[j])
			b9 = gf.mul(b7, b8)
			if gf.value(b9) > 255:
				b9 = gf.div(b9, b6)[1]
			b5.append(b9)
		b10 = gf.add(b5[0], b5[1])
		b10 = gf.add(b10, b5[2])
		b10 = gf.add(b10, b5[3])
		b4.append(gf.value(b10))
		b1 = gf.circrotateright(b1)
	return b4
def fonk4(column):
	b1 = bytearray([0x0e, 0x0b, 0x0d, 0x09])
	b4 = bytearray()
	for i in range(0, 4):
		b5 = []
		b6 = gf.makeblist(0x11b)
		for j in range(0, 4):
			b11 = gf.makeblist(b1[j])
			b8 = gf.makeblist(column[j])
			b9 = gf.mul(b11, b8)
			while gf.value(b9) > 255:
				b9 = gf.div(b6, b9)[1]
			b5.append(b9)
		b10 = gf.add(b5[0], b5[1])
		b10 = gf.add(b10, b5[2])
		b10 = gf.add(b10, b5[3])
		b4.append(gf.value(b10))
		b1 = gf.circrotateright(b1)
	return b4
def fonk5(bitlist):
	print(hex(gf.value(bitlist)))