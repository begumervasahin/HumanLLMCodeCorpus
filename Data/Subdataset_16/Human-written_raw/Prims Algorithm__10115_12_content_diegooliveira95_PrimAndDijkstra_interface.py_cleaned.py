from graph import Vertex as Vertex
from graph import Graph as Graph
from dijkstra import dijkstra as Dijkstra
from prim import prim as Prim
import random
import time
def fonk1(numberVertices, probability, lowerWeight, higherWeight):
	b1 = Graph()
	for x in range(1, numberVertices):
		b1.addVertex(str(x))
	for aVertex in b1:
		for bVertex in b1:
			if bVertex.getId() == aVertex.getId() or bVertex.getId() in aVertex.getConnections():
				continue
			if(probability > random.randrange(0, 100)):
				b1.addEdge(aVertex.getId(), bVertex.getId(), random.randint(lowerWeight, higherWeight))
	return b1
if b2 = = '__main__':
	b3 = fonk1(200, 90, 1, 5)
	b4 = fonk1(300, 90, 1, 5)
	b5 = fonk1(400, 90, 1, 5)
	b6 = fonk1(200, 20, 1, 5)
	b7 = fonk1(300, 20, 1, 5)
	b8 = fonk1(400, 20, 1, 5)
	b9 = time.time()
	Dijkstra(b3, b3.getVertex('1'))
	b10 = time.time() - b9
	b11 = time.time()
	Prim(b3, b3.getVertex('1'))
	b12 = time.time() - b11
	print("----------------- Primeira Amostra -----------------\nDijkstra: %s segundos\nPrim: %s segundos\n----------------------------------------------------\n" % (b10, b12))
	b9 = time.time()
	Dijkstra(b4, b4.getVertex('1'))
	b10 = time.time() - b9
	b11 = time.time()
	Prim(b4, b4.getVertex('1'))
	b12 = time.time() - b11
	print("----------------- Segunda Amostra -----------------\nDijkstra: %s segundos\nPrim: %s segundos\n----------------------------------------------------\n" % (b10, b12))
	b9 = time.time()
	Dijkstra(b5, b5.getVertex('1'))
	b10 = time.time() - b9
	b11 = time.time()
	Prim(b5, b5.getVertex('1'))
	b12 = time.time() - b11
	print("----------------- Terceira Amostra -----------------\nDijkstra: %s segundos\nPrim: %s segundos\n----------------------------------------------------\n" % (b10, b12))
	b9 = time.time()
	Dijkstra(b6, b6.getVertex('1'))
	b10 = time.time() - b9
	b11 = time.time()
	Prim(b6, b6.getVertex('1'))
	b12 = time.time() - b11
	print("----------------- Quarta Amostra -----------------\nDijkstra: %s segundos\nPrim: %s segundos\n----------------------------------------------------\n" % (b10, b12))
	b9 = time.time()
	Dijkstra(b7, b7.getVertex('1'))
	b10 = time.time() - b9
	b11 = time.time()
	Prim(b7, b7.getVertex('1'))
	b12 = time.time() - b11
	print("----------------- Quinta Amostra -----------------\nDijkstra: %s segundos\nPrim: %s segundos\n----------------------------------------------------\n" % (b10, b12))
	b9 = time.time()
	Dijkstra(b8, b8.getVertex('1'))
	b10 = time.time() - b9
	b11 = time.time()
	Prim(b8, b8.getVertex('1'))
	b12 = time.time() - b11
	print("----------------- Sexta Amostra -----------------\nDijkstra: %s segundos\nPrim: %s segundos\n----------------------------------------------------\n" % (b10, b12))