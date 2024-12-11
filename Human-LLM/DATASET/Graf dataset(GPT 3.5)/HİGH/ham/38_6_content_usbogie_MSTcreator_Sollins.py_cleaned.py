import copy
from Node import Node
def fonk1(trees):
	b1 = list()
	for tree in trees:
		b1.append(fonk2(tree))
	return b1
def fonk2(tree):
	b2 = list()
	b3 = dict()
	b4 = dict()
	for n in tree:
		b5 = list()
		b6 = copy.copy(n)
		b6.b7 = {}
		b3[n] = b6
		b4[b6] = n
		b5.append(b6)
		b2.append(b5)
	while len(b2) != 1:
		b2 = fonk3(b2, tree, b3, b4)
	return b2.pop(0)
def fonk3(b2, tree, b3, b4):
	for subtree in b2:
		b8 = Node(0, 0, 0, {})
		a1 = -1
		b9 = Node(0, 0, 0, {})
		for n in subtree:
			b10 = b4[n]
			for p in b10.b7:
				b11 = b3[p]
				if b11 not in subtree and (b10.b7[p] < a1 or a1 = = -1):
					a1 = b10.b7[p]
					b8 = b11
					b9 = n
		fonk4(b2, subtree, b9, b8, a1)
	return b2
def fonk4(b2, subtree, b9, b8, a1):
	b12 = list()
	for sub in b2:
		if b8 in sub:
			b12 = sub
	b9.b7[b8] = a1
	b8.b7[b9] = a1
	for y in subtree:
		b12.append(y)
	b2.remove(subtree)
	return b2