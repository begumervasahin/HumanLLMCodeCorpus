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
    def find_path(self, node1, node2, path=[]):
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
        for n, k in self.graph.items():
            print(n, '--->', k)
        print(self.graph['B'])
    def BFS(self, s):
        visited = [False] * (len(self.graph))
        queue = deque()
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.popleft()
            print(s, end="-->")
            for nodes in self.graph[s]:
                if not visited[nodes]:
                    queue.append(nodes)
                    visited[nodes] = True
    def DFS(self, s):
        visited = [False] * (len(self.graph))
        self.DFS_track(s, visited)
    def DFS_track(self, s, visited):
        visited[s] = True
        print(s, end="-->")
        for nodes in self.graph[s]:
            if not visited[nodes]:
                visited[nodes] = True
                self.DFS_track(nodes, visited)
connections = [(0, 1), (1, 2), (2, 3), (2, 4), (3, 4), (5, 6), (7, 3)]
g = Graph(connections)
g.add_connections([[6, 8], [8, 4], [9, 10]])
print(g.graph)
print()
g.BFS(0)
print()
g.DFS(0)