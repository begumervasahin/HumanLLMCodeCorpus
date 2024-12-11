from vertice import vertice
class class1:
	def fonk1(self, b1 = False):
		self.b2 = {}
		self.b1 = b1
	def fonk2(self, id):
		b3 = vertice(id)
		self.b2[id] = b3
		return b3
	def fonk3(self, de, para, b4 = 0):
		if de not in self.b2:
			self.fonk2(de)
		if para not in self.b2:
			self.fonk2(para)
		self.b2[de].inserir_vertice_adjacente(self.b2[para],b4)
		if not self.b1:
			self.b2[para].inserir_vertice_adjacente(self.b2[de],b4)
	def fonk4(self):
		return ([b3 for k,b3 in self.b2.iteritems()])
	def fonk5(self, id):
		if id in self.b2:
			return self.b2[id]
		else:
			return None
	def fonk6(self):
		b5 = set()
		for id, b3 in self.b2.iteritems():
			for a in b3._vertices_adjacentes:
				b5.add((b3,a))
		return b5
	def fonk7(self):
		return iter(self.b2.values())