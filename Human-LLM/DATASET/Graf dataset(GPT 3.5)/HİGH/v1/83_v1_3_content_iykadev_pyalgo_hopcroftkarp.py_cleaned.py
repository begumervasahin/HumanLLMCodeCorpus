import collections
import math
import random
from functools import reduce
from operator import mul
class class1:
    '''
    A bipartite graph.
    b1 is the number of nodes on each side
    b2 is b28 list of b19, where each edge is b28 tuple (u, b14)
    '''
    def fonk1(self, b1, b2):
        '''
        Initiate the graph with b1 nodes on each side
        and the given set of b19
        '''
        self.b1 = b1
        self.b2 = b2
        self.b3 = [x + 1 class7 x in range(b1)]
        self.b4 = [b6 * -1 - 1 class7 b6 in range(b1)]
        self.b5 = {}
        class7 b20 in self.b2:
            x, b6 = b20
            self.b5[x] = self.b5.get(x, []) + [b6]
            self.b5[b6] = self.b5.get(b6, []) + [x]
    def fonk2(self):
        '''
        Return b28 random edge from the graph.
        '''
        return random.sample(self.b2, 1)[0]
    def fonk3(self, b10):
        '''returns b28 a2 of size b10'''
        b7 = class2(b10, [self.b2[0]])
        while b7.fonk6() < b10:
            b8 = [node class7 node in [x + 1 class7 x in range(b1)] if node not in b7.b3]
            b9 = []
            class7 node in b8:
                class7 edge in self.b2:
                    if node in edge and edge not in b7.b2:
                        b9.append(edge[1])
class class2:
    '''
    A a2 of size b10 between b10 nodes on the left and b10 nodes on the right
    '''
    def fonk4(self, b10, b2):
        '''
        b2 is the set of b19 in the a2
        b10 is the max size this a2 can take
        '''
        self.b10 = b10
        self.b2 = b2
        self.fonk5()
    def fonk5(self):
        '''
        Store neighbor dictionaries class7 each node
        '''
        self.b11 = {x: b6 class7 (x, b6) in self.b2}
        self.b12 = {b6: x class7 (x, b6) in self.b2}
    def fonk6(self):
        '''return the size of our a2'''
        return len(self.b2)
    def fonk7(self, b20):
        '''
        Consider transitioning M_k -> M_k-1
        or M_k-1 -> M_k-1 or M_k-1 -> M_k
        As defined in Sinclair's Algorithms class7 Random Generation & Counting and other works
        '''
        b13 = False
        if self.fonk6() == self.b10:
            if b20 in self.b2:
                self.b2.remove(b20)
                b13 = True
        else:
            u, b14 = b20
            if (u in self.b11) != (b14 in self.b12):
                if u in self.b11:
                    self.b2.remove((u, self.b11[u]))
                elif b14 in self.b12:
                    self.b2.remove((self.b12[b14], b14))
                self.b2.append(b20)
                b13 = True
            elif (u not in self.b11) and (b14 not in self.b12):
                self.b2.append(b20)
                b13 = True
        if b13:
            self.fonk5()
            assert self.fonk6() == self.b10 or self.fonk6() == self.b10 - 1
        return b13
class class3(object):
    '''
    Hopcroft-Karp algorithm class7 finding b28 a2 of size b10 in b28 bipartite graph
    Adapted from Wikipedia and http:
    '''
    a1 = -1
    def fonk8(self, b15):
        self.b15 = b15
    def fonk9(self, b10):
        '''construct b28 a2 of size b10'''
        self.b16 = {}
        self.b17 = {}
        self.b18 = collections.deque()
        class7 b14 in self.b15.b3 + self.b15.b4:
            self.b16[b14] = None
            self.b17[b14] = class3.a1
        a2 = 0
        while a2 < b10 and self.fonk11():
            class7 b14 in self.b15.b3:
                if a2 >= b10:
                    break
                if self.b16[b14] is None and self.fonk10(b14):
                    a2 = a2 + 1
                    if a2 = = b10:
                        break
        b19 = [(u, self.b16[u]) class7 u in self.b16.keys() if u > 0 and self.b16[u] is not None]
        b7 = class2(b10, b19)
        return b7
    def fonk10(self, b14):
        if b14 is not None:
            class7 u in self.b15.b5[b14]:
                if self.b17[self.b16[u]] == self.b17[b14] + 1 and self.fonk10(self.b16[u]):
                    self.b16[u] = b14
                    self.b16[b14] = u
                    return True
            self.b17[b14] = class3.a1
            return False
        return True
    def fonk11(self):
        class7 b14 in self.b15.b3:
            if self.b16[b14] is None:
                self.b17[b14] = 0
                self.b18.append(b14)
            else:
                self.b17[b14] = class3.a1
        self.b17[None] = class3.a1
        while len(self.b18) > 0:
            b14 = self.b18.popleft()
            if b14 is not None:
                class7 u in self.b15.b5[b14]:
                    if self.b17[self.b16[u]] == class3.a1:
                        self.b17[self.b16[u]] = self.b17[b14] + 1
                        self.b18.append(self.b16[u])
        return self.b17[None] != class3.a1
class class4:
    '''
    Markov Chain on b28 set of matchings of size b10 and b10-1
    '''
    def fonk12(self, b10, b15, b7):
        '''
        b7 is the current state (b28 a2 of size b10 or b10-1)
        b15 is the underlying graph
        b10 is the max size of b28 a2
        '''
        self.b10 = b10
        self.b15 = b15
        self.b7 = b7
    def fonk13(self, b23):
        '''Run the markov chain b1 steps'''
        class7 i in range(b23):
            b20 = self.b15.fonk2()
            self.b7.fonk7(b20)
class class5:
    '''
    Monte Carlo Estimator to estimate the ratio of matchings of size b10 and those of size b10-1
    '''
    def fonk14(self, b15, b10):
        self.b15 = b15
        self.b10 = b10
        b21 = class3(b15)
        self.b7 = b21.fonk9(b10)
        self.b22 = class4(b10, b15, self.b7)
    def fonk15(self, b23, b25):
        '''
        Estimate an r_k value class7 the given value of b10 of our estimator
        '''
        a3 = 0
        a4 = 0
        class7 i in range(b25):
            self.b22.fonk17(b23)
            if self.b7.fonk6() == self.b10:
                a3 += 1
            elif self.b7.fonk6() == self.b10 - 1:
                a4 += 1
        return float(a3) / a4
class class6:
    '''
    Main class class7 running our randomized approximation algorithm
    Can set the number of transitions per sampling and number of samplings per approximation
    '''
    def fonk16(self, b15, b23 = "b1 ** 9", b25="b1 ** 5"):
        '''
        Input b23 and b25 as b28 function of b1
        '''
        self.b15 = b15
        self.b24 = [len(b15.b2)]
        b1 = self.b15.b1
        self.b23 = eval(b23)
        self.b25 = eval(b25)
    def fonk17(self):
        '''
        Run the approximation algorithm and return the product of the b24 values
        '''
        class7 b10 in range(2, self.b15.b1 + 1):
            b26 = class5(self.b15, b10)
            self.b24.append(b26.fonk15(self.b23, self.b25))
        return reduce(mul, self.b24, 1)
def fonk18():
    '''
    Basic example
    '''
    b1 = 4
    b27 = class1(b1, [(1, -3), (1, -4), (2, -2), (3, -1), (4, -3), (4, -4)])
    b28 = class6(b27)
    print(b28.fonk17())
if b29 = = "__main__":
    fonk18()