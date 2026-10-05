from collections import defaultdict
class Graph:
    def __init__(self, num_nodes):
        self.graph = defaultdict(list)
        self.num_nodes = num_nodes
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def depth_first_search(self, start, goal):
        visited = [False] * self.num_nodes
        stack = [start]
        visited[start] = True
        while stack:
            current_node = stack.pop()
            print(current_node, end=" ")
            if current_node == goal:
                print("Goal found.")
                return True
            for neighbor in self.graph[current_node]:
                if not visited[neighbor]:
                    stack.append(neighbor)
                    visited[neighbor] = True
        print("Search failed.")
        return False
with open('input.txt', 'r') as inputFile:
    num_nodes = int(inputFile.readline())
    start_node = int(inputFile.readline())
    goal_node = int(inputFile.readline())
    graph = Graph(num_nodes)
    for line in inputFile.readlines():
        u, v = map(int, line.split())
        graph.add_edge(u, v)
graph.depth_first_search(start_node, goal_node)