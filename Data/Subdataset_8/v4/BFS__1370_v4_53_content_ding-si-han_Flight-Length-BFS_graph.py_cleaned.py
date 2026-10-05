import random
from itertools import chain
import time
import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt
class Graph:
    graph_dict = {}
    def __init__(self):
        self.graph_dict = {}
    def addEdge(self, node, neighbour):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbour]
        else:
            if neighbour not in self.graph_dict[node] and neighbour != node:
                self.graph_dict[node].append(neighbour)
    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(", node, ", ", neighbour, ")")
    def BFS(self, start, destination):
        originalStart = start
        visited = {}
        parentDictionary = {}
        for i in self.graph_dict:
            visited[i] = False
        queue = []
        queue.append(start)
        visited[start] = True
        while len(queue) != 0:
            start = queue.pop(0)
            for node in self.graph_dict[start]:
                if visited[node] != True:
                    parentDictionary[node] = start
                    if node == destination:
                        self.printParent(parentDictionary, originalStart, destination)
                        return
                    visited[node] = True
                    queue.append(node)
        print("NO FLIGHT PATH AVAILABLE")
    def printParent(self, parentDictionary, start, destination):
        print("OPTIMAL ROUTE:", end=" ")
        current = parentDictionary[destination]
        print(destination, end=" ")
        while start != current:
            print("-", current, end=" ")
            current = parentDictionary[current]
        print('-', start)
    def generateGraph(self, max, percentageCities):
        for i in range(max):
            randomRange = chain(range(0, i), range(i + 1, max))
            randomNeighbourArray = random.sample(list(randomRange), round(max * percentageCities))
            for neighbour in randomNeighbourArray:
                self.addEdge(str(i + 1), str(neighbour + 1))
                self.addEdge(str(neighbour + 1), str(i + 1))
"""
Measuring the time taken for BFS Algorithm for:
1. Different number of cities in graphs (Vertices)
2. Different number of non-stop flights (Edges)
Plotting the shortest path for an airline to enable a passenger to fly from city A (Singapore) to city B (Florida).
1. Finding how the number of cities in the network affect the time taken for BFS Algorithm: