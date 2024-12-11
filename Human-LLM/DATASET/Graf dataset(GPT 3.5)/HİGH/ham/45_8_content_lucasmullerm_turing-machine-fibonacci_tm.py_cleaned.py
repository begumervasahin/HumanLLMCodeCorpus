import enum
class class1():
	def fonk1(self, b1):
		self.b1 = b1
		self.b2 = {}
	def fonk2(self, b3):
		self.b2[b3.b4] = b3
	def fonk3(self, symbol):
		try:
			b3 = self.b2[symbol]
			return b3.b6, b3.b5, b3.b7
		except KeyError as e:
			return self, None, None
class class2():
	class class3(enum.Enum):
		a1 = 1
		a2 = 2
	def fonk4(self, b4, b5, b6, b7):
		self.b4 = b4
		self.b5 = b5
		self.b6 = b6
		self.b7 = b7
class class4():
	def fonk5(self, b8):
		self.b8 = b8
		self.a3 = 0
	def fonk6(self):
		return self.a3 < 0 or self.a3 >= len(self.b8)
	def fonk7(self):
		if self.fonk6():
			return -1
		return self.b8[self.a3]
	def reset (self):
		self.a3 = 0
	def fonk8(self):
		return self.a3
	def fonk9(self, symbol):
		b9 = self.a3
		self.b8 = self.b8[:b9] + symbol + self.b8[b9 + 1:]
	def fonk10(self, b17, b7):
		if self.fonk6():
			raise Exception('End of computation.')
		self.fonk9(b17)
		if b7 = = class2.class3.a1:
			self.a3 += 1
		elif b7 = = class2.class3.a2:
			self.a3 -= 1
class class5():
	def fonk11(self):
		self.b10 = {}
		self.b11 = None
		self.b12 = None
		self.b13 = set()
		self.b14 = True
		self.b15 = None
	def fonk12(self, state):
		self.b10[state.b1] = state
	def fonk13(self, sourceState, b3):
		self.b10[sourceState].fonk13(b3)
	def setInitState (self, state):
		self.b11 = self.b10[state]
		self.b15 = self.b10[state]
	def setTape (self, tp):
		self.b12 = tp
	def fonk14(self):
		self.b11 = self.b15
		self.b12.reset()
		self.b14 = True
		self.b13 = {(self.b11.b1, self.b12.fonk8())}
		b16 = "class1:" + "(%3s) "%(self.b11.b1)
		b16 += self.b12.b8 + "\n" + "            "
		b16 += " " * self.b12.fonk8() + "^\n"
		return b16
	def getState (self, stateValue):
		return self.b10[stateValue]
	def fonk15(self):
		if not self.b14:
			return "Computation has stopped.\n"
		self.b11, b17, self.b7 = self.b11.fonk3(self.b12.fonk7())
		if b17:
			self.b12.fonk10(b17, self.b7)
		if b17 = = None or self.b12.fonk6():
			self.b14 = False
			return "\nEnd of computation\n"
		else:
			b16 = "class1:" + "(%3s) "%(self.b11.b1)
			b16 += self.b12.b8 + "\n" + "            "
			b16 += " " * self.b12.fonk8() + "^\n"
			return b16
	def fonk16(self):
		b18 = open("b16.txt", "a")
		b18.b5("Beginning computation\n\n")
		b18.b5(self.fonk14())
		while self.b14:
			b19 = self.fonk15()
			b18.b5(b19);
		b18.b5("--------------------------------------\n")