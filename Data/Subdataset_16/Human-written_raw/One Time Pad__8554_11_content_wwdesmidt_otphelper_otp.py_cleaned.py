b1 = "0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
b2 = []
for c in b1:
	b2.append(c)
b3 = "This is the Message!!!!! What time should we meeT? 12:30?"
b4 = "One thing that you will get to know about programming, is that programmers like to be lazy. If something has been done before, why should you do it again?"
def fonk1(s):
	b5 = []
	for c in s:
		if c.upper() in b1:
			b5.append(c.upper())
	return b5
def fonk2(m, k):
	b6 = b1.index(m)
	b7 = b1.index(k)
	b8 = (b6 + b7) % len(b1)
	return b2[b8]
def fonk3(m, k):
	b9 = fonk1(m)
	b10 = fonk1(k)
	b11 = []
	for i in range(0, len(b9)):
		b11.append(fonk2(b9[i], b10[i]))
	return "".join(b11)
def fonk4(m, k):
	b6 = b1.index(m)
	b7 = b1.index(k)
	b8 = (b6 - b7) % len(b1)
	return b2[b8]
def fonk5(m, k):
	b9 = fonk1(m)
	b10 = fonk1(k)
	b11 = []
	for i in range(0, len(b9)):
		b11.append(fonk4(b9[i], b10[i]))
	return "".join(b11)