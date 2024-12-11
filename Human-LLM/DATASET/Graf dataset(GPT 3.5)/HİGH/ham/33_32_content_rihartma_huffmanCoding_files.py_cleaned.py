class class1():
	def fonk1(self, name):
		b1 = ""
		b2 = open(name, 'r')
		b1 = b2.read()
		b2.close()
		return b1
	def fonk2(self, b1, name):
		b2 = open(name, 'w')
		b2.write(b1)
		b2.close()
	def fonk3(self, name, b1, b5):
		b3 = ''
		for char in b1:
			b3 = b3 + b5[char]
		b4 = ""
		for i in range(0, len(b3)-8, 8):
			b4 = b4 + chr(int(b3[i:i+8],2))
		if len(b3)%8 != 0:
			b4 = b4 + "~~~" + b3[len(b3)-1-len(b3)%8:len(b3)]
		b2 = open(name, 'w')
		b2.write(b4)
		b2.close()
	def fonk4(self, name):
		b2 = open(name, "r")
		b1 = b2.read()
		b2.close()
		b5 = {}
		b6 = b1.split(",")
		b7 = len(b6)
		a1 = 0
		while a1 < b7:
			if b6[a1] == "":
				b6[a1+1] = "," + b6[a1+1]
				del b6[a1]
				b7 -= 1
				a1 -= 1
			a1 += 1
		for pair in b6:
			b8 = pair.split("-")
			b5[b8[1]] = b8[0]
		return b5