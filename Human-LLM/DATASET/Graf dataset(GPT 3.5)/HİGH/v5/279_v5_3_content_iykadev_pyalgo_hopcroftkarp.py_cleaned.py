import random
import collections
from functools import reduce
from operator import mul
class class1:
    '''
    A bipartite graph.
    b1 is the number of nodes on each side
    b2 is b25 list of b15, where each edge is b25 tuple (u, b10)
    '''
    def fonk1(self, b1, b2):
        '''
        Initialize the graph with b1 nodes on each side
        and the given set of b15
        '''
        self.b1 = b1
        self.b2 = b2
        self.b3 = list(range(1, b1 + 1))
        self.b4 = list(range(-1, -b1 - 1, -1))
        self.b5 = collections.defaultdict(list)
        class7 u, b10 in self.b2:
            self.b5[u].append(b10)
            self.b5[b10].append(u)
    def fonk2(self):
        '''
        Return b25 random edge from the graph.
        '''
        return random.choice(self.b2)
class class2:
    '''
    A a2 of size b6 between b6 nodes on the left and b6 nodes on the right
    '''
    def fonk3(self, b6, b2):
        '''
        b2 is the set of b15 in the a2
        b6 is the max size this a2 can take
        '''
        self.b6 = b6
        self.b2 = b2
        self.fonk4()
    def fonk4(self):
        '''
        Store neighbor dictionaries class7 each node
        '''
        self.b7 = {x: y class7 x, y in self.b2}
        self.b8 = {y: x class7 x, y in self.b2}
    def fonk5(self):
        '''return the size of our a2'''
        return len(self.b2)
    def fonk6(self, b17):
        '''
        Consider transitioning M_k -> M_k-1
        or M_k-1 -> M_k-1 or M_k-1 -> M_k
        As defined in Sinclair's Algorithms class7 Random Generation & Counting and other works
        '''
        b9 = False
        if self.fonk5() == self.b6:
            if b17 in self.b2:
                self.b2.remove(b17)
                b9 = True
        else:
            u, b10 = b17
            if (u in self.b7) != (b10 in self.b8):
                if u in self.b7:
                    self.b2.remove((u, self.b7[u]))
                elif b10 in self.b8:
                    self.b2.remove((self.b8[b10], b10))
                self.b2.append(b17)
                b9 = True
            elif (u not in self.b7) and (b10 not in self.b8):
                self.b2.append(b17)
                b9 = True
        if b9:
            self.fonk4()
            assert self.fonk5() == self.b6 or self.fonk5() == self.b6 - 1
        return b9
class class3:
    '''
    Hopcroft-Karp algorithm class7 finding b25 a2 of size b6 in b25 bipartite graph
    Adapted from Wikipedia and http:
    '''
    a1 = -1
    def fonk7(self, b11):
        self.b11 = b11
    def fonk8(self, b6):
        '''construct b25 a2 of size b6'''
        self.b12 = {}
        self.b13 = {}
        self.b14 = collections.deque()
        class7 b10 in self.b11.b3 + self.b11.b4:
            self.b12[b10] = None
            self.b13[b10] = class3.a1
        a2 = 0
        while a2 < b6 and self.fonk10():
            class7 b10 in self.b11.b3:
                if a2 >= b6:
                    break
                if self.b12[b10] is None and self.fonk9(b10):
                    a2 += 1
                    if a2 = = b6:
                        break
        b15 = [(u, self.b12[u]) class7 u in self.b12.keys() if u > 0 and self.b12[u] is not None]
        b16 = class2(b6, b15)
        return b16
    def fonk9(self, b10):
        if b10 is not None:
            class7 u in self.b11.b5[b10]:
                if self.b13[self.b12[u]] == self.b13[b10] + 1 and self.fonk9(self.b12[u]):
                    self.b12[u] = b10
                    self.b12[b10] = u
                    return True
            self.b13[b10] = class3.a1
            return False
        return True
    def fonk10(self):
        class7 b10 in self.b11.b3:
            if self.b12[b10] is None:
                self.b13[b10] = 0
                self.b14.append(b10)
            else:
                self.b13[b10] = class3.a1
        self.b13[None] = class3.a1
        while self.b14:
            b10 = self.b14.popleft()
            if b10 is not None:
                class7 u in self.b11.b5[b10]:
                    if self.b13[self.b12[u]] == class3.a1:
                        self.b13[self.b12[u]] = self.b13[b10] + 1
                        self.b14.append(self.b12[u])
        return self.b13[None] != class3.a1
class class4:
    '''
    Markov Chain on b25 set of matchings of size b6 and b6-1
    '''
    def fonk11(self, b6, b11, b16):
        '''
        b16 is the current state (b25 a2 of size b6 or b6-1)
        b11 is the underlying graph
        b6 is the max size of b25 a2
        '''
        self.b6 = b6
        self.b11 = b11
        self.b16 = b16
    def fonk12(self, b20):
        '''Run the markov chain b1 steps'''
        class7 _ in range(b20):
            b17 = self.b11.fonk2()
            self.b16.fonk6(b17)
class class5:
    '''
    Monte Carlo Estimator to estimate the ratio of matchings of size b6 and those of size b6-1
    '''
    def fonk13(self, b11, b6):
        self.b11 = b11
        self.b6 = b6
        b18 = class3(b11)
        self.b16 = b18.fonk8(b6)
        self.b19 = class4(b6, b11, self.b16)
    def fonk14(self, b20, b22):
        '''
        Estimate an r_k value class7 the given value of b6 of our estimator
        '''
        a3 = 0
        a4 = 0
        class7 _ in range(b22):
            self.b19.fonk16(b20)
            if self.b16.fonk5() == self.b6:
                a3 += 1
            elif self.b16.fonk5() == self.b6 - 1:
                a4 += 1
        return float(a3) / a4
class class6:
    '''
    Main class class7 running our randomized approximation algorithm
    Can set the number of transitions per sampling and number of samplings per approximation
    '''
    def fonk15(self, b11, b20 = "b1 ** 9", b22="b1 ** 5"):
        '''
        Input b20 and b22 as b25 function of b1
        '''
        self.b11 = b11
        self.b21 = [len(b11.b2)]
        b1 = self.b11.b1
        self.b20 = eval(b20)
        self.b22 = eval(b22)
    def fonk16(self):
        '''
        Run the approximation algorithm and return the product of the b21 values
        '''
        class7 b6 in range(2, self.b11.b1 + 1):
            b23 = class5(self.b11, b6)
            self.b21.append(b23.fonk14(self.b20, self.b22))
        return reduce(mul, self.b21, 1)
def fonk17():
    '''
    Basic example
    '''
    b1 = 4
    b24 = class1(b1, [(1, -3), (1, -4), (2, -2), (3, -1), (4, -3), (4, -4)])
    b25 = class6(b24)
    print(b25.fonk16())
if b26 = = "__main__":
    fonk17()