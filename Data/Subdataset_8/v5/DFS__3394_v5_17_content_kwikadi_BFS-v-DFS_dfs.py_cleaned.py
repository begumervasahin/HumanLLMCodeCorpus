from collections import defaultdict
class Graph:
    def __init__(self, num_nodes):
        self.graph = defaultdict(list)
        self.num_nodes = num_nodes
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def depth_first_search(self, start_node, goal_node):
        visited = [False] * self.num_nodes
        stack = [start_node]
        visited[start_node] = True
        while stack:
            current_node = stack.pop()
            print(current_node, end=" ")
            if current_node == goal_node:
                print("Goal found.")
                return True
            for neighbor in self.graph[current_node]:
                if not visited[neighbor]:
                    stack.append(neighbor)
                    visited[neighbor] = True
        print("Goal not reachable.")
        return False
with open('input.txt', 'r') as input_file:
    num_nodes = int(input_file.readline())
    start_node = int(input_file.readline())
    goal_node = int(input_file.readline())
    graph = Graph(num_nodes)
    for line in input_file.readlines():
        u, v = map(int, line.split())
        graph.add_edge(u, v)
graph.depth_first_search(start_node, goal_node)