from collections import defaultdict
class Graph:
    def __init__(self, count):
        self.graph = defaultdict(list)
        self.count = count
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def DFS(self, s, g):
        visited = [False] * self.count
        stack = [s]
        visited[s] = True
        while stack:
            s = stack.pop()
            print(s, end=" ")
            if s == g:
                print("Goal found.")
                return 0
            for i in self.graph[s]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = True
        print("Search failed.")
        return 0
with open('input.txt', 'r') as inputFile:
    count = int(inputFile.readline())
    start = int(inputFile.readline())
    goal = int(inputFile.readline())
    graph = Graph(count)
    for line in inputFile.readlines():
        u, v = map(int, line.split())
        graph.add_edge(u, v)
graph.DFS(start, goal)