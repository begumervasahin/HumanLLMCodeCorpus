class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, id):
        return self.b1[id]
    def fonk3(self):
        for key, item in self.b1.items():
            print(key, item)
b2 = class1()
b2.b1 = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}
import collections
class class2:
    def fonk4(self):
        self.b3 = collections.deque()
    def fonk5(self):
        return len(self.b3) == 0
    def fonk6(self, x):
        self.b3.append(x)
    def fonk7(self):
        return self.b3.pop()
def fonk8(graph, start):
    b4 = class2()
    b4.fonk6(start)
    b5 = {}
    b5[start] = True
    while not b4.fonk5():
        b6 = b4.fonk7()
        print("Visiting %r" % b6)
        for next in graph.fonk2(b6):
            if next not in b5:
                b4.fonk6(next)
                b5[next] = True
fonk8(b2, 'A')