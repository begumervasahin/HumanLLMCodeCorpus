class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = [[] for _ in range(num_vertices)]
    def addEdge(self, v1, v2, c=1):
        self.adjacency_list[v1].append((v2, c))
    def getNrVertices(self):
        return self.num_vertices
    def getNrEdges(self):
        total_edges = sum(len(edges) for edges in self.adjacency_list)
        return total_edges
    def isEdge(self, v1, v2):
        return any(v2 in neighbors for neighbors in self.adjacency_list[v1])
    def getDegree(self, v):
        return len(self.adjacency_list[v])
    def parseNeighbours(self, v):
        return [neighbor[0] for neighbor in self.adjacency_list[v]]
    def parseAll(self):
        all_edges = []
        for v in range(self.num_vertices):
            for neighbor, _ in self.adjacency_list[v]:
                all_edges.append((v, neighbor))
        return all_edges
class Repository:
    def __init__(self, filename="graph1.txt"):
        self._loadFromFile(filename)
    def _loadFromFile(self, filename):
        try:
            with open(filename, 'r') as file:
                text = file.readline()
                num_vertices = int(text.strip())
                self.graph = Graph(num_vertices)
                for line in file:
                    v1, v2 = map(int, line.split())
                    self.graph.addEdge(v1, v2)
                    self.graph.addEdge(v2, v1)
        except FileNotFoundError:
            print("File not found.")
    def getNrVertices(self):
        return self.graph.getNrVertices()
    def getNrEdges(self):
        return self.graph.getNrEdges()
    def isEdge(self, v1, v2):
        return self.graph.isEdge(v1, v2)
    def getDegree(self, v):
        return self.graph.getDegree(v)
    def getNeighbours(self, v):
        return self.graph.parseNeighbours(v)
    def showAll(self):
        return self.graph.parseAll()
    def addEdge(self, v1, v2, c=1):
        return self.graph.addEdge(v1, v2, c)
repo = Repository("graph1.txt")
print("Number of vertices:", repo.getNrVertices())
print("Number of edges:", repo.getNrEdges())
print("Is there an edge between vertices 1 and 2?", repo.isEdge(1, 2))
print("Degree of vertex 1:", repo.getDegree(1))
print("Neighbours of vertex 1:", repo.getNeighbours(1))
print("All edges in the graph:", repo.showAll())