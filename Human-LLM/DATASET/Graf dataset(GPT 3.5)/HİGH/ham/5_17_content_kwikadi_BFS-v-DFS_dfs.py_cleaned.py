from collections import defaultdict
class class1:
    def fonk1(self, b2):
        self.b1 = defaultdict(list)
        self.b2 = b2
    def fonk2(self,u,v):
        self.b1[u].append(v)
    def fonk3(self, b5, b9):
        b3 = [False] * self.b2
        b4 = []
        b4.insert(0,b5)
        b3[b5] = True
        while b4:
            b5 = b4.pop(0)
            print (b5, b6 = " ")
            if b5 = = b9:
                print("Goal found.")
                return 0
            for i in self.b1[b5]:
                if b3[i] == False:
                    b4.insert(0,i)
                    b3[i] = True
        print("Search failed.")
        return 0
with open('input.txt', 'rb') as inputFile:
    b2 = int(inputFile.readline())
    b7 = int(inputFile.readline())
    b8 = int(inputFile.readline())
    b9 = class1(b2)
    for i in inputFile.readlines():
        b9.fonk2(int(i.split()[0]), int(i.split()[1]))
b9.fonk3(b7,b8)