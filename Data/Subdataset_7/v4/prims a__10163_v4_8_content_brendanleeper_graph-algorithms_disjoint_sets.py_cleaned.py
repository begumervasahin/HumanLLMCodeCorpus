class class1:
    '''
    This class class2 an undirected connected weighted graph.
    It uses a disjoint set implementation to build the graph.
    '''
    def fonk1(self, numvertices, numedges):
        '''
        Initializes the graph with the given number of vertices and edges.
        '''
        print("Initializing graph")
        self.b1 = {}
        self.b2 = {}
        self.b3 = {}
    def fonk2(self, x):
        '''
        Creates a new set with the given vertex.
        '''
        self.b1[x] = 0
        self.b2[x] = x
        self.b3[x] = {x}
    def fonk3(self, node):
        '''
        Finds the representative of the specified vertex.
        '''
        if self.b2[node] == node:
            return node
        else:
            self.b2[node] = self.fonk3(self.b2[node])
            return self.b2[node]
    def fonk4(self, x, y):
        '''
        Merges the sets containing vertices x and y.
        '''
        b4 = self.fonk3(x)
        b5 = self.fonk3(y)
        if b4 != b5:
            if len(self.b3[b4]) > len(self.b3[b5]):
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
        Returns the representative members of all sets.
        '''
        return self.b3