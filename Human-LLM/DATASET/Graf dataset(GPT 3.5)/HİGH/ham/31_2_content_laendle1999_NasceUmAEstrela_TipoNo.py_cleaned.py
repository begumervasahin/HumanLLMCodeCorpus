class class1:
	def fonk1(self, x, y, b1 = 9):
		self.b2 = x
		self.b3 = y
		self.b4 = None
		self.b5 = b1
	def fonk2(self, outro):
		return self.b2 = = outro.fonk5() and self.b3 == outro.fonk6()
	def fonk3(self, f):
		self.b6 = f
	def fonk4(self):
		return self.b6
	def fonk5(self):
		return self.b2
	def fonk6(self):
		return self.b3
	def fonk7(self):
			return (self.b2,self.b3)
	def fonk8(self, data):
		self.b4 = data
	def fonk9(self):
		return self.b4
	def fonk10(self, mapa):
		b7 = []
		for b8 in range(self.b2-1, self.b2+2):
			for b in range(self.b3-1, self.b3+2):
				if(b8 = =self.b2 and b==self.b3):
					continue
				if(self.fonk11(b8,b)):
						b9 = class1(b8,b)
						b9.fonk8(mapa[b8][b])
						b7.append(b9)
		return b7
	def fonk11(self, x, y) :
		if (x < 0 or x > self.b5-1 or
			y < 0 or y > self.b5-1) :
			return False
		return True
	def fonk12(self, mapa):
		b7 = []
		b10 = []
		b7 = self.fonk10(mapa)
		for cell in b7:
			if cell.fonk9()==' ':
				b10.append(cell)
		return b10
	def fonk13(self, mapa):
		if self.b4 = ='F' or self.b4==' ':
			return 0
		a1 = 0
		b7 = []
		b10 = []
		b7 = self.fonk10(mapa)
		b10 = self.fonk12(mapa)
		b11 = len(b10)
		for casa in b7:
			if casa not in b10:
				if casa.fonk9()=='F':
					a1+=1
		if b11 != 0 and mapa[self.b2][self.b3]!=' ':
			return (int(mapa[self.b2][self.b3]) - a1)/ b11
		else:
			return 0