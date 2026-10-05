import sys
from Node import Node
class MinQueue(object):
	def __init__(self,n):
		self.list = n[:]
	def __len__(self):
		return len(self.list)
	def contains(self,x):
		if x in self.list:
			return True
		return False
	def extractMin(self):
		min = sys.maxint
		node = None
		for l in self.list:
			if l.key < min:
				min = l.key
				node = l
		self.list.remove(node)
		return node.idx