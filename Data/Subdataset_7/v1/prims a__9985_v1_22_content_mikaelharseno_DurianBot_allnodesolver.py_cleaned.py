import networkx as nx
import random
from heapq import heappop, heappush
from itertools import count
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = random.choice(list(b1.nodes()))
        self.a1 = 0
        self.b3 = {node: 0 for node in b1.nodes()}
    def fonk2(self):
        pass
    def fonk3(self):
        pass
    def fonk4(self, b9, b4):
        print(f"Bot moved from {b9} to {b4}")
        self.b3[b4] += 1
        if b4 = = self.b2:
            self.a1 += 1
def fonk5(b10):
    b10.fonk3()
    b10.fonk2()
    b5 = b10.b1
    b6 = nx.minimum_spanning_tree(b5)
    fonk6(b6, b10)
    print("Number of bots needed to be rescued:")
    print(b10.a1)
    print("Number of final rescued bots:")
    print(b10.b3[b10.b2])
    b10.fonk3()
def fonk6(b6, b10):
    b7 = list(b6.degree)
    while len(b7) > 1:
        a2 = 0
        b8 = len(b7)
        while a2 < b8:
            if b7[a2][1] == 1 and b7[a2][0] != b10.b2:
                break
            a2 += 1
        b9 = b7[a2][0]
        b4 = list(b6[b9].keys())[0]
        b10.fonk4(b9, b4)
        b6.remove_node(b9)
        b7 = list(b6.degree)
    return 1
b1 = nx.complete_graph(5)
b10 = class1(b1)
fonk5(b10)