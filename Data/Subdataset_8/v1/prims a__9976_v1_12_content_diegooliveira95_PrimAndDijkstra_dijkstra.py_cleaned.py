import heapq
class Vertex:
    def __init__(self, key):
        self.id = key
        self.adjacent = {}
        self.distance = float('inf')
        self.previous = None
        self.visited = False
    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
    def getId(self):
        return self.id
    def getWeight(self, neighbor):
        return self.adjacent[neighbor]
    def getDistance(self):
        return self.distance
    def setDistance(self, dist):
        self.distance = dist
    def getPrevious(self):
        return self.previous
    def setPrevious(self, prev):
        self.previous = prev
    def setVisited(self):
        self.visited = True
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None
    def __contains__(self, key):
        return key in self.vertList
    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
def shortest(v, path):
    if v.previous:
        path.append(v.previous.getId())
        shortest(v.previous, path)
    return
def dijkstra(aGraph, start):
    start.setDistance(0)
    unvisitedQueue = [(vertex.getDistance(), vertex) for vertex in aGraph.vertList.values()]
    heapq.heapify(unvisitedQueue)
    while len(unvisitedQueue):
        aVertex = heapq.heappop(unvisitedQueue)
        current = aVertex[1]
        current.setVisited()
        for nextVertex, weight in current.adjacent.items():
            if not nextVertex.visited:
                newDistance = current.getDistance() + weight
                if newDistance < nextVertex.getDistance():
                    nextVertex.setDistance(newDistance)
                    nextVertex.setPrevious(current)
        unvisitedQueue = [(vertex.getDistance(), vertex) for vertex in aGraph.vertList.values() if not vertex.visited]
        heapq.heapify(unvisitedQueue)
if __name__ == "__main__":
    g = Graph()
    g.addEdge('A', 'B', 4)
    g.addEdge('A', 'C', 2)
    g.addEdge('B', 'C', 5)
    g.addEdge('B', 'D', 10)
    g.addEdge('C', 'D', 3)
    g.addEdge('D', 'E', 7)
    g.addEdge('E', 'F', 2)
    g.addEdge('F', 'A', 6)
    startVertex = g.getVertex('A')
    dijkstra(g, startVertex)
    for v in g.vertList.values():
        path = []
        shortest(v, path)
        print("Shortest path to vertex", v.getId(), ":", path[::-1] + [v.getId()], "with distance", v.getDistance())