25. Repository: aravindkanna/Implementation-of-Apriori-Algorithm
   File: Trie.py
   URL: https:
   Code Content:
from Queue import *
class class1:
	def fonk1(self, b1 = 1, b3 = "root"):
		self.b2 = {}
		self.b1 = b1
		self.b3 = b3
	def fonk2(self, itemset, b1):
		b4 = self.b2
		for i in itemset:
			if i in b4:
				b4 = b4[i].b2
			else:
				b5 = class1(b1, i)
				b4[i] = b5
	def fonk3(self, itemset):
		b4 = self.b2
		for i in itemset:
			if i in b4:
				b4 = b4[i].b2
			else:
				return False
		return True
	def fonk4(self, FreqItemSets, counts):
		b6 = len(FreqItemSets)
		for i in range(b6):
			self.fonk2(FreqItemSets[i], counts[i])
	def fonk5(self, prevStr):
		for i in self.b2:
			b7 = prevStr + i
			print b7
			self.b2[i].fonk5(b7 + ",")
	def fonk6(self, prevList):
		for i in self.b2:
			b7 = prevList+[i]
			yield b7
			for j in self.b2[i].fonk6(b7):
				yield j
	def fonk7(self, itemSet):
		b4 = self.b2
		for i in itemSet:
			b8 = b4[i]
			b4 = b4[i].b2
		return b8.b1
   README Content:
This is the Implementation of Apriori Algorithm which is b7 famous Frequent Set Mining Algorithm.
