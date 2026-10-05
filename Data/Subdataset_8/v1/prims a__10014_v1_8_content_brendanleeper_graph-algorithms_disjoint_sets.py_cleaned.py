class UndirectedConnectedWeightedGraph:
    ''' Uses a disjoint set implementation to build a complete graph '''
    weights = {}
    parents = {}
    rep_members = {}
    def __init__(self, numvertices, numedges):
        ''' Create the graph '''
        print("Initializing graph")
    def makeSet(self, x):
        ''' Creates a new set '''
        self.weights[x] = 0
        self.parents[x] = x
        self.rep_members[x] = set([x])
    def find(self, node):
        ''' Finds the representative of the specified vertex '''
        if self.parents[node] == node:
            return node
        else:
            return self.find(self.parents[node])
    def union(self, x, y):
        ''' Merges two sets '''
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            if self.weights[xroot] > self.weights[yroot]:
                self.parents[yroot] = xroot
                self.weights[xroot] += 1
                self.rep_members[xroot] = self.rep_members[xroot] | self.rep_members[yroot]
                self.rep_members.pop(yroot)
            else:
                self.parents[xroot] = yroot
                self.weights[yroot] += 1
                self.rep_members[yroot] = self.rep_members[yroot] | self.rep_members[xroot]
                self.rep_members.pop(xroot)
    def done(self):
        return self.rep_members
num_vertices = 5
num_edges = 4
graph = UndirectedConnectedWeightedGraph(num_vertices, num_edges)
for i in range(num_vertices):
    graph.makeSet(i)
edges = [(0, 1), (1, 2), (3, 4), (2, 3)]
for edge in edges:
    graph.union(*edge)
print("Representative members of each set:")
print(graph.done())