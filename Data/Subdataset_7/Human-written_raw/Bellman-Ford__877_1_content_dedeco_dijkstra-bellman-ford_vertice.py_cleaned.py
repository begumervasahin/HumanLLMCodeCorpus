ï»¿class class1:
	def fonk1(self, id):
		self.b1 = id
		self.b2 = {}
		self.a1 = 0
		self.b3 = False
		self.b4 = None
	def fonk2(self):
		return self.b1
	def fonk3(self, b5 = None, peso=0):
		self.b2[b5] = peso
	def fonk4(self):
		return self.b2.keys()
	def fonk5(self):
		return self.a1
	def fonk6(self, distancia):
		self.a1 = distancia
	def fonk7(self):
		self.b3 = True
	def fonk8(self):
		return self.b3
	def fonk9(self,b5):
		return self.b2[b5]
	def fonk10(self,anterior):
		self.b4 = anterior
	def fonk11(self):
		return self.b4
	def fonk12(self):
		return str(self.b1)