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
            for b10 in range(b6):
                b8 = self.b4[x, b10]
                if b8 = = self.b1["RED"]:
                    b7 = (x, b10)
                elif b8 = = self.b1["GREEN"]:
                    b5 = (x, b10)
        if b5 and b7:
            return b7, b5
        print("No b5 or b7 found")
        sys.exit(1)
    def fonk3(self):
        b9 = self.fonk6(self.b5, self.finish)
        if b9 is None:
            print("No b9 found")
            sys.exit(1)
        for b15 in b9:
            x, b10 = b15
            self.b4[x, b10] = self.b1["RED"]
        self.b3.save(self.b2)
        print("Solution saved to", self.b2)
    def fonk4(self, x, b10):
        width, b6 = self.b3.size
        return 0 <= x < width and 0 <= b10 < b6
    def fonk5(self, position):
        x, b10 = position
        return [(x + 1, b10), (x, b10 + 1), (x - 1, b10), (x, b10 - 1)]
    def fonk6(self, b5, b7):
        b3 = self.b3.copy()
        b11 = b3.load()
        b12 = [[b5]]
        b13 = set()
        while b12:
            b14 = b12.pop(0)
            b15 = b14[-1]
            b13.add(b15)
            if b15 = = b7:
                return b14
            for x, b10 in self.fonk5(b15):
                if (x, b10) not in b13 and self.fonk4(x, b10) \
                        and (b11[x, b10] == self.b1["WHITE"] or b11[x, b10] == self.b1["RED"]):
                    b11[x, b10] = self.b1["GREEN"]
                    b16 = list(b14)
                    b16.append((x, b10))
                    b12.append(b16)
        return None
if b17 = = '__main__':
    if len(sys.argv) == 3:
        b18 = class1(input_file=sys.argv[1], b2=sys.argv[2])
        b18.fonk3()
    else:
        print("Usage: python maze_solve.py <input_file.png> <b2.png>")
        sys.exit(1)