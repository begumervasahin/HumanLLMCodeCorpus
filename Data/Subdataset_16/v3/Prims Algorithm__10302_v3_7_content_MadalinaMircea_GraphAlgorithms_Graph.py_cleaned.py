class class1:
    def fonk1(self, n):
        '''
        Creates a b4 with n vertices (numbered from 0 to n-1) and no edges.
        '''
        self.b1 = n
        self.a1 = 0
        self.b2 = {i: [] for i in range(n)}
    def fonk2(self, vertex):
        '''
        Returns True if vertex is a vertex, False otherwise.
        '''
        return vertex in self.b2
    def fonk3(self):
        '''
        Returns a list containing all the vertices.
        '''
        return list(self.b2.keys())
    def fonk4(self, vertex):
        '''
        Returns a list containing the neighbours of vertex.
        Returns False if vertex is not a vertex.
        '''
        if self.fonk2(vertex):
            return self.b2[vertex]
        return False
    def fonk5(self, vertex1, vertex2):
        '''
        Returns True if there is an edge from vertex1 to vertex2, False otherwise.
        Also returns False if one or both of the vertices do not exist.
        '''
        if self.fonk2(vertex1):
            return vertex2 in self.b2[vertex1]
        return False
    def fonk6(self, vertex1, vertex2):
        '''
        Adds an edge from vertex1 to vertex2.
        Returns True if the edge was added, False if the edge already exists.
        '''
        if not self.fonk5(vertex1, vertex2):
            self.b2[vertex1].append(vertex2)
            self.b2[vertex2].append(vertex1)
            self.a1 += 1
            return True
        return False
    def fonk7(self):
        '''
        Returns the number of vertices.
        '''
        return self.b1
    def fonk8(self):
        '''
        Returns the number of edges.
        '''
        return self.a1
    def fonk9(self, vertex):
        '''
        Returns the degree of the vertex.
        Returns False if vertex does not exist.
        '''
        if self.fonk2(vertex):
            return len(self.b2[vertex])
        return False
if b3 = = "__main__":
    b4 = class1(5)
    print("All vertices:", b4.fonk3())
    print("Add edge 0-1:", b4.fonk6(0, 1))
    print("Add edge 0-2:", b4.fonk6(0, 2))
    print("Add edge 1-2:", b4.fonk6(1, 2))
    print("Add edge 1-3:", b4.fonk6(1, 3))
    print("Is edge 0-1:", b4.fonk5(0, 1))
    print("Is edge 0-3:", b4.fonk5(0, 3))
    print("Number of edges:", b4.fonk8())
    print("Number of vertices:", b4.fonk7())
    print("Degree of vertex 1:", b4.fonk9(1))
    print("Degree of vertex 4:", b4.fonk9(4))
    print("Neighbours of vertex 1:", b4.fonk4(1))
