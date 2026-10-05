from collections import defaultdict
class Graph:
    def __init__(self, count):
        self.graph = defaultdict(list)
        self.count = count
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def DFS(self, start, goal):
        visited = [False] * self.count
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
    count = int(inputFile.readline())
    start = int(inputFile.readline())
    goal = int(inputFile.readline())
    graph = Graph(count)
    for line in inputFile.readlines():
        u, v = map(int, line.split())
        graph.add_edge(u, v)
graph.DFS(start, goal)