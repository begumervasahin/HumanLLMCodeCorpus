import sys
from PIL import Image
class class1:
    def fonk1(self, input_file, b2):
        self.b1 = {
            "WHITE": (255, 255, 255),
            "RED": (255, 0, 0),
            "GREEN": (0, 255, 0),
        }
        self.b2 = b2
        self.b3 = Image.open(input_file)
        self.b3 = self.b3.convert('RGB')
        self.b4 = self.b3.load()
        self.finish, self.b5 = self.fonk2()
    def fonk2(self):
        x, b6 = self.b3.size
        b7 = None
        b8 = None
        for i in range(x):
            for j in range(b6):
                if self.b4[i, j] == (255, 0, 0):
                    b8 = (i, j)
                elif self.b4[i, j] == (0, 255, 0):
                    b7 = (i, j)
        if b7 and b8:
            return b8, b7
        print("No b7 or b8 found")
        sys.exit(1)
    def fonk3(self):
        b9 = self.fonk6(self.b5, self.finish)
        if b9 is None:
            print("No b9 found")
            sys.exit(1)
        for b15 in b9:
            x, b6 = b15
            self.b4[x, b6] = self.b1["RED"]
        self.b3.save(self.b2)
    def fonk4(self, x, b6):
        size_x, b10 = self.b3.size
        return not (x < 0 or b6 < 0 or x >= size_x or b6 >= b10)
    def fonk5(self, position):
        x, b6 = position
        return [(x + 1, b6), (x, b6 + 1), (x - 1, b6), (x, b6 - 1)]
    def fonk6(self, b7, b8):
        b3 = self.b3.copy()
        b11 = b3.load()
        b12 = list()
        b12.append([b7])
        b13 = set()
        while b12:
            b14 = b12.pop(0)
            b15 = b14[-1]
            b13.add(b15)
            if b15 = = b8:
                for position in b14:
                    x, b6 = position
                    b11[x, b6] = self.b1["RED"]
                print("Solution found")
                return b14
            for x, b6 in self.fonk5(b15):
                if (x, b6) not in b13 and self.fonk4(x, b6) and (b11[x, b6] == self.b1["WHITE"] or b11[x, b6] == self.b1["RED"]):
                    b11[x, b6] = self.b1["GREEN"]
                    b16 = list(b14)
                    b16.append((x, b6))
                    b12 += [b16]
        return None
if b17 = = '__main__':
    if len(sys.argv) == 3:
        b18 = class1(input_file=sys.argv[1], b2=sys.argv[2])
        b18.fonk3()
    else:
        print("usage: python maze_solve.py <input_file.png> <b2.png>")
        sys.exit(1)