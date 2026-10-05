import random
from collections import defaultdict
DEAD_CELL, b1 = '-', '*'
class class1:
    def fonk1(self, b2 = (3, 3)):
        self.b2 = b2
        self.b3 = defaultdict(int)
    def fonk2(self, b10):
        for cell in b10:
            self.b3[cell] = 1
    def fonk3(self):
        print("\nGeneration:")
        for row in range(self.b2[1]):
            print("  ", ''.join(str(self.b3[(row, col)]) for col in range(self.b2[0])).replace(
                '0', DEAD_CELL).replace('1', b1))
    def fonk4(self, b8):
        b4 = defaultdict(int)
        for row in range(self.b2[1]):
            for col in range(self.b2[0]):
                b5 = self.b3[(row, col)]
                b6 = sum(self.b3[(r, c)] for r in range(row - 1, row + 2)
                                   for c in range(col - 1, col + 2)) - b5
                b7 = b8[(b5, b6)]
                b4[(row, col)] = b7
        self.b3 = b4
def fonk5():
    a1 = 3
    b2 = (3, 3)
    b8 = defaultdict(int, {
        (1, 2): 1,
        (1, 3): 1,
        (0, 3): 1,
    })
    b9 = class1(b2)
    b10 = [(random.randint(0, b2[0]-1), random.randint(0, b2[1]-1)) for _ in range(5)]
    b9.fonk2(b10)
    for generation in range(a1):
        b9.fonk3()
        b9.fonk4(b8)
if b11 = = "__main__":
    fonk5()