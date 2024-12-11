import networkx as nx
import random
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
    def fonk4(self, from_node, b4):
        print(f"Bot moved from {from_node} to {b4}")
        self.b3[b4] += 1
        if b4 = = self.b2:
            self.a1 += 1
def fonk5(b10):
    b10.fonk3()
    b10.fonk2()
    b5 = nx.minimum_spanning_tree(b10.b1)
    fonk6(b10, b5)
    print("Number of bots needing rescue:")
    print(b10.a1)
    print("Number of final rescued bots:")
    print(b10.b3[b10.b2])
    b10.fonk3()
def fonk6(b10, b5):
    b6 = list(b5.degree)
    while len(b6) > 1:
        a2 = 0
        b7 = len(b6)
        while a2 < b7:
            if b6[a2][1] == 1 and b6[a2][0] != b10.b2:
                break
            a2 += 1
        b8 = b6[a2][0]
        b9 = list(b5[b8].keys())[0]
        b10.fonk4(b8, b9)
        b5.remove_node(b8)
        b6 = list(b5.degree)
    return 1
b1 = nx.complete_graph(5)
b10 = class1(b1)
fonk5(b10)