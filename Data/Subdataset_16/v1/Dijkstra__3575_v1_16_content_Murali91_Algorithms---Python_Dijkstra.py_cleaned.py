import collections
class class1:
    def fonk1(self, *args):
        self.b1 = list(args)
        self.b2 = dict.fromkeys(self.b1, float('inf'))
        self.b3 = collections.defaultdict(dict)
    def fonk2(self, src, dest, dist):
        self.b3[src][dest] = dist
    def fonk3(self, index, item):
        b4 = float('inf')
        for key, value in item.items():
            b4 = min(b4, self.b2[index] + value)
            if self.b2[value] == float('inf') or self.b2[value] > self.b2[index] + value:
                self.b2[value] = self.b2[index] + value
    def fonk4(self, source):
        self.b2[source] = 0
        b5 = set()
        b6 = [source]
        while b6:
            b7 = b6.pop(0)
            if b7 in b5:
                continue
            b5.add(b7)
            if b7 in self.b3:
                for neighbor, dist in self.b3[b7].items():
                    if self.b2[neighbor] > self.b2[b7] + dist:
                        self.b2[neighbor] = self.b2[b7] + dist
                        b6.append(neighbor)
        print(self.b2)
if b8 = = '__main__':
    b9 = class1('a', 'b', 'c', 'd', 'e')
    b9.fonk2('a', 'b', 1)
    b9.fonk2('a', 'c', 4)
    b9.fonk2('b', 'c', 2)
    b9.fonk2('b', 'd', 5)
    b9.fonk2('c', 'd', 1)
    b9.fonk2('d', 'e', 3)
    b9.fonk4('a')