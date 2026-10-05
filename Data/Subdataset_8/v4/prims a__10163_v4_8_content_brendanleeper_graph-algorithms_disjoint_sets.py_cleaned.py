class UndirectedConnectedWeightedGraph:
    '''
    This class represents an undirected connected weighted graph.
    It uses a disjoint set implementation to build the graph.
    '''
    def __init__(self, numvertices, numedges):
        '''
        Initializes the graph with the given number of vertices and edges.
        '''
        print("Initializing graph")
        self.weights = {}
        self.parents = {}
        self.rep_members = {}
    def makeSet(self, x):
        '''
        Creates a new set with the given vertex.
        '''
        self.weights[x] = 0
        self.parents[x] = x
        self.rep_members[x] = {x}
    def find(self, node):
        '''
        Finds the representative of the specified vertex.
        '''
        if self.parents[node] == node:
            return node
        else:
            self.parents[node] = self.find(self.parents[node])
            return self.parents[node]
    def union(self, x, y):
        '''
        Merges the sets containing vertices x and y.
        '''
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            if len(self.rep_members[xroot]) > len(self.rep_members[yroot]):
                self.parents[yroot] = xroot
                self.weights[xroot] += 1
                self.rep_members[xroot] |= self.rep_members[yroot]
                del self.rep_members[yroot]
            else:
                self.parents[xroot] = yroot
                self.weights[yroot] += 1
                self.rep_members[yroot] |= self.rep_members[xroot]
                del self.rep_members[xroot]
    def done(self):
        '''
        Returns the representative members of all sets.
        '''
        return self.rep_members