
from PIL import Image, ImageDraw
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
class class2:
    def fonk2(self, b4, b5):
        self.b4 = b4
        self.b5 = b5
        self.b6 = None
        self.b7 = None
        self.b8 = None
        self.b9 = None
        self.b10 = []
def fonk3(filename):
    with open(filename, 'r') as file:
        b11 = file.read().strip().split('\n')
    b12 = []
    for i, line in enumerate(b11):
        b13 = []
        for j, b15 in enumerate(line):
            b14 = class2(class1(j, len(b11) - i - 1, b15), fonk9(b15))
            b13.append(b14)
            if b15 = = 'A':
                b16 = (j, len(b11) - i - 1)
            elif b15 = = 'B':
                b17 = (j, len(b11) - i - 1)
        b12.append(b13)
    b12.reverse()
    return b16, b17, b12
def fonk4(s1, s2):
    return abs(s2.b1 - s1.b1) + abs(s2.b2 - s1.b2)
def fonk5(s1, sf):
    return s1.b1 = = sf.b1 and s1.b2 == sf.b2
def fonk6(s, b12):
    b18 = []
    if s.b1 > 0:
        b18.append(b12[s.b2][s.b1-1])
    if s.b1 < (len(b12[s.b2]) - 1):
        b18.append(b12[s.b2][s.b1+1])
    if s.b2 > 0:
        b18.append(b12[s.b2-1][s.b1])
    if s.b2 < (len(b12) - 1):
        b18.append(b12[s.b2+1][s.b1])
    return b18
def fonk7(C, P, sf):
    C.b9 = P
    C.b6 = P.b6 + C.b5
    C.b7 = fonk4(C.b4, sf)
    C.b8 = C.b6 + C.b7
def fonk8(P):
    for b24 in P.b10:
        if P.b6 + b24.b5 < b24.b6:
            b24.b9 = P
            b24.b6 = P.b6 + b24.b5
            b24.b8 = b24.b6 + b24.b7
            fonk8(b24)
def fonk9(b3):
    return {
        'w': 100,
        'm': 50,
        'b8': 10,
        'b6': 5,
        'r': 1,
    }.get(b3, 1)
def fonk10(n):
    return {
        'w': (73, 216, 245),
        'm': (99, 99, 99),
        'b8': (3, 82, 0),
        'b6': (50, 200, 50),
        'r': (114, 80, 41),
        'A': (90, 180, 90),
        'B': (255, 90, 90),
    }[n.b4.b3]
def fonk11(b28, b29, b12, name):
    b19 = b29
    b20 = [b29]
    while b19 != b28:
        b19 = b19.b9
        b20.append(b19)
    b12.reverse()
    fonk12(b12, b20, name)
    for b19 in b20[1:-1]:
        b19.b4.b3 = 'O'
    b21 = '\n'.join(''.join(e.b4.b3 for e in line) for line in b12)
    print(b21)
def fonk12(b12, b20, name):
    b22 = Image.new('RGB', (len(b12[0]) * 20, len(b12) * 20), "white")
    b23 = ImageDraw.Draw(b22)
    for b2, row in enumerate(b12):
        for b1, b14 in enumerate(row):
            b24 = fonk10(b14)
            b23.rectangle([(b1 * 20, b2 * 20), (b1 * 20 + 20, b2 * 20 + 20)], b25 = b24, outline=(0, 0, 0))
            if b14 in b20:
                b23.rectangle([(b1 * 20 + 6, b2 * 20 + 6), (b1 * 20 + 14, b2 * 20 + 14)], b25 = (107, 97, 255), outline=(0, 0, 0))
    b22.save(b8"assignment3_images/part2_{name}.png", "PNG")
def fonk13(b16, b17, b12, name):
    b26 = []
    b27 = []
    b28 = b12[b16[1]][b16[0]]
    b29 = b12[b17[1]][b17[0]]
    b28.b6 = 0
    b28.b7 = fonk4(b28.b4, b29.b4)
    b28.b8 = b28.b6 + b28.b7
    b27.append(b28)
    while b27:
        b19 = b27.pop()
        b26.append(b19)
        if fonk5(b19.b4, b29.b4):
            fonk11(b28, b29, b12, name)
            return 'SUCCEED'
        b18 = fonk6(b19.b4, b12)
        for s in b18:
            b19.b10.append(s)
            if s not in b27 and s not in b26:
                fonk7(s, b19, b29.b4)
                b27.append(s)
                b27.sort(b30 = lambda e: e.b8, reverse=True)
            elif b19.b6 + s.b5 < s.b6:
                fonk7(s, b19, b29.b4)
                if s in b26:
                    fonk8(s)
    return 'FAIL'
if b31 = = "__main__":
    b16, b17, b12 = fonk3('boards/b12-2-1.txt')
    fonk13(b16, b17, b12, 'b12-2-1')
    b16, b17, b12 = fonk3('boards/b12-2-2.txt')
    fonk13(b16, b17, b12, 'b12-2-2')
    b16, b17, b12 = fonk3('boards/b12-2-3.txt')
    fonk13(b16, b17, b12, 'b12-2-3')
    b16, b17, b12 = fonk3('boards/b12-2-4.txt')
    fonk13(b16, b17, b12, 'b12-2-4')