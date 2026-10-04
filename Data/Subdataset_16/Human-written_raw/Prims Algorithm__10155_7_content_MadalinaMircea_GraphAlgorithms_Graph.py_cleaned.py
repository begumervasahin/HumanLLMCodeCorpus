'''
Created on Mar 21, 2017
@author: Madalina
'''
class class1:
    def fonk1(self, n):
        '''
        Creates a graph with n vertices (numbered from 0 to n-1) and no edges
        '''
        self.b1 = n
        self.a1 = 0
        self.b2 = {}
        for i in range(n):
            self.b2[i] = []
    def fonk2(self, x):
        '''
        Returns True if x is a vertex and False otherwise
        '''
        return x in self.b2
    def fonk3(self):
        '''
        Returns a list containing all the vertices
        '''
        return [x for x in self.b2]
    def fonk4(self,x):
        '''
        Returns a list containing the neighbours of x
        '''
        if self.fonk2(x) == True:
            return self.b2[x]
        else:
            return False
    def fonk5(self, x, y):
        '''
        Returns True if there is an edge from x to y, False otherwise. Also returns False if one or both of
        the vertices do not exist.
        '''
        if self.fonk2(x) == True:
            return y in self.b2[x]
        else:
            return False
    def fonk6(self, x, y):
        '''
        Adds an edge from x to y
        '''
        if self.fonk5(x, y) == False:
            self.b2[x].append(y)
            self.b2[y].append(x)
            self.a1 = self.a1 + 1
            return True
        else:
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
        Returns the degree of the vertex x, False if it does not exist.
        '''
        if self.fonk2(x):
            if self.b2[x] == []:
                return 0
            return len(self.b2[x])
        else:
            return False