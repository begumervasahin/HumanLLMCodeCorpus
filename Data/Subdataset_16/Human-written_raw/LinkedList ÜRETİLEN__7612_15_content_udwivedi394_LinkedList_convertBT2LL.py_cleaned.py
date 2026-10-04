class class1:
	def fonk1(self,b1):
		self.b1 = b1
		self.b2 = None
		self.b3 = None
class class2:
	def fonk2(self):
		self.b4 = None
	def fonk3(self,b1):
		pass
	def fonk4(self):
		b5 = []
		b6 = self.b4
		while len(b5):
			pass
def fonk5(b4):
	b6 = b4
	b5 = []
	while 1:
		while b6:
			b5.append(b6)
			b6 = b6.b2
		while b6 = = None and len(b5):
			b6 = b5.pop()
			print b6.b1,
			b6 = b6.b3
		if len(b5) == 0 and b6 = = None:
			break
	return
def fonk6(b4):
	b6 = b4
	b5 = []
	b7 = None
	b8 = None
	b9 = None
	while 1:
		while b6:
			b5.append(b6)
			b6 = b6.b2
		while b6 = = None and len(b5):
			b6 = b5.pop()
			b6.b2 = b7
			if b7:
				b7.b3 = b6
			else:
				b8 = b6
			b7 = b6
			print b6.b1,
			if b6.b3 = = None:
				b9 = b6
			b6 = b6.b3
		if len(b5) == 0 and b6 = = None:
			b9.b3 = b8
			b8.b2 = b9
			break
	return b8
def fonk7(b4):
	b6 = b4
	b10 = True
	while b6 and (b10 or b6!=b4):
		print b6.b1,"->",
		b6 = b6.b3
		b10 = False
	print "None"
	return
b4 = class1(10)
b4.b2 = class1(12)
b4.b2.b2 = class1(25)
b4.b2.b3 = class1(30)
b4.b3 = class1(15)
b4.b3.b2 = class1(36)
fonk5(b4)
print
b8 = fonk6(b4)
print
fonk7(b8)