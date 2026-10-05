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
        return self.vertList.get(key)
    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
def shortest_path_to_vertex(vertex, path):
    if vertex.previous:
        path.append(vertex.previous.getId())
        shortest_path_to_vertex(vertex.previous, path)
    return
def dijkstra(graph, start):
    start.setDistance(0)
    unvisitedQueue = [(vertex.getDistance(), vertex) for vertex in graph.vertList.values()]
    heapq.heapify(unvisitedQueue)
    while unvisitedQueue:
        current_distance, current_vertex = heapq.heappop(unvisitedQueue)
        current_vertex.setVisited()
        for next_vertex, weight in current_vertex.adjacent.items():
            if not next_vertex.visited:
                new_distance = current_distance + weight
                if new_distance < next_vertex.getDistance():
                    next_vertex.setDistance(new_distance)
                    next_vertex.setPrevious(current_vertex)
        unvisitedQueue = [(vertex.getDistance(), vertex) for vertex in graph.vertList.values() if not vertex.visited]
        heapq.heapify(unvisitedQueue)
if __name__ == "__main__":
    graph = Graph()
    graph.addEdge('A', 'B', 4)
    graph.addEdge('A', 'C', 2)
    graph.addEdge('B', 'C', 5)
    graph.addEdge('B', 'D', 10)
    graph.addEdge('C', 'D', 3)
    graph.addEdge('D', 'E', 7)
    graph.addEdge('E', 'F', 2)
    graph.addEdge('F', 'A', 6)
    start_vertex = graph.getVertex('A')
    dijkstra(graph, start_vertex)
    for vertex in graph.vertList.values():
        path = []
        shortest_path_to_vertex(vertex, path)
        print("Shortest path to vertex", vertex.getId(), ":", path[::-1] + [vertex.getId()], "with distance", vertex.getDistance())