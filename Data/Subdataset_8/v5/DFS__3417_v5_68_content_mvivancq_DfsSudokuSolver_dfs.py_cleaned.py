class SimpleGraph:
    def __init__(self):
        self.edges = {}
    def get_neighbors(self, node_id):
        return self.edges.get(node_id, [])
    def print_graph(self):
        for node, neighbors in self.edges.items():
            print(f"Node {node}: Neighbors {neighbors}")
class Stack:
    def __init__(self):
        self.elements = []
    def is_empty(self):
        return len(self.elements) == 0
    def push(self, item):
        self.elements.append(item)
    def pop(self):
        return self.elements.pop()
def depth_first_search(graph, start_node):
    frontier = Stack()
    frontier.push(start_node)
    visited = {start_node: True}
    while not frontier.is_empty():
        current_node = frontier.pop()
        print("Visiting node:", current_node)
        for neighbor_node in graph.get_neighbors(current_node):
            if neighbor_node not in visited:
                frontier.push(neighbor_node)
                visited[neighbor_node] = True
if __name__ == "__main__":
    example_graph = SimpleGraph()
    example_graph.edges = {
        'A': ['B'],
        'B': ['A', 'C', 'D'],
        'C': ['A'],
        'D': ['E', 'A'],
        'E': ['B']
    }
    depth_first_search(example_graph, 'A')