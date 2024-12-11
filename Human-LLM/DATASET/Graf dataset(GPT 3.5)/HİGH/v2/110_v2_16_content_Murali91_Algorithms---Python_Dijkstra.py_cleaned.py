import collections
class class1:
    def fonk1(self, *b1):
        self.b1 = list(b1)
        self.b2 = {node: float('inf') for node in self.b1}
        self.b3 = collections.defaultdict(dict)
    def fonk2(self, src, dest, dist):
        if src not in self.b3:
            self.b3[src] = {}
        self.b3[src][dist] = dest
    def fonk3(self, index, item):
        b4 = float('inf')
        for b6, value in item.items():
            b4 = min(b4, b6)
            if self.b2[value] == float('inf') or self.b2[value] > b6 + self.b2[index]:
                self.b2[value] = b6 + self.b2[index]
        self.b5 = item[b4]
    def fonk4(self, b5):
        self.b5 = b5
        if self.b5 in self.b3:
            self.b2[self.b5] = 0
            a1 = 0
            while a1 <= len(self.b3):
                for b6, value in self.b3.items():
                    if b6 = = self.b5 or self.b2[b6] != float('inf'):
                        self.fonk3(b6, value)
                a1 += 1
        print(self.b2)
if b7 = = '__main__':
    b8 = class1('A', 'B', 'C', 'D', 'E')
    b8.fonk2('A', 'B', 4)
    b8.fonk2('A', 'C', 2)
    b8.fonk2('B', 'C', 5)
    b8.fonk2('B', 'D', 10)
    b8.fonk2('C', 'D', 3)
    b8.fonk2('C', 'E', 7)
    b8.fonk2('D', 'E', 8)
    b8.fonk4('A')
