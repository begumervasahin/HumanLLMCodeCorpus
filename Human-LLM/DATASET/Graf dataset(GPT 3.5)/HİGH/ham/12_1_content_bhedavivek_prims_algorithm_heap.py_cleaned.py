class class1:
	b1 = [0];
	def fonk1(self,key_value):
		self.b1.append(key_value)
		self.b1[0] = len(self.b1)-1
		self.fonk2(self.b1[0])
	def fonk2(self,b4):
		while(b4>1):
			b2 = b4/2
			if(int(self.b1[b2].distance)>int(self.b1[b4].distance)):
				b3 = self.b1[b4]
				self.b1[b4] = self.b1[b2]
				self.b1[b2]=b3
				b4 = b2
			else:
				break;
	def fonk3(self):
		b5 = self.b1[0]
		b6 = self.b1[1]
		self.b1[1] = self.b1[b5]
		self.b1[0] = self.b1[0]-1
		if self.b1[0]>1:
			self.fonk4(1)
		del self.b1[-1]
		return b6
	def fonk4(self,b4):
		while (2*b4<=self.b1[0]):
			if(2*b4 = =self.b1[0]) or (self.b1[2*b4].distance<self.b1[2*b4+1].distance):
				b2 = 2*b4
			else:
				b2 = 2*b4+1
			if self.b1[b2].distance<self.b1[b4].distance:
				b3 = self.b1[b4]
				self.b1[b4] = self.b1[b2]
				self.b1[b2]=b3
				b4 = b2
			else:
				break;