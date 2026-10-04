class class1:
    def fonk1(self, n):
        '''
        Creates a graph with n vertices (numbered from 0 to n-1) and no edges.
        '''
        self.b1 = n
        self.a1 = 0
        self.b2 = {i: [] for i in range(n)}
    def fonk2(self, x):
        '''
        Returns True if x is a vertex, False otherwise.
        '''
        return x in self.b2
    def fonk3(self):
        '''
        Returns a list containing all the vertices.
        '''
        return list(self.b2.keys())
    def fonk4(self, x):
        '''
        Returns a list containing the neighbours of vertex x.
        Returns False if x is not a vertex.
        '''
        if self.fonk2(x):
            return self.b2[x]
        return False
    def fonk5(self, x, y):
        '''
        Returns True if there is an edge from x to y, False otherwise.
        Also returns False if one or both of the vertices do not exist.
        '''
        if self.fonk2(x):
            return y in self.b2[x]
        return False
    def fonk6(self, x, y):
        '''
        Adds an edge from x to y.
        Returns True if the edge was added, False if the edge already exists.
        '''
        if not self.fonk5(x, y):
            self.b2[x].append(y)
            self.b2[y].append(x)
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
    def fonk9(self, x):
        '''
        Returns the degree of the vertex x.
        Returns False if x does not exist.
        '''
        if self.fonk2(x):
            return len(self.b2[x])
        return False
if b3 = = "__main__":
    b4 = class1(5)
    print(b4.fonk3())
    print(b4.fonk6(0, 1))
    print(b4.fonk6(0, 2))
    print(b4.fonk6(1, 2))
    print(b4.fonk6(1, 3))
    print(b4.fonk5(0, 1))
    print(b4.fonk5(0, 3))
    print(b4.fonk8())
    print(b4.fonk7())
    print(b4.fonk9(1))
    print(b4.fonk9(4))
    print(b4.fonk4(1))
