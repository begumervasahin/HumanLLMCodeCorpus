from collections import defaultdict
class class1:
    def fonk1(self, b2):
        self.b1 = defaultdict(list)
        self.b2 = b2
    def fonk2(self, u, b9):
        self.b1[u].append(b9)
    def fonk3(self, b7, b8):
        b3 = [False] * self.b2
        b4 = [b7]
        b3[b7] = True
        while b4:
            b5 = b4.pop()
            print(b5, b6 = " ")
            if b5 = = b8:
                print("Goal found.")
                return True
            for neighbor in self.b1[b5]:
                if not b3[neighbor]:
                    b4.append(neighbor)
                    b3[neighbor] = True
        print("Search failed.")
        return False
with open('input.txt', 'r') as inputFile:
    b2 = int(inputFile.readline())
    b7 = int(inputFile.readline())
    b8 = int(inputFile.readline())
    b1 = class1(b2)
    for line in inputFile.readlines():
        u, b9 = map(int, line.split())
        b1.fonk2(u, b9)
b1.fonk3(b7, b8)