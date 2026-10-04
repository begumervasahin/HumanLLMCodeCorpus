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
            else:
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
            else:
                for col in range(self.b1):
                    b6 = b4.copy()
                    b6.append((b5, col))
                    b7.put(b6)
        return b2
    def fonk4(self, queens):
        for i in range(len(queens)):
            for j in range(i):
                (row1, b8) = queens[i]
                (row2, col2) = queens[j]
                if b8 = = col2 or abs(row1 - row2) == abs(b8 - col2):
                    return True
        return False
    def fonk5(self, queens):
        b9 = [[" " for _ in range(self.b1)] for _ in range(self.b1)]
        for (b5, col) in queens:
            b9[b5][col] = "Q"
        for b5 in b9:
            print(" ---" * self.b1)
            print("| " + " | ".join(b5) + " |")
        print(" ---" * self.b1)
if b10 = = "__main__":
    a1 = 8
    b11 = class1(a1)
    print("Solving N-Queens using DFS:")
    b12 = b11.fonk2()
    print(f"Number of b2 found: {len(b12)}")
    for b4 in b12:
        b11.fonk5(b4)
        print()
    print("Solving N-Queens using BFS:")
    b13 = b11.fonk3()
    print(f"Number of b2 found: {len(b13)}")
    for b4 in b13:
        b11.fonk5(b4)
        print()