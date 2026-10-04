
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
        b7 = None
        b8 = None
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
        b9 = self.fonk7(self.b5, self.finish)
        if b9 is None:
            print("No b9 found")
            sys.exit(1)
        self.fonk4(b9)
        self.b3.save(self.b2)
    def fonk4(self, b13):
        for b14 in b13:
            x, b10 = b14
            self.b4[x, b10] = self.b1["RED"]
    def fonk5(self, x, b10):
        width, b6 = self.b3.size
        return 0 <= x < width and 0 <= b10 < b6
    def fonk6(self, position):
        x, b10 = position
        return [(x + 1, b10), (x, b10 + 1), (x - 1, b10), (x, b10 - 1)]
    def fonk7(self, b7, b8):
        b11 = [[b7]]
        b12 = set()
        while b11:
            b13 = b11.pop(0)
            b14 = b13[-1]
            b12.add(b14)
            if b14 = = b8:
                print("Solution found")
                return b13
            for neighbor in self.fonk6(b14):
                x, b10 = neighbor
                if (
                    (x, b10) not in b12
                    and self.fonk5(x, b10)
                    and (self.b4[x, b10] == self.b1["WHITE"] or self.b4[x, b10] == self.b1["RED"])
                ):
                    self.b4[x, b10] = self.b1["GREEN"]
                    b15 = b13 + [neighbor]
                    b11.append(b15)
        return None
if b16 = = '__main__':
    if len(sys.argv) == 3:
        b17 = class1(input_file=sys.argv[1], b2=sys.argv[2])
        b17.fonk3()
    else:
        print("Usage: python maze_solve.py <input_file.png> <b2.png>")
        sys.exit(1)