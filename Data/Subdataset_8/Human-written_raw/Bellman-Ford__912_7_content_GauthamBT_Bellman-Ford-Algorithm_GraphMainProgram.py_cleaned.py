from  DirectedGraphClass import *
numberOfVertices = 5
source = 0
directedGraphVar = DirectedGraph(numberOfVertices)
createDirectedGraph(directedGraphVar, source)
BellmanFordFunction(directedGraphVar)
directedGraphVar.printShortestPath()