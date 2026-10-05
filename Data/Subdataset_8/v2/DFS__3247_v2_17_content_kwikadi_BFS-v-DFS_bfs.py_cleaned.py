from collections import defaultdict
class Graph:
    def __init__(self, count):
        self.graph = defaultdict(list)
        self.count = count
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def BFS(self, start, goal):
        visited = [False] * self.count
        queue = [start]
        visited[start] = True
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex, end=" ")
            if current_vertex == goal:
                print("Goal found.")
                return
            for neighbor in self.graph[current_vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        print("Search failed.")
def main():
    with open('input.txt', 'r') as inputFile:
        count = int(inputFile.readline())
        start_vertex = int(inputFile.readline())
        goal_vertex = int(inputFile.readline())
        graph = Graph(count)
        for line in inputFile:
            u, v = map(int, line.split())
            graph.addEdge(u, v)
    graph.BFS(start_vertex, goal_vertex)
if __name__ == "__main__":
    main()