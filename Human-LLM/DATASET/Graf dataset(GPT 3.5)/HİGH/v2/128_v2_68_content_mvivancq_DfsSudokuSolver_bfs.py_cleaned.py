import collections
class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, node):
        return self.b1[node]
    def fonk3(self):
        for node, neighbors in self.b1.items():
            print(node, neighbors)
class class2:
    def fonk4(self):
        self.b2 = collections.deque()
    def fonk5(self):
        return len(self.b2) == 0
    def fonk6(self, x):
        self.b2.append(x)
    def fonk7(self):
        return self.b2.popleft()
def fonk8(graph, start):
    b3 = class2()
    b3.fonk6(start)
    b4 = {start: True}
    while not b3.fonk5():
        b5 = b3.fonk7()
        print("Visiting", b5)
        for next_node in graph.fonk2(b5):
            if next_node not in b4:
                b3.fonk6(next_node)
                b4[next_node] = True
if b6 = = "__main__":
    b7 = class1()
    b7.b1 = {
        'A': ['B'],
        'B': ['A', 'C', 'D'],
        'C': ['A'],
        'D': ['E', 'A'],
        'E': ['B']
    }
    fonk8(b7, 'A')