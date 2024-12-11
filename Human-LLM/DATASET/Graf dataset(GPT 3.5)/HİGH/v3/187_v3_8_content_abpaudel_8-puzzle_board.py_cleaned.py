import numpy as np
import heapq
class class1:
    def fonk1(self, b2, b1 = None, b3=None, b4=0):
        self.b1 = b1
        self.b2 = np.array(b2)
        self.b3 = b3
        self.b4 = b4
        self.b5 = self.fonk5()
        self.b6 = self.b4 + self.fonk6()
    def fonk2(self, other):
        if self.b6 != other.b6:
            return self.b6 < other.b6
        else:
            b7 = {'Up': 0, 'Down': 1, 'Left': 2, 'Right': 3}
            return b7[self.b3] < b7[other.b3]
    def fonk3(self):
        return (
            str(self.b2[:3]) + '\n' +
            str(self.b2[3:6]) + '\n' +
            str(self.b2[6:]) + ' ' +
            str(self.b4) + str(self.b3) + '\n'
        )
    def fonk4(self):
        return np.array_equal(self.b2, np.arange(9))
    def fonk5(self):
        return np.where(self.b2 = = 0)[0][0]
    def fonk6(self):
        b2 = self.fonk7(self.b2)
        b8 = self.fonk7(np.arange(9))
        return sum((abs(b2
    @staticmethod
    def fonk7(b2):
        b9 = np.array(range(9))
        for x, y in enumerate(b2):
            b9[y] = x
        return b9
    def fonk8(self, i, j):
        b10 = np.array(self.b2)
        b10[i], b10[j] = b10[j], b10[i]
        return b10
    def fonk9(self, direction):
        b11 = {'Up': -3, 'Down': 3, 'Left': -1, 'Right': 1}
        if direction in b11:
            b12 = self.b5 + b11[direction]
            if 0 <= b12 < 9:
                return class1(self.fonk8(self.b5, b12), self, direction, self.b4 + 1)
        return None
    def fonk10(self):
        b13 = ['Up', 'Down', 'Left', 'Right']
        return [self.fonk9(direction) for direction in b13]
    def fonk11(self):
        return self.fonk3()
def fonk12(b22):
    b14 = class1(b22)
    if b14.fonk4():
        return [b14]
    b15 = set()
    b16 = [b14]
    heapq.heapify(b16)
    while b16:
        b17 = heapq.heappop(b16)
        b15.add(tuple(b17.b2))
        for neighbor in b17.fonk10():
            if neighbor.fonk4():
                return fonk13(neighbor)
            if tuple(neighbor.b2) not in b15:
                heapq.heappush(b16, neighbor)
def fonk13(b19):
    b18 = []
    while b19:
        b18.append(b19)
        b19 = b19.b1
    return b18[::-1]
if b20 = = "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python main.py <b21> <b22>")
        sys.exit(1)
    b21 = sys.argv[1]
    b22 = list(map(int, sys.argv[2].split(',')))
    if b21 = = 'ast':
        b23 = fonk12(b22)
        if b23:
            with open("ast_output.txt", "w") as f:
                for b19 in b23:
                    f.write(str(b19))
                    f.write("\n")
        else:
            print("No solution found.")
    else:
        print("Invalid b21. Please choose 'ast'.")