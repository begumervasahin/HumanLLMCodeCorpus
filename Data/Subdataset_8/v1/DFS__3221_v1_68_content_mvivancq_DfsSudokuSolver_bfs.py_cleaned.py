import collections
class SimpleGraph:
    def __init__(self):
        self.edges = {}
    def neighbors(self, node):
        return self.edges[node]
    def print_graph(self):
        for node, neighbors in self.edges.items():
            print(node, neighbors)
class Queue:
    def __init__(self):
        self.elements = collections.deque()
    def empty(self):
        return len(self.elements) == 0
    def put(self, x):
        self.elements.append(x)
    def get(self):
        return self.elements.popleft()
def breadth_first_search(graph, start):
    frontier = Queue()
    frontier.put(start)
    visited = {start: True}
    while not frontier.empty():
        current = frontier.get()
        print("Visiting", current)
        for next_node in graph.neighbors(current):
            if next_node not in visited:
                frontier.put(next_node)
                visited[next_node] = True
example_graph = SimpleGraph()
example_graph.edges = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}
breadth_first_search(example_graph, 'A')