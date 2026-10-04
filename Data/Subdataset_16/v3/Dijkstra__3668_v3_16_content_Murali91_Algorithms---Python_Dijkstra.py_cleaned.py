import collections
class class1:
    def fonk1(self, *b1):
        self.b1 = list(b1)
        self.b2 = {node: float('inf') for node in self.b1}
        self.b3 = collections.defaultdict(dict)
    def fonk2(self, src, dest, cost):
        self.b3[src][dest] = cost
    def fonk3(self, source):
        self.b2[source] = 0
        b4 = set()
        b5 = [source]
        while b5:
            b6 = b5.pop(0)
            if b6 in b4:
                continue
            b4.add(b6)
            for neighbor, cost in self.b3[b6].items():
                b7 = self.b2[b6] + cost
                if b7 < self.b2[neighbor]:
                    self.b2[neighbor] = b7
                    b5.append(neighbor)
        return self.b2
def fonk4():
    b8 = class1('a', 'b', 'c', 'd', 'e')
    b8.fonk2('a', 'b', 1)
    b8.fonk2('a', 'c', 4)
    b8.fonk2('b', 'c', 2)
    b8.fonk2('b', 'd', 5)
    b8.fonk2('c', 'd', 1)
    b8.fonk2('d', 'e', 3)
    b9 = b8.fonk3('a')
    print("Shortest paths from node 'a':")
    for node, distance in b9.items():
        print(f"Distance to {node}: {distance}")
if b10 = = '__main__':
    fonk4()