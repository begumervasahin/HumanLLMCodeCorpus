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
		b5 = copy.copy(n)
		b5.b6 = {}
		b3[n] = b5
		b4[b5] = n
	b7 = b3[tree.keys()[0]]
	b2.append(b7)
	b8 = False
	while (not b8):
		if len(b2) == len(tree):
			b8 = True
		else:
			b2.append(fonk3(b2, tree, b3, b4))
	return b2
def fonk3(b2, tree, b3, b4):
	b9 = Node(0, 0, 0, {})
	a1 = -1
	b10 = Node(0, 0, 0, {})
	b11 = Node(0, 0, 0, {})
	for n in b2:
		b12 = b4[n]
		for p in b12.b6:
			if (b12.b6[p] < a1 or a1 = = -1) and not b3[p] in b2:
				a1 = b12.b6[p]
				b9 = b3[p]
				b11 = p
				b10 = n
	b13 = b4[b10]
	del b13.b6[b11]
	del b11.b6[b13]
	b10.b6[b9] = a1
	b9.b6[b10] = a1
	return b9