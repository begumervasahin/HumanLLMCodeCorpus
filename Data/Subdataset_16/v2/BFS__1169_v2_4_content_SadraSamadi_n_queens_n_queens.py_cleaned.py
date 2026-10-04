from b7 import Queue
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
                b6 = b4.copy()
                b6.append((b5, col))
                b3.append(b6)
        return b2
    def fonk3(self):
        if self.b1 < 1:
            return []
        b2 = []
        b7 = Queue()
        b7.put([])
        while not b7.empty():
            b4 = b7.get()
            if self.fonk4(b4):
                continue
            b5 = len(b4)
            if b5 = = self.b1:
                b2.append(b4)
                continue
            for col in range(self.b1):
                b6 = b4.copy()
                b6.append((b5, col))
                b7.put(b6)
        return b2
    def fonk4(self, b6):
        for i in range(1, len(b6)):
            for j in range(i):
                b10, b8 = b6[i]
                c, b9 = b6[j]
                if b10 = = c or b8 == b9 or abs(b10 - c) == abs(b8 - b9):
                    return True
        return False
    def fonk5(self, b6):
        for i in range(self.b1):
            print(' ---' * self.b1)
            for j in range(self.b1):
                b11 = 'Q' if (i, j) in b6 else ' '
                print(f'| {b11} ', b12 = '')
            print('|')
        print(' ---' * self.b1)
if b13 = = "__main__":
    a1 = 8
    b14 = class1(a1)
    print("Solving N-Queens using DFS:")
    b15 = b14.fonk2()
    print(f"Number of b2 found: {len(b15)}")
    for b4 in b15:
        b14.fonk5(b4)
        print()
    print("Solving N-Queens using BFS:")
    b16 = b14.fonk3()
    print(f"Number of b2 found: {len(b16)}")
    for b4 in b16:
        b14.fonk5(b4)
        print()