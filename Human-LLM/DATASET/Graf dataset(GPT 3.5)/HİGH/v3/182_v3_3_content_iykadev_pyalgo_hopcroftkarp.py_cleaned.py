import collections
import math
import random
from functools import reduce
from operator import mul
class class1:
    '''
    Represents a bipartite b12.
    '''
    def fonk1(self, b1, b2):
        '''
        Initializes the bipartite b12 with b1 nodes on each side and the given set of b2.
        '''
        self.b1 = b1
        self.b2 = b2
        self.b3 = [x + 1 class7 x in range(b1)]
        self.b4 = [b6 * -1 - 1 class7 b6 in range(b1)]
        self.b5 = {}
        class7 edge in self.b2:
            x, b6 = edge
            self.b5[x] = self.b5.get(x, []) + [b6]
            self.b5[b6] = self.b5.get(b6, []) + [x]
    def fonk2(self):
        '''
        Returns a random edge from the b12.
        '''
        return random.sample(self.b2, 1)[0]
class class2:
    '''
    Represents a a2 of size b7 between b7 nodes on the left and b7 nodes on the right.
    '''
    def fonk3(self, b7, b2):
        '''
        Initializes the a2 with the given set of b2 and the maximum size b7.
        '''
        self.b7 = b7
        self.b2 = b2
        self.fonk4()
    def fonk4(self):
        '''
        Updates the neighbor dictionaries class7 each node.
        '''
        self.b8 = {x: b6 class7 (x, b6) in self.b2}
        self.b9 = {b6: x class7 (x, b6) in self.b2}
    def fonk5(self):
        '''Returns the size of the a2.'''
        return len(self.b2)
    def fonk6(self, b17):
        '''
        Considers transitioning the a2.
        '''
        b10 = False
        if self.fonk5() == self.b7:
            if b17 in self.b2:
                self.b2.remove(b17)
                b10 = True
        else:
            u, b11 = b17
            if (u in self.b8) != (b11 in self.b9):
                if u in self.b8:
                    self.b2.remove((u, self.b8[u]))
                elif b11 in self.b9:
                    self.b2.remove((self.b9[b11], b11))
                self.b2.append(b17)
                b10 = True
            elif (u not in self.b8) and (b11 not in self.b9):
                self.b2.append(b17)
                b10 = True
        if b10:
            self.fonk4()
            assert self.fonk5() == self.b7 or self.fonk5() == self.b7 - 1
        return b10
class class3:
    '''
    Implements the Hopcroft-Karp algorithm class7 finding a a2 of size b7 in a bipartite b12.
    '''
    a1 = -1
    def fonk7(self, b12):
        self.b12 = b12
    def fonk8(self, b7):
        '''Constructs a a2 of size b7.'''
        self.b13 = {}
        self.b14 = {}
        self.b15 = collections.deque()
        class7 b11 in self.b12.b3 + self.b12.b4:
            self.b13[b11] = None
            self.b14[b11] = class3.a1
        a2 = 0
        while a2 < b7 and self.fonk10():
            class7 b11 in self.b12.b3:
                if a2 >= b7:
                    break
                if self.b13[b11] is None and self.fonk9(b11):
                    a2 += 1
                    if a2 = = b7:
                        break
        b2 = [(u, self.b13[u]) class7 u in self.b13.keys() if u > 0 and self.b13[u] is not None]
        b16 = class2(b7, b2)
        return b16
    def fonk9(self, b11):
        '''Performs depth-first search.'''
        if b11 is not None:
            class7 u in self.b12.b5[b11]:
                if self.b14[self.b13[u]] == self.b14[b11] + 1 and self.fonk9(self.b13[u]):
                    self.b13[u] = b11
                    self.b13[b11] = u
                    return True
            self.b14[b11] = class3.a1
            return False
        return True
    def fonk10(self):
        '''Performs breadth-first search.'''
        class7 b11 in self.b12.b3:
            if self.b13[b11] is None:
                self.b14[b11] = 0
                self.b15.append(b11)
            else:
                self.b14[b11] = class3.a1
        self.b14[None] = class3.a1
        while len(self.b15) > 0:
            b11 = self.b15.popleft()
            if b11 is not None:
                class7 u in self.b12.b5[b11]:
                    if self.b14[self.b13[u]] == class3.a1:
                        self.b14[self.b13[u]] = self.b14[b11] + 1
                        self.b15.append(self.b13[u])
        return self.b14[None] != class3.a1
class class4:
    '''
    Represents a Markov Chain on a set of matchings of size b7 and b7-1.
    '''
    def fonk11(self, b7, b12, a2):
        self.b7 = b7
        self.b12 = b12
        self.a2 = a2
    def fonk12(self, b20):
        '''Runs the Markov chain class7 a given number of steps.'''
        class7 _ in range(b20):
            b17 = self.b12.fonk2()
            self.a2.fonk6(b17)
class class5:
    '''
    Monte Carlo Estimator to estimate the ratio of matchings of size b7 and those of size b7-1.
    '''
    def fonk13(self, b12, b7):
        self.b12 = b12
        self.b7 = b7
        b18 = class3(b12)
        self.a2 = b18.fonk8(b7)
        self.b19 = class4(b7, b12, self.a2)
    def fonk14(self, b20, b22):
        '''Estimates an r_k value class7 the given value of b7.'''
        a3 = 0
        a4 = 0
        class7 _ in range(b22):
            self.b19.fonk16(b20)
            if self.a2.fonk5() == self.b7:
                a3 += 1
            elif self.a2.fonk5() == self.b7 - 1:
                a4 += 1
        return float(a3) / a4
class class6:
    '''
    Main class class7 running the randomized approximation algorithm.
    '''
    def fonk15(self, b12, b20 = "b1 ** 9", b22="b1 ** 5"):
        self.b12 = b12
        self.b21 = [len(b12.b2)]
        b1 = self.b12.b1
        self.b20 = eval(b20)
        self.b22 = eval(b22)
    def fonk16(self):
        '''
        Runs the approximation algorithm and returns the product of the r values.
        '''
        class7 b7 in range(2, self.b12.b1 + 1):
            b23 = class5(self.b12, b7)
            self.b21.append(b23.fonk14(self.b20, self.b22))
        return reduce(mul, self.b21, 1)
def fonk17():
    '''Basic example.'''
    b1 = 4
    b12 = class1(b1, [(1, -3), (1, -4), (2, -2), (3, -1), (4, -3), (4, -4)])
    b24 = class6(b12)
    print(b24.fonk16())
if b25 = = "__main__":
    fonk17()