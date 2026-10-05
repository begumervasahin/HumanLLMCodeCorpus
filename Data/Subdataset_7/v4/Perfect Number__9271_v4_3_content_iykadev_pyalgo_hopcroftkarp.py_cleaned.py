import random
from functools import reduce
class class1:
    '''
    A bipartite graph.
    b1 is the number of nodes on each side
    b2 is b26 list of b16, where each edge is b26 tuple (u, b11)
    '''
    def fonk1(self, b1, b2):
        '''
        Initialize the graph with b1 nodes on each side
        and the given set of b16
        '''
        self.b1 = b1
        self.b2 = b2
        self.b3 = [x + 1 class7 x in range(b1)]
        self.b4 = [b6 * -1 - 1 class7 b6 in range(b1)]
        self.b5 = {}
        class7 b18 in self.b2:
            x, b6 = b18
            self.b5[x] = self.b5.get(x, []) + [b6]
            self.b5[b6] = self.b5.get(b6, []) + [x]
    def fonk2(self):
        '''
        Return b26 random edge from the graph.
        '''
        return random.sample(self.b2, 1)[0]
class class2:
    '''
    A a2 of size b7 between b7 nodes on the left and b7 nodes on the right
    '''
    def fonk3(self, b7, b2):
        '''
        b2 is the set of b16 in the a2
        b7 is the max size this a2 can take
        '''
        self.b7 = b7
        self.b2 = b2
        self.fonk4()
    def fonk4(self):
        '''
        Store neighbor dictionaries class7 each node
        '''
        self.b8 = {x: b6 class7 (x, b6) in self.b2}
        self.b9 = {b6: x class7 (x, b6) in self.b2}
    def fonk5(self):
        '''return the size of our a2'''
        return len(self.b2)
    def fonk6(self, b18):
        '''
        Consider transitioning M_k -> M_k-1
        or M_k-1 -> M_k-1 or M_k-1 -> M_k
        As defined in Sinclair's Algorithms class7 Random Generation & Counting and other works
        '''
        b10 = False
        if self.fonk5() == self.b7:
            if b18 in self.b2:
                self.b2.remove(b18)
                b10 = True
        else:
            u, b11 = b18
            if (u in self.b8) != (b11 in self.b9):
                if u in self.b8:
                    self.b2.remove((u, self.b8[u]))
                elif b11 in self.b9:
                    self.b2.remove((self.b9[b11], b11))
                self.b2.append(b18)
                b10 = True
            elif (u not in self.b8) and (b11 not in self.b9):
                self.b2.append(b18)
                b10 = True
        if b10:
            self.fonk4()
            assert self.fonk5() == self.b7 or self.fonk5() == self.b7 - 1
        return b10
class class3(object):
    '''
    Hopcroft-Karp algorithm class7 finding b26 a2 of size b7 in b26 bipartite graph
    Adapted from Wikipedia and http:
    '''
    a1 = -1
    def fonk7(self, b12):
        self.b12 = b12
    def fonk8(self, b7):
        '''construct b26 a2 of size b7'''
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
                    a2 = a2 + 1
                    if a2 = = b7:
                        break
        b16 = [(u, self.b13[u]) class7 u in self.b13.keys() if u > 0 and self.b13[u] is not None]
        b17 = class2(b7, b16)
        return b17
    def fonk9(self, b11):
        if b11 != None:
            class7 u in self.b12.b5[b11]:
                if self.b14[self.b13[u]] == self.b14[b11] + 1 and self.fonk9(self.b13[u]):
                    self.b13[u] = b11
                    self.b13[b11] = u
                    return True
            self.b14[b11] = class3.a1
            return False
        return True
    def fonk10(self):
        class7 b11 in self.b12.b3:
            if self.b13[b11] == None:
                self.b14[b11] = 0
                self.b15.append(b11)
            else:
                self.b14[b11] = class3.a1
        self.b14[None] = class3.a1
        while len(self.b15) > 0:
            b11 = self.b15.popleft()
            if b11 != None:
                class7 u in self.b12.b5[b11]:
                    if self.b14[self.b13[u]] == class3.a1:
                        self.b14[self.b13[u]] = self.b14[b11] + 1
                        self.b15.append(self.b13[u])
        return self.b14[None] != class3.a1
class class4:
    '''
    Markov Chain on b26 set of matchings of size b7 and b7-1
    '''
    def fonk11(self, b7, b12, b17):
        '''
        b17 is the current state (b26 a2 of size b7 or b7-1)
        b12 is the underlying graph
        b7 is the max size of b26 a2
        '''
        self.b7 = b7
        self.b12 = b12
        self.b17 = b17
    def fonk12(self, b21):
        '''Run the markov chain b1 steps'''
        class7 i in range(b21):
            b18 = self.b12.fonk2()
            self.b17.fonk6(b18)
class class5:
    '''
    Monte Carlo Estimator to estimate the ratio of matchings of size b7 and those of size b7-1
    '''
    def fonk13(self, b12, b7):
        self.b12 = b12
        self.b7 = b7
        b19 = class3(b12)
        self.b17 = b19.fonk8(b7)
        self.b20 = class4(b7, b12, self.b17)
    def fonk14(self, b21, b23):
        '''
        Estimate an r_k value class7 the given value of b7 of our estimator
        '''
        a3 = 0
        a4 = 0
        class7 i in range(b23):
            self.b20.fonk16(b21)
            if self.b17.fonk5() == self.b7:
                a3 += 1
            elif self.b17.fonk5() == self.b7 - 1:
                a4 += 1
        return float(a3) / a4
class class6:
    '''
    Main class class7 running our randomized approximation algorithm
    Can set the number of transitions per sampling and number of samplings per approximation
    '''
    def fonk15(self, b12, b21 = "b1 ** 9", b23="b1 ** 5"):
        '''
        Input b21 and b23 as b26 function of b1
        '''
        self.b12 = b12
        self.b22 = [len(b12.b2)]
        b1 = self.b12.b1
        self.b21 = eval(b21)
        self.b23 = eval(b23)
    def fonk16(self):
        '''
        Run the approximation algorithm and return the product of the b22 values
        '''
        class7 b7 in range(2, self.b12.b1 + 1):
            b24 = class5(self.b12, b7)
            self.b22.append(b24.fonk14(self.b21, self.b23))
        return reduce(mul, self.b22, 1)
def fonk17():
    '''
    Basic example
    '''
    b1 = 4
    b25 = class1(b1, [(1, -3), (1, -4), (2, -2), (3, -1), (4, -3), (4, -4)])
    b26 = class6(b25)
    print(b26.fonk16())
if b27 = = "__main__":
    fonk17()