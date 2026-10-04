from collections import defaultdict, deque
class Graph:
    def __init__(self, connections=None, directed=False):
        self.graph = defaultdict(set)
        self.directed = directed
        if connections:
            self.add_connections(connections)
    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)
    def add(self, node1, node2):
        self.graph[node1].add(node2)
        if not self.directed:
            self.graph[node2].add(node1)
    def remove(self, node):
        for neighbors in self.graph.values():
            neighbors.discard(node)
        self.graph.pop(node, None)
    def is_connected(self, node1, node2):
        return node2 in self.graph.get(node1, set())
    def find_path(self, start_node, end_node, path=None):
        if path is None:
            path = []
        path.append(start_node)
        if start_node == end_node:
            return path
        if start_node not in self.graph:
            return None
        for neighbor in self.graph[start_node]:
            if neighbor not in path:
                new_path = self.find_path(neighbor, end_node, path.copy())
                if new_path:
                    return new_path
        return None
    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        while queue:
            node = queue.popleft()
            print(node, end=" --> ")
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        print("End")
    def dfs(self, start_node):
        visited = set()
        self._dfs_util(start_node, visited)
        print("End")
    def _dfs_util(self, node, visited):
        visited.add(node)
        print(node, end=" --> ")
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs_util(neighbor, visited)
    def __str__(self):
        return f'Graph({dict(self.graph)})'
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