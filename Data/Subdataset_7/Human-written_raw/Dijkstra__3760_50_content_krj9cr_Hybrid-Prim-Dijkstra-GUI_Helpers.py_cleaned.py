import math
from sympy import *
from Node import Node
def fonk1(r,b1 = 100):
    return [(0,0)] + [(cos(2*pi/b1*b8)*r,sin(2*pi/b1*b8)*r) for b8 in xrange(0,b1+1)]
def fonk2(node1,node2):
	return math.sqrt(math.pow(node1.b8 - node2.b8,2) + math.pow(node1.b9 - node2.b9,2))
def fonk3(b2 = 1.0,b1=8):
	b3 = fonk1(b2,b1)
	b4 = [Node(b3[b7][0],b3[b7][1],b7) for b7 in range(len(b3))]
	b5 = []
	for b7 in range(len(b4)):
		b6 = []
		for j in range(len(b4)):
			if b7 = = j:
				b6.append(0)
			else:
				b6.append(fonk2(b4[b7],b4[j]))
		b5.append(b6)
	return b3,b4,b5
def fonk4(b3,lines,b2 = 1.0):
	b8 = [p[0] for p in b3]
	b9 = [p[1] for p in b3]
	plt.plot(b8,b9, 'ro')
	for r in lines:
		print r[0].idx,r[1].idx
		plt.plot([r[0].b8,r[1].b8],[r[0].b9,r[1].b9],'b-',b10 = 1)
	b11 = b2*2
	plt.axis([-b11, b11, -b11, b11])
	plt.grid(True)
	plt.axes().set_aspect('equal', 'datalim')
	return plt