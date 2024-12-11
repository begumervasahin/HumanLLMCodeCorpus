import networkx as nx
import random
class class1:
    def fonk1(self):
        self.b1 = nx.Graph()
        self.a1 = 10
        self.a2 = 1
        self.a3 = 20
    def fonk2(self):
        print("Ending b7...")
    def fonk3(self):
        print("Starting b7...")
    def fonk4(self, node, a1):
        print(f"Scouting node {node} for a1: {a1}")
        return random.choice(a1)
    def fonk5(self, u, a3):
        print(f"Remoting from {u} to {a3}")
def fonk6(b7):
    b7.fonk2()
    b7.fonk3()
    b2 = b7.b1
    print(list(b2.edges))
    b3 = list(range(1, b7.a1 + 1))
    b4 = list(range(1, b7.a2)) + list(range(b7.a2 + 1, b7.a3 + 1))
    b5 = b7.fonk4(random.choice(b4), b3)
    print(b5)
    for _ in range(100):
        u, a3 = random.choice(list(b7.b1.edges()))
        b7.fonk5(u, a3)
    b7.fonk2()
if b6 = = "__main__":
    b7 = class1()
    fonk6(b7)