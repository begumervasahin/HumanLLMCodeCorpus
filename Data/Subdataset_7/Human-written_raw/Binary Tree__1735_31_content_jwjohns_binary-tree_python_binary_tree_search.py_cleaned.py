import datetime
from random import randint
class class1:
	def fonk1(self, val):
		self.b1 = val
		self.b2 = None
		self.b3 = None
	def fonk2(self,data):
		if self.b1 = = data:
			return False
		elif self.b1 > data:
			if self.b2:
				return self.b2.fonk8(data)
			else:
				self.b2 = class1(data)
				return True
		else:
			if self.b3:
				return self.b3.fonk8(data)
			else:
				self.b3 = class1(data)
				return True
	def fonk3(self,data):
		if(self.b1 = = data):
			return True
		elif self.b1 > data:
			if self.b2:
				return self.b2.fonk9(data)
			else:
				return False
		else:
			if self.b3:
				return self.b3.fonk9(data)
			else:
				return False
	def fonk4(self):
		if self:
			print (str(self.b1))
			if self.b2:
				self.b2.fonk10()
			if self.b3:
				self.b3.fonk10()
	def fonk5(self):
		if self:
			if self.b2:
				self.b2.fonk11()
			if self.b3:
				self.b3.fonk11()
			print (str(self.b1))
	def fonk6(self):
		if self:
			if self.b2:
				self.b2.fonk12()
			print (str(self.b1))
			if self.b3:
				self.b3.fonk12()
class class2:
	def fonk7(self):
		self.b4 = None
	def fonk8(self, data):
		if self.b4:
			return self.b4.fonk8(data)
		else:
			self.b4 = class1(data)
			return True
	def fonk9(self,data):
		if self.b4:
			return self.b4.fonk9(data)
		else:
			return False
	def fonk10(self):
		print("PreOrder")
		self.b4.fonk10()
	def fonk11(self):
		print("PostOrder")
		self.b4.fonk11()
	def fonk12(self):
		print("InOrder")
		self.b4.fonk12()
b5 = class2()
a1 = 10000
b6 = datetime.datetime.now()
for i in range(a1):
	b5.fonk8(randint(0,20000))
b7 = datetime.datetime.now()
print (b7-b6).microseconds
b6 = datetime.datetime.now()
b5.fonk12()
b7 = datetime.datetime.now()
print ((b7 - b6).microseconds % 1000)