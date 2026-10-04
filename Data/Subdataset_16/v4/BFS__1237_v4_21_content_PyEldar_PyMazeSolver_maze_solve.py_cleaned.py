
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
        width, b6 = self.b3.size
        b7 = None
        b8 = None
        print(width, b6)
        for x in range(width):
            for b10 in range(b6):
                if self.b4[x, b10] == self.b1["RED"]:
                    b8 = (x, b10)
                elif self.b4[x, b10] == self.b1["GREEN"]:
                    b7 = (x, b10)
        if b7 and b8:
            return b8, b7
        print("No b7 or b8 found")
        sys.exit(1)
    def fonk3(self):
        b9 = self.fonk6(self.b5, self.finish)
        if b9 is None:
            print("No b9 found")
            sys.exit(1)
        for b16 in b9:
            x, b10 = b16
            self.b4[x, b10] = self.b1["RED"]
        self.b3.save(self.b2)
    def fonk4(self, x, b10):
        width, b6 = self.b3.size
        return 0 <= x < width and 0 <= b10 < b6
    def fonk5(self, position):
        x, b10 = position
        return [(x + 1, b10), (x, b10 + 1), (x - 1, b10), (x, b10 - 1)]
    def fonk6(self, b7, b8):
        b11 = self.b3.copy()
        b12 = b11.load()
        b13 = [[b7]]
        b14 = set()
        while b13:
            b15 = b13.pop(0)
            b16 = b15[-1]
            b14.add(b16)
            if b16 = = b8:
                for position in b15:
                    x, b10 = position
                    b12[x, b10] = self.b1["RED"]
                print("Solution found")
                return b15
            for neighbor in self.fonk5(b16):
                x, b10 = neighbor
                if (x, b10) not in b14 and self.fonk4(x, b10) and (b12[x, b10] == self.b1["WHITE"] or b12[x, b10] == self.b1["RED"]):
                    b12[x, b10] = self.b1["GREEN"]
                    b17 = list(b15)
                    b17.append((x, b10))
                    b13.append(b17)
        return None
if b18 = = '__main__':
    if len(sys.argv) == 3:
        b19 = class1(input_file=sys.argv[1], b2=sys.argv[2])
        b19.fonk3()
    else:
        print("Usage: python maze_solve.py <input_file.png> <b2.png>")
        sys.exit(1)