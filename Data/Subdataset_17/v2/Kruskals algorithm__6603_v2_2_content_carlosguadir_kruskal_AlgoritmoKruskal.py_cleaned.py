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
        return -1
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
        return self.nodes[name]
    def get_edges(self):
        return sorted(self.edges, key=lambda edge: edge.get_weight())
class KruskalAlgorithm:
    def apply_kruskal(self, graph):
        mst = Graph()
        node_names = graph.get_node_names()
        for name in node_names:
            mst.add_node(name)
        edges = graph.get_edges()
        while edges:
            edge = edges.pop(0)
            if not self.does_create_cycle(mst, edge, mst.get_node(edge.get_terminal()), edge.get_terminal()):
                mst.add_edge(edge.get_start(), edge.get_terminal(), edge.get_weight())
        return mst
    def does_create_cycle(self, graph, edge_to_check, terminal_node, last_node_name):
        edges = terminal_node.get_edges()
        if not edges:
            return False
        if terminal_node.has_edge(edge_to_check.get_start()) != -1:
            return True
        for edge in edges:
            next_node = graph.get_node(edge.get_terminal())
            if next_node.get_name() != last_node_name:
                if self.does_create_cycle(graph, edge_to_check, next_node, terminal_node.get_name()):
                    return True
        return False
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