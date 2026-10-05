from collections import defaultdict
class Graph:
    def __init__(self, count):
        self.graph = defaultdict(list)
        self.count = count
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFS(self, s, g):
        visited = [False] * self.count
        stack = []
        stack.insert(0,s)
        visited[s] = True
        while stack:
            s = stack.pop(0)
            print (s, end = " ")
            if s == g:
                print("Goal found.")
                return 0
            for i in self.graph[s]:
                if visited[i] == False:
                    stack.insert(0,i)
                    visited[i] = True
        print("Search failed.")
        return 0
with open('input.txt', 'rb') as inputFile:
    count = int(inputFile.readline())
    a = int(inputFile.readline())
    b = int(inputFile.readline())
    g = Graph(count)
    for i in inputFile.readlines():
        g.addEdge(int(i.split()[0]), int(i.split()[1]))
g.DFS(a,b)