import collections
class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, node):
        return self.b1.get(node, [])
    def fonk3(self):
        for node, neighbors in self.b1.items():
            print(f"{node}: {neighbors}")
class class2:
    def fonk4(self):
        self.b2 = collections.deque()
    def fonk5(self):
        return len(self.b2) == 0
    def fonk6(self, item):
        self.b2.append(item)
    def fonk7(self):
        return self.b2.popleft()
def fonk8(graph, start_node):
    b3 = class2()
    b3.fonk6(start_node)
    b4 = {start_node: True}
    while not b3.fonk5():
        b5 = b3.fonk7()
        print("Visiting node:", b5)
        for neighbor_node in graph.fonk2(b5):
            if neighbor_node not in b4:
                b3.fonk6(neighbor_node)
                b4[neighbor_node] = True
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