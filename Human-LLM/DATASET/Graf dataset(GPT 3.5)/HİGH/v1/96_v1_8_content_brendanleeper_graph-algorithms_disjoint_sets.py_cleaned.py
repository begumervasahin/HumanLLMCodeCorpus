class class1:
    ''' Uses a disjoint set implementation to build a complete b6 '''
    b1 = {}
    b2 = {}
    b3 = {}
    def fonk1(self, numvertices, numedges):
        ''' Create the b6 '''
        print("Initializing b6")
    def fonk2(self, x):
        ''' Creates a new set '''
        self.b1[x] = 0
        self.b2[x] = x
        self.b3[x] = set([x])
    def fonk3(self, node):
        ''' Finds the representative of the specified vertex '''
        if self.b2[node] == node:
            return node
        else:
            return self.fonk3(self.b2[node])
    def fonk4(self, x, y):
        ''' Merges two sets '''
        b4 = self.fonk3(x)
        b5 = self.fonk3(y)
        if b4 != b5:
            if self.b1[b4] > self.b1[b5]:
                self.b2[b5] = b4
                self.b1[b4] += 1
                self.b3[b4] = self.b3[b4] | self.b3[b5]
                self.b3.pop(b5)
            else:
                self.b2[b4] = b5
                self.b1[b5] += 1
                self.b3[b5] = self.b3[b5] | self.b3[b4]
                self.b3.pop(b4)
    def fonk5(self):
        return self.b3
a1 = 5
a2 = 4
b6 = class1(a1, a2)
for i in range(a1):
    b6.fonk2(i)
b7 = [(0, 1), (1, 2), (3, 4), (2, 3)]
for edge in b7:
    b6.fonk4(*edge)
print("Representative members of each set:")
print(b6.fonk5())