from b8 import Queue
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        if self.b1 < 1:
            return []
        b2 = []
        b3 = [[]]
        while b3:
            b4 = b3.pop()
            if self.fonk4(b4):
                continue
            b5 = len(b4)
            if b5 = = self.b1:
                b2.append(b4)
                continue
            for col in range(self.b1):
                b6 = (b5, col)
                b7 = b4.copy()
                b7.append(b6)
                b3.append(b7)
        return b2
    def fonk3(self):
        if self.b1 < 1:
            return []
        b2 = []
        b8 = Queue()
        b8.put([])
        while not b8.empty():
            b4 = b8.get()
            if self.fonk4(b4):
                continue
            b5 = len(b4)
            if b5 = = self.b1:
                b2.append(b4)
                continue
            for col in range(self.b1):
                b6 = (b5, col)
                b7 = b4.copy()
                b7.append(b6)
                b8.put(b7)
        return b2
    def fonk4(self, b7):
        for i in range(1, len(b7)):
            for j in range(i):
                b11, b9 = b7[i]
                c, b10 = b7[j]
                if b11 = = c or b9 == b10 or abs(b11 - c) == abs(b9 - b10):
                    return True
        return False
    def fonk5(self, b7):
        for i in range(self.b1):
            print(' ---' * self.b1)
            for j in range(self.b1):
                b12 = 'Q' if (i, j) in b7 else ' '
                print('| %s ' % b12, b13 = '')
            print('|')
        print(' ---' * self.b1)
if b14 = = "__main__":
    a1 = 8
    b15 = class1(a1)
    b16 = b15.fonk2()
    b17 = b15.fonk3()
    print(f"Number of b2 using DFS: {len(b16)}")
    print(f"Number of b2 using BFS: {len(b17)}")
    if b16:
        print("One of the b2 using DFS:")
        b15.fonk5(b16[0])
    if b17:
        print("One of the b2 using BFS:")
        b15.fonk5(b17[0])