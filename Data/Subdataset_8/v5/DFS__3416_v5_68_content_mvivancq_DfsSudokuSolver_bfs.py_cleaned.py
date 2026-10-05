import collections
class SimpleGraph:
    def __init__(self):
        self.edges = {}
    def neighbors(self, node_id):
        return self.edges.get(node_id, [])
    def print_graph(self):
        for node, neighbors in self.edges.items():
            print(f"{node}: {neighbors}")
class Queue:
    def __init__(self):
        self.elements = collections.deque()
    def is_empty(self):
        return len(self.elements) == 0
    def enqueue(self, item):
        self.elements.append(item)
    def dequeue(self):
        return self.elements.popleft()
def breadth_first_search(graph, start_node):
    frontier = Queue()
    frontier.enqueue(start_node)
    visited = {start_node: True}
    while not frontier.is_empty():
        current_node = frontier.dequeue()
        print("Visiting", current_node)
        for neighbor_node in graph.neighbors(current_node):
            if neighbor_node not in visited:
                frontier.enqueue(neighbor_node)
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
    breadth_first_search(example_graph, 'A')