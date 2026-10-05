import sys
from Node import Node
class class1(object):
	def fonk1(self,n):
		self.b1 = n[:]
	def fonk2(self):
		return len(self.b1)
	def fonk3(self,x):
		if x in self.b1:
			return True
		return False
	def fonk4(self):
		b2 = sys.maxint
		b3 = None
		for l in self.b1:
			if l.key < b2:
				b2 = l.key
				b3 = l
		self.b1.remove(b3)
		return b3.idx