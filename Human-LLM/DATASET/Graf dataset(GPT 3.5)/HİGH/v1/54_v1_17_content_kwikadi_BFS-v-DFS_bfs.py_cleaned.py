from collections import defaultdict
class class1:
    def fonk1(self, b2):
        self.b1 = defaultdict(list)
        self.b2 = b2
    def fonk2(self, u, b10):
        self.b1[u].append(b10)
    def fonk3(self, b5, b9):
        b3 = [False] * self.b2
        b4 = []
        b4.append(b5)
        b3[b5] = True
        while b4:
            b5 = b4.pop(0)
            print(b5, b6 = " ")
            if b5 = = b9:
                print("Goal found.")
                return 0
            for i in self.b1[b5]:
                if not b3[i]:
                    b4.append(i)
                    b3[i] = True
        print("Search failed.")
        return 0
def fonk4():
    with open('input.txt', 'r') as inputFile:
        b2 = int(inputFile.readline())
        b7 = int(inputFile.readline())
        b8 = int(inputFile.readline())
        b9 = class1(b2)
        for line in inputFile:
            u, b10 = map(int, line.split())
            b9.fonk2(u, b10)
    b9.fonk3(b7, b8)
if b11 = = "__main__":
    fonk4()