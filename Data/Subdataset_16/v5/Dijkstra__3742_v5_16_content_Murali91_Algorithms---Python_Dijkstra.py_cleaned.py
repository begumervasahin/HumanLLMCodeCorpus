import collections
class class1:
    def fonk1(self, *b1):
        self.b1 = list(b1)
        self.b2 = {node: float('inf') for node in self.b1}
        self.b3 = collections.defaultdict(dict)
    def fonk2(self, src, dest, cost):
        self.b3[src][dest] = cost
    def fonk3(self, node, neighbors):
        for neighbor, cost in neighbors.items():
            b4 = self.b2[node] + cost
            if b4 < self.b2[neighbor]:
                self.b2[neighbor] = b4
    def fonk4(self, source):
        self.b2[source] = 0
        b5 = set()
        while len(b5) < len(self.b1):
            b6 = min((node for node in self.b1 if node not in b5), key=lambda node: self.b2[node])
            b5.add(b6)
            if b6 in self.b3:
                self.fonk3(b6, self.b3[b6])
        return self.b2
def fonk5():
    b7 = class1('a', 'b', 'c', 'd', 'e')
    b7.fonk2('a', 'b', 1)
    b7.fonk2('a', 'c', 4)
    b7.fonk2('b', 'c', 2)
    b7.fonk2('b', 'd', 5)
    b7.fonk2('c', 'd', 1)
    b7.fonk2('d', 'e', 3)
    b8 = b7.fonk4('a')
    print("Shortest paths from node 'a':")
    for node, distance in b8.items():
        print(f"Distance to {node}: {distance}")
if b9 = = '__main__':
    fonk5()