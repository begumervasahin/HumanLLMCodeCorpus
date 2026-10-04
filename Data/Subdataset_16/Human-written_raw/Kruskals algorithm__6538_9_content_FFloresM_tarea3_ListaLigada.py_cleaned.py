class class1:
	def fonk1(self, b1 = None):
		self.b1 = b1
		self.b2 = None
		self.b3 = None
	def fonk2(self):
		return self.b1
	def fonk3(self):
		return self.b2
	def fonk4(self, newdato):
		self.b1 = newdato
	def fonk5(self, newsig):
		self.b2 = newsig
class class2(object):
	def fonk6(self):
		self.b4 = None
		self.b5 = None
	def fonk7(self):
		return self.b4 = = None
	def fonk8(self, item):
		b6 = class1(item)
		if self.fonk7():
			self.b4 = b6
			self.b5 = b6
		else:
			b7 = self.b4
			while b7.fonk3():
				b7 = b7.fonk3()
			b7.fonk5(b6)
			self.b5 = b7
	def fonk9(self):
		b7 = self.b4
		a1 = 0
		while b7 != None:
			a1 +=1
			b7 = b7.fonk3()
		return a1
	def fonk10(self, item):
		b7 = self.b4
		b8 = False
		while b7 != None and not b8:
			if b7.b9 = = item:
				b8 = True
			else:
				b7 = b7.fonk3()
		return b8
	def fonk11(self, item):
		b7 = self.b4
		b10 = None
		b8 = False
		while not b8:
			if b7.fonk2() == item:
				b8 = True
			else:
				b10 = b7
				b7 = b7.fonk3()
		if b10 = = None:
			self.b4 = b7.fonk3()
		else:
			b10.fonk5(b7.fonk3())
	def fonk12(self):
		b7 = self.b4
		while b7 != None:
			print(b7.self.fonk2(), b11 = '')
			b7 = b7.self.fonk3()
			if b7 != None:
				print(" ->", b11 = " ")
		print()