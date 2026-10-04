class Graph:
    def __init__(self, n):
        '''
        Creates a graph with n vertices (numbered from 0 to n-1) and no edges.
        '''
        self.nrVertices = n
        self.nrEdges = 0
        self.adjacency_list = {i: [] for i in range(n)}
    def is_vertex(self, vertex):
        '''
        Returns True if vertex is a vertex, False otherwise.
        '''
        return vertex in self.adjacency_list
    def get_all_vertices(self):
        '''
        Returns a list containing all the vertices.
        '''
        return list(self.adjacency_list.keys())
    def get_neighbours(self, vertex):
        '''
        Returns a list containing the neighbours of vertex.
        Returns False if vertex is not a vertex.
        '''
        if self.is_vertex(vertex):
            return self.adjacency_list[vertex]
        return False
    def is_edge(self, vertex1, vertex2):
        '''
        Returns True if there is an edge from vertex1 to vertex2, False otherwise.
        Also returns False if one or both of the vertices do not exist.
        '''
        if self.is_vertex(vertex1):
            return vertex2 in self.adjacency_list[vertex1]
        return False
    def add_edge(self, vertex1, vertex2):
        '''
        Adds an edge from vertex1 to vertex2.
        Returns True if the edge was added, False if the edge already exists.
        '''
        if not self.is_edge(vertex1, vertex2):
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            self.nrEdges += 1
            return True
        return False
    def get_number_of_vertices(self):
        '''
        Returns the number of vertices.
        '''
        return self.nrVertices
    def get_number_of_edges(self):
        '''
        Returns the number of edges.
        '''
        return self.nrEdges
    def get_degree(self, vertex):
        '''
        Returns the degree of the vertex.
        Returns False if vertex does not exist.
        '''
        if self.is_vertex(vertex):
            return len(self.adjacency_list[vertex])
        return False
if __name__ == "__main__":
    graph = Graph(5)
    print("All vertices:", graph.get_all_vertices())
    print("Add edge 0-1:", graph.add_edge(0, 1))
    print("Add edge 0-2:", graph.add_edge(0, 2))
    print("Add edge 1-2:", graph.add_edge(1, 2))
    print("Add edge 1-3:", graph.add_edge(1, 3))
    print("Is edge 0-1:", graph.is_edge(0, 1))
    print("Is edge 0-3:", graph.is_edge(0, 3))
    print("Number of edges:", graph.get_number_of_edges())
    print("Number of vertices:", graph.get_number_of_vertices())
    print("Degree of vertex 1:", graph.get_degree(1))
    print("Degree of vertex 4:", graph.get_degree(4))
    print("Neighbours of vertex 1:", graph.get_neighbours(1))
