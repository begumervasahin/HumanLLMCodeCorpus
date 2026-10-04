25. Repository: aravindkanna/Implementation-of-Apriori-Algorithm
   File: Trie.py
   URL: https:
   Code Content:
from Queue import *
class trieNode:
	def __init__(self, count = 1, name = "root"):
		self.child = {}
		self.count = count
		self.name = name
	def insertNode(self, itemset, count):
		f = self.child
		for i in itemset:
			if i in f:
				f = f[i].child
			else:
				temp = trieNode(count, i)
				f[i] = temp
	def hasNode(self, itemset):
		f = self.child
		for i in itemset:
			if i in f:
				f = f[i].child
			else:
				return False
		return True
	def insertAll(self, FreqItemSets, counts):
		size = len(FreqItemSets)
		for i in range(size):
			self.insertNode(FreqItemSets[i], counts[i])
	def printAll(self, prevStr):
		for i in self.child:
			a = prevStr + i
			print a
			self.child[i].printAll(a + ",")
	def getItemSets(self, prevList):
		for i in self.child:
			a = prevList+[i]
			yield a
			for j in self.child[i].getItemSets(a):
				yield j
	def getCount(self, itemSet):
		f = self.child
		for i in itemSet:
			fp = f[i]
			f = f[i].child
		return fp.count
   README Content:
This is the Implementation of Apriori Algorithm which is a famous Frequent Set Mining Algorithm.
