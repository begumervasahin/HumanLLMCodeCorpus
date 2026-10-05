
class Vertex:
    def __init__(self, id, parentId, distance, position=0):
        self.id = id
        self.parentId = parentId
        self.distance = distance
        self.position = position
class Graph:
    def __init__(self, n):
        self.adjacency_list = [[] for _ in range(n)]
    def insert(self, u, v, w):
        vert = Vertex(v, u, w)
        self.adjacency_list[u - 1].append(vert)
if __name__ == "__main__":
    g = Graph(5)
    g.insert(1, 2, 10)
    g.insert(1, 3, 15)
    g.insert(2, 4, 20)
    g.insert(3, 5, 25)
    print(g.adjacency_list)