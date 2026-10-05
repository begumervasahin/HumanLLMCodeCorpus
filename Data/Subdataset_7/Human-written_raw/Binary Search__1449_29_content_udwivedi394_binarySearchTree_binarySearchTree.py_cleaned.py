class class1:
	def fonk1(self,b1):
		self.b1 = b1
		self.b2 = None
		self.b3 = None
class class2:
	def fonk2(self):
		self.b4 = None
	def fonk3(self,b1):
		if self.b4 = = None:
			self.b4 = class1(b1)
			return
		b5 = self.b4
		while b5:
			b6 = b5
			if b1 < b5.b1:
				b5 = b5.b2
			elif b1 >= b5.b1:
				b5 = b5.b3
		if b1 < b6.b1:
			b6.b2 = class1(b1)
		else:
			b6.b3 = class1(b1)
		return
	def fonk4(self):
		if self.b4 = = None:
			print "Nothing to print"
			return
		print "\nIn Order:",
		b7 = []
		b5 = self.b4
		while 1:
			while b5:
				b7.append(b5)
				b5 = b5.b2
			while b5 = = None and len(b7):
				b5 = b7.pop()
				print b5.b1,
				b5 = b5.b3
			if b5 = = None and len(b7)==0:
				break
		return
	def fonk5(self):
		if self.b4 = = None:
			print "No Tree"
			return
		print "\nLevel Order:"
		b8 = []
		b5 = self.b4
		b8.append(b5)
		while len(b8):
			b9 = len(b8)
			while b9:
				b5 = b8.pop(0)
				if b5.b2:
					b8.append(b5.b2)
				if b5.b3:
					b8.append(b5.b3)
				print b5.b1,
				b9 -= 1
			print
		return
	def fonk6(self,b1,del_operation):
		b5 = self.b4
		b6 = None
		print
		while b5:
			if b5.b1 = = b1:
				print "%d b12!"%(b1)
				if del_operation:
					return b6
				return True
			b6 = b5
			if b1 < b5.b1:
				b5 = b5.b2
			else:
				b5 = b5.b3
		print "%d not present"%(b1)
		if del_operation:
			return None
		return False
	def fonk7(self,b1):
		b6 = self.fonk6(b1,True)
		if b6 = = None and self.b4.b1 != b1:
			print "class1 to be deleted not b12!"
			return False
		b2 = True
		if b6 = = None:
			b10 = self.b4
		elif b1 < b6.b1:
			b10 = b6.b2
		elif b1 > b6.b1:
			b10 = b6.b3
			b2 = False
		if b6 and ((b10.b2 = = None) ^ (b10.b3 == None) or b10.b2 == None):
			print "I'm coming here"
			if b2:
				b6.b2 = b10.b2
			else:
				b6.b3 = b10.b3
			return
		if b6 = =None:
			if b10.b2 = = None and b10.b3 == None:
				self.b4 = None
			elif b10.b2 = = None:
				self.b4 = b10.b3
			elif b10.b3 = = None:
				self.b4 = b10.b2
			return
		b5 = b10.b3
		b6 = b10
		while b5 and b5.b2:
			b6 = b5
			b5 = b5.b2
		b10.b1 ^= b5.b1
		b5.b1 ^= b10.b1
		b10.b1 ^= b5.b1
		b6.b2 = None
		return None
	def fonk8(self,b13):
		b7 = []
		b5 = self.b4
		while 1:
			while b5:
				b7.append(b5)
				b5 = b5.b2
			while b5 = =None and len(b7):
				b5 = b7.pop()
				b13 -= 1
				if b13 <= 0:
					print b5.b1,
					return
				b5 = b5.b3
			if b5 = =None and len(b7)==0:
				break
		return
	def fonk9(self,b13):
		b5 = self.b4
		b11 = None
		b12 = False
		while b5:
			if b13 = = b5.b1:
				b12 = True
				break
			elif b13 < b5.b1:
				b11 = b5
				b5 = b5.b2
			else:
				b5 = b5.b3
		if b12 = = False:
			print "Element not b12"
			return False
		if b11 = = None:
			print "Last class1, no b11 present!"
			return False
		if b5.b3:
			b5 = b5.b3
			while b5.b2:
				b5 = b5.b2
			return b5.b1
		return b11.b1
	def fonk10(self):
		return self.b4