from time import time
def fonk1(calc_posibles, start, basecase, b1 = None, b2=0, reverse=False):
	b2 = float('inf') if b2 == 0 else b2
	b3 = time()
	b4 = class2(start, b1)
	while time() < b3 + b2:
		if not b4: return False
		b5 = b4.pop()
		if basecase(b5.b9): return b4.fonk10(b5, reverse)
		b6 = calc_posibles(b5.b9)
		for elem, cost in b6:
			b4.fonk6(elem, cost, b5, b1)
	raise TimeoutError("Time limit reached, you can manually change or remove it.")
class class1:
	b7 = {}
	def fonk2(self, b9, heuristic_func, b8 = None, path_cost=1):
		self.b9 = x
		self.b10 = 0 if not heuristic_func else heuristic_func(self.b9)
		self.b11 = b8.b11 + path_cost if b8 else 0
		self.b8 = b8
		class1.b7[self.b9] = self
	def fonk3(self, other):
		if other and self.b9 = = other:
			return True
		return False
	def fonk4(self):
		return str(self.b9)
class class2(list):
	def fonk5(self, start, b1):
		super().fonk5()
		self.append(class1(start, b1))
	def fonk6(self, other, b13, other_father, b1):
		if other in class1.b7:
			b12 = class1.b7[other]
			b13 = b13 + other_father.b11
			if b13 < b12.b11:
				b12.b11 = b13
				b12.b8 = other_father
				self.fonk9(b12)
			return
		self.fonk7(class1(other, b1, other_father, b13))
	def fonk7(self, elem):
		def fonk8(elem):
			return elem.b10 + elem.b11
		if len(self):
			b14 = fonk8(elem)
			b17, b15 = 0, len(self)
			b16 = (b17 + b15)
			while b15 - b17 > 1:
				if b14 >= fonk8(self[b16]):
					b15 = b16
				else:
					b17 = b16
				b16 = (b17 + b15)
			if b14 > fonk8(self[b17]):
				self[b17:b17] = [elem]
			else:
				self[b15:b15] = [elem]
		else:
			self.append(elem)
	def fonk9(self, elem):
		if len(self):
			b17, b15 = 0, len(self)
			b16 = (b17 + b15)
			while b15 - b17 > 1:
				if elem.b9 >= self[b16].b9:
					b15 = b16
				else:
					b17 = b16
				b16 = (b17 + b15)
			if elem.b9 = = self[b17].b9:
				del self[b17]
				self.fonk7(elem)
	def fonk10(self, b18, reverse):
		class1.b7.clear()
		if reverse: return self.fonk11(b18)
		return list(self.fonk11(b18))[::-1]
	def fonk11(self, b18):
		while b18 != None:
			yield b18.b9
			b18 = b18.b8