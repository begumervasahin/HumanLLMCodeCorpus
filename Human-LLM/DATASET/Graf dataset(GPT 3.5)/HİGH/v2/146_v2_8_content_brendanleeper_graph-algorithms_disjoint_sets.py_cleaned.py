class class1:
    '''
    Represents a weighted undirected connected b6 using disjoint set implementation.
    '''
    def fonk1(self, a1, a2):
        '''
        Initializes the b6 with the specified number of vertices and b7.
        '''
        print("Initializing b6")
        self.b1 = {}
        self.b2 = {}
        self.b3 = {}
    def fonk2(self, vertex):
        '''
        Creates a new set with a single vertex.
        '''
        self.b1[vertex] = 0
        self.b2[vertex] = vertex
        self.b3[vertex] = {vertex}
    def fonk3(self, vertex):
        '''
        Finds the representative of the set that contains the specified vertex.
        '''
        if self.b2[vertex] == vertex:
            return vertex
        else:
            return self.fonk3(self.b2[vertex])
    def fonk4(self, vertex_x, vertex_y):
        '''
        Merges two sets containing the specified vertices.
        '''
        b4 = self.fonk3(vertex_x)
        b5 = self.fonk3(vertex_y)
        if b4 != b5:
            if self.b1[b4] > self.b1[b5]:
                self.b2[b5] = b4
                self.b1[b4] += 1
                self.b3[b4] |= self.b3[b5]
                del self.b3[b5]
            else:
                self.b2[b4] = b5
                self.b1[b5] += 1
                self.b3[b5] |= self.b3[b4]
                del self.b3[b4]
    def fonk5(self):
        '''
        Returns representative members of each set in the disjoint set.
        '''
        return self.b3
a1 = 5
a2 = 4
b6 = class1(a1, a2)
for vertex in range(a1):
    b6.fonk2(vertex)
b7 = [(0, 1), (1, 2), (3, 4), (2, 3)]
for edge in b7:
    b6.fonk4(*edge)
print("Representative members of each set:")
print(b6.fonk5())