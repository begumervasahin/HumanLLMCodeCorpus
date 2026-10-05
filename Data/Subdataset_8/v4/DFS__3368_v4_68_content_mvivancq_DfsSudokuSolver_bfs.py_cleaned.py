class SimpleGraph:
    def __init__(self):
        self.edges = {}
    def neighbors(self, node_id):
        return self.edges.get(node_id, [])
    def print_graph(self):
        for node, neighbors in self.edges.items():
            print(f"{node}: {neighbors}")
if __name__ == "__main__":
    example_graph = SimpleGraph()
    example_graph.edges = {
        'A': ['B'],
        'B': ['A', 'C', 'D'],
        'C': ['A'],
        'D': ['E', 'A'],
        'E': ['B']
    }
    import collections
    class Queue:
        def __init__(self):
            self.elements = collections.deque()
        def empty(self):
            return len(self.elements) == 0
        def put(self, item):
            self.elements.append(item)
        def get(self):
            return self.elements.popleft()
    def breadth_first_search(graph, start_node):
        frontier = Queue()
        frontier.put(start_node)
        visited = {start_node: True}
        while not frontier.empty():
            current_node = frontier.get()
            print("Visiting", current_node)
            for neighbor_node in graph.neighbors(current_node):
                if neighbor_node not in visited:
                    frontier.put(neighbor_node)
                    visited[neighbor_node] = True
    breadth_first_search(example_graph, 'A')