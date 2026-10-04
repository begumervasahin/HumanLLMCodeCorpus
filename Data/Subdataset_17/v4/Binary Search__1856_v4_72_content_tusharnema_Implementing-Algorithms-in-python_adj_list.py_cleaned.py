from collections import defaultdict, deque
class Graph:
    def __init__(self, connections, directed=False):
        self.graph = defaultdict(set)
        self.directed = directed
        self.add_connections(connections)
    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)
    def add(self, node1, node2):
        self.graph[node1].add(node2)
        if not self.directed:
            self.graph[node2].add(node1)
    def remove(self, node):
        for n, connections in self.graph.items():
            connections.discard(node)
        self.graph.pop(node, None)
    def is_connected(self, node1, node2):
        return node1 in self.graph and node2 in self.graph[node1]
    def find_path(self, node1, node2, path=None):
        if path is None:
            path = []
        path.append(node1)
        if node1 == node2:
            return path
        if node1 not in self.graph:
            return None
        for neighbor in self.graph[node1]:
            if neighbor not in path:
                new_path = self.find_path(neighbor, node2, path.copy())
                if new_path:
                    return new_path
        return None
    def bfs(self, start):
        visited = [False] * len(self.graph)
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            print(node, end="-->")
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        print("End")
    def dfs(self, start):
        visited = [False] * len(self.graph)
        self._dfs_util(start, visited)
        print("End")
    def _dfs_util(self, node, visited):
        visited[node] = True
        print(node, end="-->")
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self._dfs_util(neighbor, visited)
    def __str__(self):
        return f'{self.__class__.__name__}({dict(self.graph)})'
connections = [(0, 1), (1, 2), (2, 3), (2, 4),
               (3, 4), (5, 6), (7, 3)]
g = Graph(connections)
g.add_connections([(6, 8), (8, 4), (9, 10)])
print("Graph representation:")
print(g)
print("\nBFS traversal starting from node 0:")
g.bfs(0)
print("\nDFS traversal starting from node 0:")
g.dfs(0)