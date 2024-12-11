class class1:
	def fonk1(self, b1):
		self.b1 = b1
		self.b2 = None
		self.b3 = None
class class2:
	def fonk2(self):
		self.b4 = None
	def fonk3(self, b1):
		b5 = class1(b1)
		if self.b4 = = None:
			self.b4 = b5
		else:
			b6 = self.b4
			while (True):
				if b1 < b6.b1:
					if b6.b2 = = None:
						b6.b2 = b5
						break
					b6 = b6.b2
				elif b1 > b6.b1:
					if b6.b3 = = None:
						b6.b3 = b5
						break
					b6 = b6.b3
				else:
					break
	def fonk4(self, b1):
		b6 = self.b4
		while(True):
			print(b6)
			if b6.b1 != b1:
				if b1 < b6.b1:
					b6 = b6.b2
				else:
					b6 = b6.b3
			else:
				print('b1 ', b1)
				if(b6.b2 = =None):
					print('None')
				else:
					print('b2 ', b6.b2.b1)
				if(b6.b3 = =None):
					print('None')
				else:
					print('b3 ', b6.b3.b1)
				break
			if b6 = = None:
				print('Value not found')
				break
	def fonk5(self, b1):
		b7 = None
		b6 = self.b4
		while(True):
			if b6 = =None:
				print("b1 not found")
				break
			elif b1 < b6.b1:
				b7 = b6
				b6 = b6.b2
			elif b1 > b6.b1:
				b7 = b6
				b6 = b6.b3
			elif b6.b1 = =b1:
				if(b6.b2 = =None and b6.b3==None):
					if(b7.b2 = =b6):
						b7.b2 = None
					elif(b7.b3 = =b6):
						b7.b3 = None
					del b6
					break
				elif (b6.b2!=None and b6.b3 = =None) or (b6.b2==None and b6.b3!=None):
					b7.b2 = b6.b2
					del b6
					break
				else:
					b8 = b6
					b9 = b6.b3
					while(b9.b2!=None):
						b8 = b9
						b9 = b9.b2
					b6.b1 = b9.b1
					b8.b2 = b9.b3
					del b9
					break
	def fonk6(self):
		b6 = self.b4
		b10 = []
		b11 = []
		b11.append(b6)
		while len(b11)>0:
			b6 = b11.pop(0)
			b10.append(b6.b1)
			if b6.b2 != None:
				b11.append(b6.b2)
			if b6.b3 != None:
				b11.append(b6.b3)
		return b10
	def fonk7(self, b11, b10):
		if len(b11)==0:
			return b10
		b6 = b11.pop(0)
		b10.append(b6.b1)
		if b6.b2 != None:
			b11.append(b6.b2)
		if b6.b3 != None:
			b11.append(b6.b3)
		return self.fonk7(b11, b10)
	def fonk8(self, b12):
		if b12 = =None:
			return 0
		else:
			return (1 + max(self.fonk8(b12.b2), self.fonk8(b12.b3)))
def fonk9(b4):
	if b4.b2 != None:
		fonk9(b4.b2)
	print(b4.b1)
	if b4.b3 != None:
		fonk9(b4.b3)
def fonk10(b4):
	print(b4.b1)
	if b4.b2 != None:
		fonk10(b4.b2)
	if b4.b3 != None:
		fonk10(b4.b3)
def fonk11(b4):
	if b4.b2 != None:
		fonk11(b4.b2)
	if b4.b3 != None:
		fonk11(b4.b3)
	print(b4.b1)
b13 = class2();
b13.fonk3(50)
b13.fonk3(28)
b13.fonk3(78)
b13.fonk3(12)
b13.fonk3(40)
b13.fonk3(66)
b13.fonk3(90)
b13.fonk3(9)
b13.fonk3(18)
b13.fonk3(37)
b13.fonk3(43)
b13.fonk3(57)
b13.fonk3(69)
b13.fonk3(81)
b13.fonk3(93)
b13.fonk3(3)
b13.fonk3(10)
b13.fonk3(15)
b13.fonk3(21)
b13.fonk3(30)
b13.fonk3(38)
b13.fonk3(42)
b13.fonk3(46)
b13.fonk3(54)
b13.fonk3(60)
b13.fonk3(67)
b13.fonk3(72)
b13.fonk3(80)
b13.fonk3(84)
b13.fonk3(92)
b13.fonk3(96)
b13.fonk3(13)
b13.fonk3(29)
b13.fonk3(55)
b13.fonk3(56)
b13.fonk5(15)
print(b13.fonk6())
print('height: ', b13.fonk8(b13.b4))
print(b13.fonk7([b13.b4], []))
print('inOrder')
fonk9(b13.b4)
print('preOrder')
fonk10(b13.b4)
print('postOrder')
fonk11(b13.b4)