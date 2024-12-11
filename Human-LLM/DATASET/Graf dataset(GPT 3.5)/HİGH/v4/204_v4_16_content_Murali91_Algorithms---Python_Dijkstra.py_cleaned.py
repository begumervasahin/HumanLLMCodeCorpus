import collections
class class1:
    def fonk1(self, *b1):
        self.b1 = list(b1)
        self.b2 = dict.fromkeys(self.b1, 99999)
        self.b3 = collections.defaultdict(dict)
    def fonk2(self, src, dest, dist):
        if src not in self.b3:
            self.b3[src] = {}
        self.b3[src][dist] = dest
    def fonk3(self, index, item):
        a1 = 99999
        for b5, value in item.items():
            a1 = min(a1, b5)
            if self.b2[value] == 99999 or self.b2[value] > b5 + self.b2[index]:
                self.b2[value] = b5 + self.b2[index]
        self.b4 = item[a1]
    def fonk4(self, b4):
        self.b4 = b4
        if self.b4 in self.b3:
            self.b2[self.b4] = 0
            a2 = 0
            while a2 <= len(self.b3):
                for b5, value in self.b3.items():
                    if b5 = = self.b4 or self.b2[b5] != 99999:
                        self.fonk3(b5, value)
                a2 += 1
        print(self.b2)
if b6 = = '__main__':
    b7 = class1('A', 'B', 'C', 'D', 'E')
    b7.fonk2('A', 'B', 4)
    b7.fonk2('A', 'C', 2)
    b7.fonk2('B', 'C', 5)
    b7.fonk2('B', 'D', 10)
    b7.fonk2('C', 'D', 3)
    b7.fonk2('C', 'E', 7)
    b7.fonk2('D', 'E', 8)
    b7.fonk4('A')
