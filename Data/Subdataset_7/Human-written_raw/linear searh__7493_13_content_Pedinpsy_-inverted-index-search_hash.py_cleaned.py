import math
class class1:
	def fonk1(self,b2,b1):
		self.b1 = []
		self.b1.append(b1)
		self.b2 = b2
class b8:
	def fonk2(self,b5,b6, b3 = "division",b9 = 'linear'):
		self.b4 = [None] * b5
		self.b5 = b5
		self.b6 = b6
		self.a1 = 0
		self.b7 = []
		if b3 = = 'multiplication':
			self.b8 = self.getValueMultiplication
		else:
			self.b8 = self.getValueDivision
		if (b9 = = 'quadratic'):
			self.b10 = self.getQuadraticValue
		else:
			self.b10 = self.getLinearValue
	def fonk3(self):
		return self.b4
	def fonk4(self):
		return self.b7
	def fonk5(self,b2,b1):
		if(len(b2)< self.b6):
			return False
		a1 = 0
		b11 = self.b8(b2)
		if b2 not in self.b7:
			self.b7.append(b2)
		while(True):
			b12 = class1(b2,b1)
			if(self.b4[b11]!= None):
				if(self.b4[b11].b2 != b2):
					b11 = self.b10(b11,a1)
					a1 = a1 + 1
				else:
					self.b4[b11].b1.append(b1)
					break
			else:
				self.b4[b11] = b12
				self.a1 = a1+1
				break
		return True
	def fonk6(self,b2):
		if(len(b2)<self.b6):
			return None
		a1 = 0
		b11 = self.b8(b2)
		if(self.b4[b11] is None):
			return None
		while(True):
			if(self.b4[b11] is None):
				return None
			if(self.b4[b11].b2 = = b2):
				return self.b4[b11].b1
			else:
				b11 = self.b10(b11, a1)
				a1 = (a1+1)%self.b5
		return None
	def fonk7(self,b2):
		b11 = 0
		for x in range(0,self.b6):
			b11 = b11 + int(ord(b2[x]))
		b11 = int(b11%len(self.b4))
		return b11
	def fonk8(self, b2):
		b13 = (math.sqrt(5)-1)/2
		b11 = 0
		for x in range(0,self.b6):
			b11 = b11 + int(ord(b2[x]))
		b11 = math.floor(math.pow(2,2)*((b13*b11)%1))
		return int(b11)
	def fonk9(self,b2,a1):
		b14 = (b2 + a1*a1) % self.b5
		return b14
	def fonk10(self,b2,adictionator):
		return int((b2+adictionator)%self.b5)