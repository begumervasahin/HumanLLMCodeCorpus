class class1:
    ''' Uses a disjoint set implementation to build a complete graph '''
    b1 = {}
    b2 = {}
    b3 = {}
    def fonk1(self, numvertices, numedges):
        ''' Create the graph '''
        print "initializing graph"
    def fonk2(self, x):
        ''' Creates an new set '''
        self.b1[x] = 0
        self.b2[x] = x
        self.b3[x] = set(x)
    def fonk3(self, node):
        ''' Finds the representative of the specified vertex '''
        if self.b2[x] == x:
            return x
        else:
            return self.fonk3(b2[x])
    def fonk4(self, x, y):
        ''' Merges two sets '''
        b4 = self.fonk3(x)
        b5 = self.fonk3(y)
        if self.b1[b4] > self.b1[b5]:
            self.b2[b5] = b4
            self.b1[b4] += 1
            self.b3[b4] = self.b3[b4] | self.b3[b5]
            self.b3[b5].pop()
        else:
            self.b2[b4] = b5
            self.b1[b5] += 1
            self.b3[b5] = self.b3[b5] | self.b3[b4]
            self.b3[b4].pop()
    def fonk5(self):
        return self.b3