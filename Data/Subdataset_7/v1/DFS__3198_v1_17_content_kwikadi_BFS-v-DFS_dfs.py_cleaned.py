from collections import defaultdict
class class1:
    def fonk1(self, b2):
        self.b1 = defaultdict(list)
        self.b2 = b2
    def fonk2(self, u, b9):
        self.b1[u].append(b9)
    def fonk3(self, b5, g):
        b3 = [False] * self.b2
        b4 = [b5]
        b3[b5] = True
        while b4:
            b5 = b4.pop()
            print(b5, b6 = " ")
            if b5 = = g:
                print("Goal found.")
                return 0
            for i in self.b1[b5]:
                if not b3[i]:
                    b4.append(i)
                    b3[i] = True
        print("Search failed.")
        return 0
with open('input.txt', 'r') as inputFile:
    b2 = int(inputFile.readline())
    b7 = int(inputFile.readline())
    b8 = int(inputFile.readline())
    b1 = class1(b2)
    for line in inputFile.readlines():
        u, b9 = map(int, line.split())
        b1.fonk2(u, b9)
b1.fonk3(b7, b8)