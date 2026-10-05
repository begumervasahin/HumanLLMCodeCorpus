class UndirectedConnectedWeightedGraph:
    '''
    Represents a weighted undirected connected graph using disjoint set implementation.
    '''
    def __init__(self, num_vertices, num_edges):
        '''
        Initializes the graph with the specified number of vertices and edges.
        '''
        print("Initializing graph")
        self.weights = {}
        self.parents = {}
        self.rep_members = {}
    def make_set(self, vertex):
        '''
        Creates a new set with a single vertex.
        '''
        self.weights[vertex] = 0
        self.parents[vertex] = vertex
        self.rep_members[vertex] = {vertex}
    def find(self, vertex):
        '''
        Finds the representative of the set that contains the specified vertex.
        '''
        if self.parents[vertex] == vertex:
            return vertex
        else:
            return self.find(self.parents[vertex])
    def union(self, vertex_x, vertex_y):
        '''
        Merges two sets containing the specified vertices.
        '''
        root_x = self.find(vertex_x)
        root_y = self.find(vertex_y)
        if root_x != root_y:
            if self.weights[root_x] > self.weights[root_y]:
                self.parents[root_y] = root_x
                self.weights[root_x] += 1
                self.rep_members[root_x].update(self.rep_members[root_y])
                del self.rep_members[root_y]
            else:
                self.parents[root_x] = root_y
                self.weights[root_y] += 1
                self.rep_members[root_y].update(self.rep_members[root_x])
                del self.rep_members[root_x]
    def done(self):
        '''
        Returns representative members of each set in the disjoint set.
        '''
        return self.rep_members
num_vertices = 5
num_edges = 4
graph = UndirectedConnectedWeightedGraph(num_vertices, num_edges)
for vertex in range(num_vertices):
    graph.make_set(vertex)
edges = [(0, 1), (1, 2), (3, 4), (2, 3)]
for edge in edges:
    graph.union(*edge)
print("Representative members of each set:")
print(graph.done())