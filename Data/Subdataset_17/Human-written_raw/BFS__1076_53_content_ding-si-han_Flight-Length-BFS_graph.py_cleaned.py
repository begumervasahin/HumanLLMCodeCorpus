53. Repository: ding-si-han/Flight-Length-BFS
   File: graph.py
   URL: https:
   Code Content:
import random
from itertools import chain
import time
import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt
class Graph:
    graph_dict = {}
    def __init__(self):
        graph_dict={}
    def __call__(self):
        self.graph_dict = {}
    def addEdge(self,node,neighbour):
        if node not in self.graph_dict:
            self.graph_dict[node]=[neighbour]
        else:
            if neighbour not in self.graph_dict[node] and neighbour != node:
                self.graph_dict[node].append(neighbour)
    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(",node,", ",neighbour,")")
    def BFS(self,start, destination):
        originalStart = start
        visited={}
        parentDictionary = {}
        for i in self.graph_dict:
            visited[i]=False
        queue=[]
        queue.append(start)
        visited[start]=True
        while len(queue)!=0:
            start=queue.pop(0)
            for node in self.graph_dict[start]:
                if visited[node]!=True:
                    parentDictionary[node] = start
                    if node == destination:
                        self.printParent(parentDictionary, originalStart, destination)
                        return
                    visited[node]=True
                    queue.append(node)
        print("NO FLIGHT PATH AVAILABLE")
    def printParent(self, parentDictionary, start, destination):
        print("OPTIMAL ROUTE:", end = " ")
        current = parentDictionary[destination]
        print(destination, end = " ")
        while start != current:
            print("-", current, end = " ")
            current = parentDictionary[current]
        print('-', start)
        return
    def generateGraph(self, max, percentageCities):
        for i in range(max):
            randomRange = chain(range(0,i), range(i+1,max))
            randomNeighbourArray = random.sample(list(randomRange), round(max*percentageCities))
            for neighbour in randomNeighbourArray:
                self.addEdge(str(i+1), str(neighbour + 1))
                self.addEdge(str(neighbour+1), str(i + 1))
   README Content:
Measuring the time taken for BFS Algorithm for:
1. Different number of cities in graphs (Vertices)
2. Different number of non-stop flights (Edges)
Plotting the shortest path for an airline to enable a passenger to fly from city A (Singapore) to city B (Florida).
1. Finding how the number of cities in the network affect the time taken for BFS Algorithm:
<pre><code> $ python numCities.py</code></pre>
2. Finding how the number of non-stop flights affect the time taken for BFS Algorithm
<pre><code> $ python numDirectFlights.py</code></pre>
_graph.py_ contains Graph Class which has the stores the flights between cities in the dictionary _graph_dict_ and has the following methods:
 1. addEdge(self,node,neighbour)
 2. showEdges(self)
 3. BFS(self,start, destination)
 4. printParent(self, parentDictionary, start, destination)
 5. generateGraph(self, max, percentageCities)
 The Graph Class is instantiated as individual objects in _numCities.py_ and _numDirectFlights.py_
