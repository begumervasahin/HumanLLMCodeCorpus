class Edge:
    def __init__(self, start_node, end_node, weight):
        self.start_node = start_node
        self.end_node = end_node
        self.weight = weight
    def __repr__(self):
        return f"Edge: {self.start_node} --({self.weight})--> {self.end_node}"
edges = [
    Edge('a', 'b', 5),
    Edge('b', 'c', 7),
    Edge('c', 'd', 3)
]
for edge in edges:
    print(edge)