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
                b6 = (b5, col)
                b3.append(b4 + [b6])
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
                b6 = (b5, col)
                b7.put(b4 + [b6])
        return b2
    def fonk4(self, queens):
        for i in range(len(queens)):
            for j in range(i):
                if self.fonk5(queens[i], queens[j]):
                    return True
        return False
    def fonk5(self, queen1, queen2):
        b10, b8 = queen1
        row2, b9 = queen2
        return b10 = = row2 or b8 == b9 or abs(b10 - row2) == abs(b8 - b9)
    def fonk6(self, queens):
        for b5 in range(self.b1):
            print(' ---' * self.b1)
            for col in range(self.b1):
                if (b5, col) in queens:
                    print('| Q ', b11 = '')
                else:
                    print('|   ', b11 = '')
            print('|')
        print(' ---' * self.b1)
if b12 = = "__main__":
    a1 = 8
    b13 = class1(a1)
    b14 = b13.fonk2()
    b15 = b13.fonk3()
    print(f"Number of b2 using DFS: {len(b14)}")
    print(f"Number of b2 using BFS: {len(b15)}")
    if b14:
        print("One of the b2 using DFS:")
        b13.fonk6(b14[0])
    if b15:
        print("One of the b2 using BFS:")
        b13.fonk6(b15[0])