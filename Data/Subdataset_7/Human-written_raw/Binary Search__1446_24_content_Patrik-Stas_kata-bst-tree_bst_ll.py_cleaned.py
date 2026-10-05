class class1:
	def fonk1(self, b3, b2, b1 = None):
		self.b2 = b2
		self.b3 = b3
		self.b4 = None
		self.b5 = None
		self.b1 = b1;
	def fonk2(self, b6):
		if (b6 = = self.b4):
			self.b4 = None
		elif (b6 = = self.b5):
			self.b5 = None
	def fonk3(self):
		b7 = "        " if (self.b4 == None) else  "b4: " + str(self.b4.b2)
		b8 = "         " if (self.b5 == None) else  "b5: " + str(self.b5.b2)
		b9 = "   ROOT" if (self.b1 == None) else "   b1 " + str(self.b1.b2)
		print "class1(" + str(self.b2) + ")  " + b7 + "  " + b8 + b9
	def fonk4(self):
		return (self.b4 = = None) and (self.b5 == None)
	def fonk5(self):
		return self.b1 = = None
	def fonk6(self, child_node):
		self.b5 = child_node
		child_node.b1 = self
	def fonk7(self, child_node):
		self.b4 = child_node
		child_node.b1 = self
	def fonk8(self, b10, new_child):
		if (b10 = = self.b4):
			self.fonk7(new_child)
		elif (b10 = = self.b5):
			self.fonk6(new_child)
		else:
			raise Exception("b10 b16 not found")
		b10.b1 = None
class class2:
	def fonk9(self, b11):
		self.b11 = b11
		self.a1 = 40
	def fonk10(self):
		print "foo"
	def fonk11(self, b12 = False):
		self.fonk12(self.b11.b14, b12)
	def fonk12(self, b13, b12):
		if (b13 = = None):
			raise Exception("Passing None as b16 to preorder print is not expected.")
		if (b12):
			b13.fonk3()
		else:
			print str(b13.b2) + " ",
		if (b13.b4 != None):
			self.fonk12(b13.b4, b12)
		if (b13.b5 != None):
			self.fonk12(b13.b5, b12)
class class3:
	def fonk13(self):
		self.b14 = None
	def fonk14(self):
		return self.fonk15(self.b14)
	def fonk15(self, b15):
		if (b15 != None):
			return 1 + self.fonk15(b15.b4) +  self.fonk15(b15.b5)
		else:
			return 0
	def fonk16(self, b3, b2):
		if (b3 = = None or b2 == None):
			raise Exception("Insert b3 or b2 is null.")
		elif (self.b14 = = None):
			self.b14 = class1(b3, b2, b1=None)
		else:
			self.fonk17(self.b14, b3, b2)
	def fonk17(self, b15, b3, b2):
		if (b15.b3 = = b3):
			raise Exception("Duplicate b3 " + str(b3))
		else:
			if (b3 < b15.b3):
				if (b15.b4 = = None):
					b15.fonk7(class1(b3, b2))
				else:
					self.fonk17(b15.b4, b3, b2)
			else:
				if (b15.b5 = = None):
					b15.fonk6(class1(b3, b2))
				else:
					self.fonk17(b15.b5, b3, b2)
	def fonk18(self, b15, search_key):
		if (b15 = = None):
			return None;
		if (b15.b3 = = search_key):
			return b15
		elif (search_key < b15.b3):
			return self.fonk18(b15.b4, search_key)
		else:
			return self.fonk18(b15.b5, search_key)
	def fonk19(self, search_key):
		b16 = self.fonk18(self.b14, search_key)
		return b16.b2 if (b16 != None) else None;
	def fonk20(self, b15):
		if (b15.b5 = = None):
			return b15;
		else:
			return self.fonk20(b15.b5)
	def fonk21(self, key_delete):
		b17 = self.fonk18(self.b14, key_delete)
		if (b17 = = None):
			raise Exception("Can't delete b16 with b3 " + str(key_delete) + " because it was not found in the tree.")
		b18 = b17.b2
		if (b17 = = None):
			raise Exception("Value " + str(key_delete) + " not found in the tree.")
		if (b17.fonk4()):
			b17.b1.fonk2(b17)
		elif (b17.b4 = = None):
			b17.b1.fonk8(b17, b17.b5)
		else:
			b19 = self.fonk20(b17.b4)
			if (b19.b4 != None ):
				b19.b1.fonk8(b19, b19.b4)
			else:
				b19.b1.fonk2(b19)
			b17.b3 = b19.b3
			b17.b2 = b19.b2
		return b18