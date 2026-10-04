__author__ = 'Milosz Chodkowski PUT'
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = {i: [] for i in range(num_vertices)}
        self.path = []
        self._initialize_graph()
    def _initialize_graph(self):
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
        def _dfs(v):
            visited.add(v)
            self.path.append(v)
            for neighbor in self.adj_list[v]:
                if neighbor not in visited:
                    _dfs(neighbor)
        _dfs(0)
if __name__ == "__main__":
    G = Graph(10)
    print("Adjacency List:", G.adj_list)
    G.dfs()
    print("DFS Path:", G.path)