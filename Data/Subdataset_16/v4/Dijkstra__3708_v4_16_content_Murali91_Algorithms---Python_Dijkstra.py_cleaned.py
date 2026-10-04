import collections
class class1:
    def fonk1(self, *b1):
        self.b1 = list(b1)
        self.b2 = {node: float('inf') for node in self.b1}
        self.b3 = collections.defaultdict(dict)
    def fonk2(self, src, dest, cost):
        if src not in self.b3:
            self.b3[src] = {}
        self.b3[src][dest] = cost
    def fonk3(self, node, neighbors):
        b4 = float('inf')
        for neighbor, cost in neighbors.items():
            b4 = min(b4, cost)
            if self.b2[neighbor] == float('inf') or self.b2[neighbor] > self.b2[node] + cost:
                self.b2[neighbor] = self.b2[node] + cost
        self.b5 = next((n for n, c in neighbors.items() if c == b4), None)
    def fonk4(self, source):
        self.b2[source] = 0
        self.b5 = source
        b6 = set()
        while self.b5 and self.b5 not in b6:
            b6.add(self.b5)
            if self.b5 in self.b3:
                self.fonk3(self.b5, self.b3[self.b5])
        return self.b2
if b7 = = '__main__':
    b8 = class1('a', 'b', 'c', 'd', 'e')
    b8.fonk2('a', 'b', 1)
    b8.fonk2('a', 'c', 4)
    b8.fonk2('b', 'c', 2)
    b8.fonk2('b', 'd', 5)
    b8.fonk2('c', 'd', 1)
    b8.fonk2('d', 'e', 3)
    b9 = b8.fonk4('a')
    print("Shortest paths from node 'a':")
    for node, distance in b9.items():
        print(f"Distance to {node}: {distance}")