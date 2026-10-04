import GenGraph
import Sollins
import Prims
import Kruskals
import time
import copy
from Node import Node
def fonk1():
	print "Hello! This is a program which randomly generates nodes and edges to connect those nodes.",
	print "After the graph is generated, you can then choose from finding an MST of each tree created",
	print "by using either Prim's, Kruskal's, or Sollin's algorithm. Addtionally, there are two methods",
	print "of generating edges. The first method is to randomly assign a weight between 1 and the user-defined",
	print "maximum edge weight, the second is to assign the weight based on the actual distance between",
	print "the two nodes. Finally, the amount of nodes in the graph, the size of the graph, and the k-value,",
	print "which determines the likelihood any two nodes will have an edge between them."
	print "Which method of edge generation would you like to use?"
	print "1: Weight based on actual distance between nodes"
	print "2: Weight based on user-defined maximum edge weight"
	b1 = int(raw_input('> '))
	print "How many nodes are in the graph (any number greater than 0)?"
	b2 = int(raw_input('> '))
	print "How big is the graph (any number greater than 0)?"
	b3 = int(raw_input('> '))
	print "What is the k-value that should be used (any number greater than 0)?"
	b4 = int(raw_input('> '))
	a1 = 0
	if b1 = = 2:
		print "What is the maximum weight of an edge (any number greater than 0)?"
		a1 = int(raw_input('> '))
	b5 = GenGraph.GenerateGraph(b2, b3, a1, b4, b1)
	print "Here are the adjacency lists of the b5 randomly generated using your inputs (b6 = ((x,y,) weight)):"
	fonk2(b5, "Tree")
	print "Here are the b9 for each of the generated b5."
	b7 = copy.deepcopy(b5)
	b8 = time.clock()
	b9 = Prims.runPrims(b7)
	b10 = (time.clock()-b8)
	print "Result of Prim's"
	fonk2(b9,"MST")
	b11 = copy.deepcopy(b5)
	b8 = time.clock()
	b9 = Kruskals.runKruskals(b11)
	b12 = (time.clock()-b8)
	print "Result of Kruskal's"
	fonk2(b9,"MST")
	b13 = copy.deepcopy(b5)
	b8 = time.clock()
	b9 = Sollins.runSollins(b13)
	b14 = (time.clock()-b8)
	print "Result of Sollin's"
	fonk2(b9,"MST")
	print "Prim's Algorithm Run b15 = "+str(b10)
	print "Kruskal's Algorithm Run b15 = "+str(b12)
	print "Sollin's Algorithm Run b15 = "+str(b14)
def fonk2(b5, term):
	print term+"s:"
	for t in b5:
		print term+":{"
		for x in t:
			print fonk3(x)+": {",
			for y in x.adjList:
				print "("+fonk3(y)+", "+str(round(x.adjList[y],2))+")",
			print "}"
		print "}"
def fonk3(n):
	return "("+str(n.xloc)+","+str(n.yloc)+")"
fonk1()