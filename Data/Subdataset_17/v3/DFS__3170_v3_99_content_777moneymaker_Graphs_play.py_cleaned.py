__author__ = 'Milosz Chodkowski PUT'
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = {i: [] for i in range(num_vertices)}
        self.path = []
        self._populate_graph()
    def _populate_graph(self):
        for i in range(self.num_vertices):
            if i < self.num_vertices - 1:
                self.add_edge(i, i + 1)
            if i % 2 == 0 and i + 2 < self.num_vertices:
                self.add_edge(i, i + 2)
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    def dfs(self):
        visited = set()
        self.path = []
        def _dfs(vertex):
            visited.add(vertex)
            self.path.append(vertex)
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    _dfs(neighbor)
        if self.num_vertices > 0:
            _dfs(0)
if __name__ == "__main__":
    graph = Graph(10)
    print("Adjacency List:", graph.adj_list)
    graph.dfs()
    print("DFS Path:", graph.path)