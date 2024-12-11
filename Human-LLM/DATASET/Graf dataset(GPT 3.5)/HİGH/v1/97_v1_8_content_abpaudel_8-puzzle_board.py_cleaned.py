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
        return str(self.b2[:3]) + '\n' + str(self.b2[3:6]) + '\n' + str(self.b2[6:]) + ' ' + str(
            self.b4) + str(self.b3) + '\n'
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
    def fonk9(self):
        if self.b5 > 2:
            return class1(self.fonk8(self.b5, self.b5 - 3), self, 'Up', self.b4 + 1)
    def fonk10(self):
        if self.b5 < 6:
            return class1(self.fonk8(self.b5, self.b5 + 3), self, 'Down', self.b4 + 1)
    def fonk11(self):
        if self.b5 % 3 != 0:
            return class1(self.fonk8(self.b5, self.b5 - 1), self, 'Left', self.b4 + 1)
    def fonk12(self):
        if (self.b5 + 1) % 3 != 0:
            return class1(self.fonk8(self.b5, self.b5 + 1), self, 'Right', self.b4 + 1)
    def fonk13(self):
        b11 = [self.fonk9(), self.fonk10(), self.fonk11(), self.fonk12()]
        return [neighbor for neighbor in b11 if neighbor]
    b12 = __str__
def fonk14(b21):
    b13 = class1(b21)
    if b13.fonk4():
        return [b13]
    b14 = set()
    b15 = [b13]
    heapq.heapify(b15)
    while b15:
        b16 = heapq.heappop(b15)
        b14.add(tuple(b16.b2))
        for neighbor in b16.fonk13():
            if neighbor.fonk4():
                return fonk15(neighbor)
            if tuple(neighbor.b2) not in b14:
                heapq.heappush(b15, neighbor)
def fonk15(b18):
    b17 = []
    while b18:
        b17.append(b18)
        b18 = b18.b1
    return b17[::-1]
if b19 = = "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python main.py <b20> <b21>")
        sys.exit(1)
    b20 = sys.argv[1]
    b21 = list(map(int, sys.argv[2].split(',')))
    if b20 = = 'ast':
        b22 = fonk14(b21)
        if b22:
            with open("ast_output.txt", "w") as f:
                for b18 in b22:
                    f.write(str(b18))
                    f.write("\n")
        else:
            print("No solution found.")
    else:
        print("Invalid b20. Please choose 'ast'.")