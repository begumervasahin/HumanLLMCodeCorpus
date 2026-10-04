from igraph import *
import numpy as np
class class1:
	def fonk1(self):
		self.b1 = ''
		self.b2 = ''
		self.b3 = ''
	def fonk2(self):
		print(self.b1,self.b3,self.b2)
def fonk3(graph,vertex):
	b4 = []
	for edge in graph.incident(vertex):
		b5 = class1()
		b5.b1 = graph.es[edge].tuple[0]
		b5.b3 = graph.es[edge]['peso']
		b5.b2 = graph.es[edge].tuple[1]
		b4.append(b5)
	return b4
b6 = Graph(directed=True)
b6.add_vertices(5)
b6.vs['nome'] = ['b5','b','c','d','e']
b6.add_edges([(0,1), (0,4), (1,2), (1,3), (1,4), (2,4)])
b6.es['peso'] = [3,11,3,2,7,2]
b7 = 5 * [999]
b7[0] = 0
for vertex in b6.vs:
	for actualArrow in fonk3(b6,vertex):
		if(b7[actualArrow.b1] + actualArrow.b3 < b7[actualArrow.b2]):
			b7[actualArrow.b2] = b7[actualArrow.b1] + actualArrow.b3
print(b7)