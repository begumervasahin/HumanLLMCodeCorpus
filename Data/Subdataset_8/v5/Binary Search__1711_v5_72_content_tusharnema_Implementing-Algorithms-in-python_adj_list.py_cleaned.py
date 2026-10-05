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
        for n, cxns in self.graph.items():
            cxns.discard(node)
        self.graph.pop(node, None)
    def is_connected(self, node1, node2):
        return node1 in self.graph and node2 in self.graph[node1]
    def find_path(self, node1, node2, path=None):
        if path is None:
            path = []
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self.graph:
            return None
        for node in self.graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None
    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.graph))
    def check(self):
        for node, connections in self.graph.items():
            print(node, '--->', connections)
        print(self.graph['B'])
    def BFS(self, start_node):
        visited = set()
        queue = deque()
        queue.append(start_node)
        visited.add(start_node)
        while queue:
            current_node = queue.popleft()
            print(current_node, end=" --> ")
            for adjacent_node in self.graph[current_node]:
                if adjacent_node not in visited:
                    queue.append(adjacent_node)
                    visited.add(adjacent_node)
    def DFS(self, start_node):
        visited = set()
        self.DFS_track(start_node, visited)
    def DFS_track(self, current_node, visited):
        visited.add(current_node)
        print(current_node, end=" --> ")
        for adjacent_node in self.graph[current_node]:
            if adjacent_node not in visited:
                self.DFS_track(adjacent_node, visited)
connections = [(0, 1), (1, 2), (2, 3), (2, 4),
               (3, 4), (5, 6), (7, 3)]
g = Graph(connections)
g.add_connections([[6, 8], [8, 4], [9, 10]])
print(g.graph)
print()
print("Breadth-First Search:")
g.BFS(0)
print()
print("Depth-First Search:")
g.DFS(0)