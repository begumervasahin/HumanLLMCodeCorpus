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
            for b11 in range(b6):
                b9 = self.b4[x, b11]
                if b9 = = self.b1["RED"]:
                    b8 = (x, b11)
                elif b9 = = self.b1["GREEN"]:
                    b7 = (x, b11)
        if b7 and b8:
            return b8, b7
        print("No b7 or b8 found")
        sys.exit(1)
    def fonk3(self):
        b10 = self.fonk6(self.b5, self.finish)
        if b10 is None:
            print("No b10 found")
            sys.exit(1)
        for b16 in b10:
            x, b11 = b16
            self.b4[x, b11] = self.b1["RED"]
        self.b3.save(self.b2)
        print("Solution saved to", self.b2)
    def fonk4(self, x, b11):
        width, b6 = self.b3.size
        return 0 <= x < width and 0 <= b11 < b6
    def fonk5(self, position):
        x, b11 = position
        return [(x + 1, b11), (x, b11 + 1), (x - 1, b11), (x, b11 - 1)]
    def fonk6(self, b7, b8):
        b3 = self.b3.copy()
        b12 = b3.load()
        b13 = [[b7]]
        b14 = set()
        while b13:
            b15 = b13.pop(0)
            b16 = b15[-1]
            b14.add(b16)
            if b16 = = b8:
                return b15
            for x, b11 in self.fonk5(b16):
                if (x, b11) not in b14 and self.fonk4(x, b11) \
                        and (b12[x, b11] == self.b1["WHITE"] or b12[x, b11] == self.b1["RED"]):
                    b12[x, b11] = self.b1["GREEN"]
                    b17 = list(b15)
                    b17.append((x, b11))
                    b13.append(b17)
        return None
if b18 = = '__main__':
    if len(sys.argv) == 3:
        b19 = class1(input_file=sys.argv[1], b2=sys.argv[2])
        b19.fonk3()
    else:
        print("Usage: python maze_solve.py <input_file.png> <b2.png>")
        sys.exit(1)