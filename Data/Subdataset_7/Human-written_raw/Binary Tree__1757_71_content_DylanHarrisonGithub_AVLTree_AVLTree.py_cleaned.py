class class1(object):
	def fonk1(self, b1):
		self.b1 = b1
		self.a1 = 1
		self.a2 = 0
		self.a3 = 0
		self.a4 = -1
		self.b2 = None
		self.b3 = None
		self.b4 = None
	def fonk2(self):
		return ((self.b2 != None) and (self.b2.b3 = = self))
	def fonk3(self):
		return ((self.b2 != None) and (self.b2.b4 = = self))
	def fonk4(self):
		return ((self.b3 = = None) and (self.b4 == None))
	def fonk5(self):
		return (self.b2 = = None)
	def fonk6(self):
		return ((self.b2 != None) and (self.b2.b2 != None))
	def fonk7(self):
		a5 = -1
		if (self.b3 != None):
			a5 = self.b3.a3
		return a5
	def fonk8(self):
		a6 = -1
		if (self.b4 != None):
			a6 = self.b4.a3
		return a6
	def fonk9(self):
		a5 = self.fonk7()
		a6 = self.fonk8()
		if (a5 > a6):
			return a5
		else:
			return a6
	def fonk10(self):
		a5 = -1
		a6 = -1
		if (self.b3 != None):
			a5 = self.b3.a3
		if (self.b4 != None):
			a6 = self.b4.a3
		if (abs(a6 - a5) > 1):
			return False
		else:
			return True
	def fonk11(self):
		b5 = self
		if (b5.b3 != None):
			b5 = b5.b3
			while (b5.b4 != None):
				b5 = b5.b4
			return b5
		else:
			return null
	def fonk12(self):
		b5 = self
		if (b5.b4 != None):
			b5 = b5.b4
			while (b5.b3 != None):
				b5 = b5.b3
			return b5
		else:
			return null
	def fonk13(self):
		b5 = self
		if (b5.fonk3()):
			while (b5.fonk3()):
				b5 = b5.b2
			if (b5.fonk2()):
				return b5.b2
			else:
				return None
		else:
			return None
	def fonk14(self):
		b5 = self
		if (b5.fonk2()):
			while (b5.fonk2()):
				b5 = b5.b2
			if (b5.fonk3()):
				return b5.b2
			else:
				return None
		else:
			return None
	def fonk15(self):
		if (self.fonk5()):
			if (self.b4 != None):
				return self.fonk12()
			else:
				return None
		elif (self.fonk2()):
			if (self.b4 != None):
				return self.fonk12()
			else:
				return self.b2
		else:
			if (self.b4 != None):
				return self.fonk12()
			else:
				return self.fonk13()
	def fonk16(self):
		if (self.fonk5()):
			if (self.b3 != None):
				return self.fonk11()
			else:
				return None
		elif (self.fonk2()):
			if (self.b3 != None):
				return self.fonk11()
			else:
				return self.fonk14()
		else:
			if (self.b3 != None):
				return self.fonk11()
			else:
				return self.b2
	def fonk17(self, delegateTree, b1):
		if (self.b1 = = b1):
			self.a1 += 1
			return None
		elif (self.b1 > b1):
			if (self.b3 = = None):
				self.b3 = class1(b1)
				self.b3.b2 = self
				self.b3.a2 = self.a2+1
				delegateTree.a7 += 1
				return self.b3
			else:
				return self.b3.fonk25(delegateTree, b1)
		else:
			if (self.b4 = = None):
				self.b4 = class1(b1)
				self.b4.b2 = self
				self.b4.a2 = self.a2+1
				delegateTree.a7 += 1
				return self.b4
			else:
				return self.b4.fonk25(delegateTree, b1)
	def fonk18(self, delegateTree):
		if (self.fonk4()):
			if (self.fonk2()):
				self.b2.b3 = None
				self.b2.fonk20(delegateTree)
			elif (self.fonk3()):
				self.b2.b4 = None
				self.b2.fonk20(delegateTree)
			else:
				delegateTree.b6 = None
		else:
			if ((self.b3 != None) and (self.b4 != None)):
				if (self.fonk16().fonk4()):
					self.fonk19(delegateTree, self.fonk16().fonk26(delegateTree))
				else:
					self.fonk19(delegateTree, self.fonk15().fonk26(delegateTree))
			else:
				if (self.b4 != None):
					self.fonk19(delegateTree, self.fonk15().fonk26(delegateTree))
				else:
					self.fonk19(delegateTree, self.fonk16().fonk26(delegateTree))
		return self
	def fonk19(self, delegateTree, b16):
		b16.b2 = self.b2
		b16.b3 = self.b3
		b16.b4 = self.b4
		b16.a3 = self.a3
		b16.a2 = self.a2
		if (self.b3 != None):
			self.b3.b2 = b16
		if (self.b4 != None):
			self.b4.b2 = b16
		if (self.fonk2()):
			self.b2.b3 = b16
		if (self.fonk3()):
			self.b2.b4 = b16
		if (self.fonk5()):
			delegateTree.b6 = b16
	def fonk20(self, delegateTree):
		self.a3 = self.fonk9() + 1
		if (self.fonk10() == False):
			self.fonk21(delegateTree)
		if (self.b2 != None):
			self.b2.fonk20(delegateTree)
	def fonk21(self, delegateTree):
		b7 = self.b2
		if (self.fonk7() > self.fonk8()):
			if (self.b3.fonk7() > self.b3.fonk8()):
				b8 = self
				b9 = self.b3
				b10 = self.b3.b3
				b11 = b10.b3
				b12 = b10.b4
				b13 = b9.b4
				b14 = b8.b4
			else:
				b8 = self
				b9 = self.b3.b4
				b10 = self.b3
				b11 = b10.b3
				b12 = b9.b3
				b13 = b9.b4
				b14 = b8.b4
			if (b8.fonk2()):
				b7.b3 = b9
			elif (b8.fonk3()):
				b7.b4 = b9
			else:
				delegateTree.b6 = b9
		else:
			if (self.b4.fonk8() > self.b4.fonk7()):
				b8 = self.b4.b4
				b9 = self.b4
				b10 = self
				b11 = b10.b3
				b12 = b9.b3
				b13 = b8.b3
				b14 = b8.b4
			else:
				b8 = self.b4
				b9 = self.b4.b3
				b10 = self
				b11 = b10.b3
				b12 = b9.b3
				b13 = b9.b4
				b14 = b8.b4
			if (b10.fonk2()):
				b7.b3 = b9
			elif (b10.fonk3()):
				b7.b4 = b9
			else:
				delegateTree.b6 = b9
		b9.b2 = b7
		b9.b3 = b10
		b9.b4 = b8
		b10.b2 = b9
		b8.b2 = b9
		if (b11 != None):
			b11.b2 = b10
		if (b12 != None):
			b12.b2 = b10
		if (b13 != None):
			b13.b2 = b8
		if (b14 != None):
			b14.b2 = b8
		b10.b3 = b11
		b10.b4 = b12
		b8.b3 = b13
		b8.b4 = b14
		b10.a3 = b10.fonk9()+1
		b8.a3 = b8.fonk9()+1
		b9.a3 = b9.fonk9()+1
		if (b7 != None):
			b9.fonk22(b7.a2+1)
		else:
			b9.fonk22(0)
	def fonk22(self, a2):
		if (self.b3 != None):
			self.b3.fonk22(a2+1)
		self.a2 = a2
		if (self.b4 != None):
			self.b4.fonk22(a2+1)
class class2(object):
	def fonk23(self):
		self.b6 = None
		self.a7 = 0
		self.b15 = None
	def fonk24(self, b1):
		if (self.b6 != None):
			b5 = self.b6
			while (b5 != None):
				if (b5.b1 = = b1):
					return b5
				elif (b5.b1 > b1):
					b5 = b5.b3
				else:
					b5 = b5.b4
			return b5
		else:
			return None
	def fonk25(self, b1):
		if (self.b6 = = None):
			self.b6 = class1(b1)
			self.b6.a3 = 0
			self.b6.a2 = 0
			self.a7 = 1
		else:
			b16 = self.b6.fonk25(self, b1)
			if (b16 != None):
				b16.fonk20(self)
	def fonk26(self, b1):
		b17 = self.fonk24(b1)
		if (b17 != None):
			b17.fonk26(self)
			self.a7 -= 1
		return b17
	def fonk27(self):
		if (self.b6 != None):
			b5 = self.b6
			while (b5.b3 != None):
				b5 = b5.b3
			while (b5 != None):
				print(b5.b1)
				b5 = b5.fonk15()
	def fonk28(self):
		if (self.b6 != None):
			b5 = self.b6
			while (b5.b3 != None):
				b5 = b5.b3
			return b5
		else:
			return None
	def fonk29(self):
		if (self.b6 != None):
			b5 = self.fonk28()
			a8 = 0
			while (b5 != None):
				b5.a4 = a8
				a8 += 1
				b5 = b5.fonk15()