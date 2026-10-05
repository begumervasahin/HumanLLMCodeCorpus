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
        self.b3 = Image.open(input_file).convert('RGB')
        self.b4 = self.b3.load()
        self.finish, self.b5 = self.fonk2()
    def fonk2(self):
        width, b6 = self.b3.size
        b5 = None
        b7 = None
        for x in range(width):
            for b9 in range(b6):
                if self.b4[x, b9] == self.b1["RED"]:
                    b7 = (x, b9)
                elif self.b4[x, b9] == self.b1["GREEN"]:
                    b5 = (x, b9)
        if b5 and b7:
            return b7, b5
        print("No b5 or b7 found")
        sys.exit(1)
    def fonk3(self):
        b8 = self.fonk6(self.b5, self.finish)
        if b8 is None:
            print("No b8 found")
            sys.exit(1)
        for b14 in b8:
            x, b9 = b14
            self.b4[x, b9] = self.b1["RED"]
        self.b3.save(self.b2)
        print("Solution saved to", self.b2)
    def fonk4(self, x, b9):
        width, b6 = self.b3.size
        return 0 <= x < width and 0 <= b9 < b6
    def fonk5(self, position):
        x, b9 = position
        return [(x + 1, b9), (x, b9 + 1), (x - 1, b9), (x, b9 - 1)]
    def fonk6(self, b5, b7):
        b3 = self.b3.copy()
        b10 = b3.load()
        b11 = [[b5]]
        b12 = set()
        while b11:
            b13 = b11.pop(0)
            b14 = b13[-1]
            b12.add(b14)
            if b14 = = b7:
                return b13
            for x, b9 in self.fonk5(b14):
                if (x, b9) not in b12 and self.fonk4(x, b9) \
                        and (b10[x, b9] == self.b1["WHITE"] or b10[x, b9] == self.b1["RED"]):
                    b10[x, b9] = self.b1["GREEN"]
                    b15 = list(b13)
                    b15.append((x, b9))
                    b11.append(b15)
        return None
if b16 = = '__main__':
    if len(sys.argv) == 3:
        b17 = class1(input_file=sys.argv[1], b2=sys.argv[2])
        b17.fonk3()
    else:
        print("Usage: python maze_solve.py <input_file.png> <b2.png>")
        sys.exit(1)