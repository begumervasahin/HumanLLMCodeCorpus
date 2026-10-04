class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []
    def add_edge(self, destination, weight):
        self.edges.append(Edge(self.name, destination, weight))
    def get_name(self):
        return self.name
    def get_edges(self):
        return self.edges
    def has_edge(self, destination):
        for edge in self.edges:
            if edge.get_terminal() == destination:
                return edge
        return None
class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight
    def get_start(self):
        return self.start
    def get_terminal(self):
        return self.end
    def get_weight(self):
        return self.weight
    def __lt__(self, other):
        return self.weight < other.weight
class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []
    def add_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = Node(name)
    def add_edge(self, start, end, weight):
        if start in self.nodes and end in self.nodes:
            self.nodes[start].add_edge(end, weight)
            self.nodes[end].add_edge(start, weight)
            self.edges.append(Edge(start, end, weight))
    def get_node_names(self):
        return list(self.nodes.keys())
    def get_node(self, name):
        return self.nodes.get(name)
    def get_edges(self):
        return sorted(self.edges)
class KruskalAlgorithm:
    def apply_kruskal(self, graph):
        mst = Graph()
        node_names = graph.get_node_names()
        for name in node_names:
            mst.add_node(name)
        edges = graph.get_edges()
        for edge in edges:
            if not self.does_create_cycle(mst, edge):
                mst.add_edge(edge.get_start(), edge.get_terminal(), edge.get_weight())
        return mst
    def does_create_cycle(self, graph, edge_to_check):
        parent = {}
        rank = {}
        def find(vertex):
            if parent[vertex] != vertex:
                parent[vertex] = find(parent[vertex])
            return parent[vertex]
        def union(vertex1, vertex2):
            root1 = find(vertex1)
            root2 = find(vertex2)
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1
        for node in graph.get_node_names():
            parent[node] = node
            rank[node] = 0
        for edge in graph.get_edges():
            root1 = find(edge.get_start())
            root2 = find(edge.get_terminal())
            if root1 != root2:
                union(root1, root2)
        root1 = find(edge_to_check.get_start())
        root2 = find(edge_to_check.get_terminal())
        return root1 == root2
if __name__ == "__main__":
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 3)
    graph.add_edge("B", "C", 1)
    graph.add_edge("B", "D", 4)
    graph.add_edge("C", "D", 2)
    kruskal = KruskalAlgorithm()
    mst = kruskal.apply_kruskal(graph)
    print("Minimum Spanning Tree:")
    for node_name in mst.get_node_names():
        edges = mst.get_node(node_name).get_edges()
        for edge in edges:
            print(f"{edge.get_start()} -- {edge.get_terminal()} == {edge.get_weight()}")