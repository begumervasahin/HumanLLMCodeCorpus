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
        b11 = file.readlines()
    b12 = []
    b16, b13 = None, None
    for i, line in enumerate(b11):
        b14 = []
        for j, b3 in enumerate(line.strip()):
            b15 = class2(class1(j, len(b11) - i - 1, b3), fonk4(b3))
            b14.append(b15)
            if b3 = = 'A':
                b16 = (j, len(b11) - i - 1)
            elif b3 = = 'B':
                b13 = (j, len(b11) - i - 1)
        b12.append(b14)
    b12.reverse()
    return b16, b13, b12
def fonk4(b3):
    b17 = {'w': 100, 'm': 50, 'b8': 10, 'b6': 5, 'r': 1}
    return b17.get(b3, 1)
def fonk5(s1, s2):
    return abs(s2.b1 - s1.b1) + abs(s2.b2 - s1.b2)
def fonk6(s1, sf):
    return s1.b1 = = sf.b1 and s1.b2 == sf.b2
def fonk7(s, b12):
    b18 = []
    if s.b1 > 0:
        b18.append(b12[s.b2][s.b1 - 1])
    if s.b1 < (len(b12[s.b2]) - 1):
        b18.append(b12[s.b2][s.b1 + 1])
    if s.b2 > 0:
        b18.append(b12[s.b2 - 1][s.b1])
    if s.b2 < (len(b12) - 1):
        b18.append(b12[s.b2 + 1][s.b1])
    return b18
def fonk8(child, b9, end_state):
    child.b9 = b9
    child.b6 = b9.b6 + child.b5
    b7 = fonk5(child.b4, end_state)
    child.b7 = b7
    child.b8 = b7 + child.b6
def fonk9(b9):
    for child in b9.b10:
        if b9.b6 + child.b5 < child.b6:
            child.b9 = b9
            child.b6 = b9.b6 + child.b5
            child.b8 = child.b6 + child.b7
            fonk9(child)
def fonk10(b15):
    b19 = {'w': (73, 216, 245), 'm': (99, 99, 99), 'b8': (3, 82, 0),
                      'b6': (50, 200, 50), 'r': (114, 80, 41), 'A': (90, 180, 90), 'B': (255, 90, 90)}
    return b19.get(b15.b4.b3, (255, 255, 255))
def fonk11(b31, b32, b12, name):
    b20 = b32
    b21 = [b32]
    while b20 != b31:
        b20 = b20.b9
        b21.append(b20)
    b12.reverse()
    fonk12(b12, b21, name)
    b22 = b21[1:-1]
    for b15 in b22:
        b15.b4.b3 = 'O'
    b23 = ''
    for line in b12:
        b23 += ''.join(b15.b4.b3 for b15 in line) + '\n'
    print(b23)
def fonk12(b12, b21, name):
    b24 = Image.new('RGB', (len(b12[0]) * 20, len(b12) * 20), "white")
    b25 = ImageDraw.Draw(b24)
    for b2, row in enumerate(b12):
        for b1, b15 in enumerate(row):
            b26 = fonk10(b15)
            b25.rectangle([(b1 * 20, b2 * 20), (b1 * 20 + 20, b2 * 20 + 20)], b27 = b26, outline=(0, 0, 0))
            if b15 in b21:
                b25.rectangle([(b1 * 20 + 6, b2 * 20 + 6), (b1 * 20 + 14, b2 * 20 + 14)], b27 = (107, 97, 255), outline=(0, 0, 0))
    b28 = "assignment3_images/part2_" + name + ".png"
    b24.save(b28, "PNG")
def fonk13(b16, b13, b12, name):
    b29 = []
    b30 = []
    b31 = b12[b16[1]][b16[0]]
    b32 = b12[b13[1]][b13[0]]
    b31.b6 = 0
    b7 = fonk5(b31.b4, b32.b4)
    b31.b7 = b7
    b31.b8 = b7
    b30.append(b31)
    while b30:
        b20 = b30.pop()
        b29.append(b20)
        if fonk6(b20.b4, b32.b4):
            fonk11(b31, b32, b12, name)
            return 'SUCCEED'
        b18 = fonk7(b20.b4, b12)
        for successor in b18:
            b20.b10.append(successor)
            if successor not in b30 and successor not in b29:
                fonk8(successor, b20, b32.b4)
                b30.append(successor)
                b30.sort(b33 = lambda e: e.b8, reverse=True)
            elif b20.b6 + successor.b5 < successor.b6:
                fonk8(successor, b20, b32.b4)
                if successor in b29:
                    fonk9(successor)
    return 'FAIL'
b16, b13, b12 = fonk3('boards/b12-2-1.txt')
b12 = fonk13(b16, b13, b12, 'b12-2-1')
b16, b13, b12 = fonk3('boards/b12-2-2.txt')
b12 = fonk13(b16, b13, b12, 'b12-2-2')
b16, b13, b12 = fonk3('boards/b12-2-3.txt')
b12 = fonk13(b16, b13, b12, 'b12-2-3')
b16, b13, b12 = fonk3('boards/b12-2-4.txt')
b12 = fonk13(b16, b13, b12, 'b12-2-4')