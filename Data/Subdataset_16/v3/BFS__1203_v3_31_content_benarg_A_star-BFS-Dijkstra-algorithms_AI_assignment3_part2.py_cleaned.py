import os
from PIL import Image, ImageDraw
b1 = {'w': 100, 'm': 50, 'b9': 10, 'b8': 5, 'r': 1, 'A': 1, 'B': 1}
b2 = {
    'w': (73, 216, 245), 'm': (99, 99, 99), 'b9': (3, 82, 0),
    'b8': (50, 200, 50), 'r': (114, 80, 41), 'A': (90, 180, 90), 'B': (255, 90, 90)
}
class class1:
    def fonk1(self, b3, b4, b5):
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
class class2:
    def fonk2(self, b6, b7):
        self.b6 = b6
        self.b7 = b7
        self.b8 = float('inf')
        self.a1 = 0
        self.b9 = float('inf')
        self.b10 = None
        self.b11 = []
def fonk3(filename):
    with open(filename, 'r') as file:
        b12 = file.read().strip().split('\n')
    b13 = []
    b18, b14 = None, None
    for b4, line in enumerate(b12):
        b15 = []
        for b3, b17 in enumerate(line):
            b16 = class2(class1(b3, len(b12) - b4 - 1, b17), b1[b17])
            b15.append(b16)
            if b17 = = 'A':
                b18 = (b3, len(b12) - b4 - 1)
            elif b17 = = 'B':
                b14 = (b3, len(b12) - b4 - 1)
        b13.append(b15)
    b13.reverse()
    return b18, b14, b13
def fonk4(s1, s2):
    return abs(s2.b3 - s1.b3) + abs(s2.b4 - s1.b4)
def fonk5(s1, s2):
    return s1.b3 = = s2.b3 and s1.b4 == s2.b4
def fonk6(s, b13):
    b19 = []
    if s.b3 > 0:
        b19.append(b13[s.b4][s.b3 - 1])
    if s.b3 < len(b13[s.b4]) - 1:
        b19.append(b13[s.b4][s.b3 + 1])
    if s.b4 > 0:
        b19.append(b13[s.b4 - 1][s.b3])
    if s.b4 < len(b13) - 1:
        b19.append(b13[s.b4 + 1][s.b3])
    return b19
def fonk7(child, b10, goal):
    child.b10 = b10
    child.b8 = b10.b8 + child.b7
    child.a1 = fonk4(child.b6, goal)
    child.b9 = child.b8 + child.a1
def fonk8(b10):
    for child in b10.b11:
        if b10.b8 + child.b7 < child.b8:
            fonk7(child, b10, b10.b6)
            fonk8(child)
def fonk9(b13, b23, filename):
    b20 = Image.new('RGB', (len(b13[0]) * 20, len(b13) * 20), "white")
    b21 = ImageDraw.Draw(b20)
    for b4, b15 in enumerate(b13):
        for b3, b16 in enumerate(b15):
            b21.rectangle([(b3 * 20, b4 * 20), (b3 * 20 + 20, b4 * 20 + 20)], b22 = b2[b16.b6.b5], outline=(0, 0, 0))
            if b16 in b23:
                b21.rectangle([(b3 * 20 + 6, b4 * 20 + 6), (b3 * 20 + 14, b4 * 20 + 14)], b22 = (107, 97, 255), outline=(0, 0, 0))
    b20.save(filename, "PNG")
def fonk10(b27, b28, b13, filename):
    b23 = []
    b24 = b28
    while b24 != b27:
        b23.append(b24)
        b24 = b24.b10
    b23.append(b27)
    b23.reverse()
    fonk9(b13, b23, filename)
def fonk11(b18, b14, b13, filename):
    b25 = []
    b26 = []
    b27 = b13[b18[1]][b18[0]]
    b28 = b13[b14[1]][b14[0]]
    b27.b8 = 0
    b27.a1 = fonk4(b27.b6, b28.b6)
    b27.b9 = b27.a1
    b25.append(b27)
    while b25:
        b25.sort(b29 = lambda b16: b16.b9)
        b30 = b25.pop(0)
        b26.append(b30)
        if fonk5(b30.b6, b28.b6):
            fonk10(b27, b28, b13, filename)
            return 'SUCCEEDED'
        b19 = fonk6(b30.b6, b13)
        for successor in b19:
            b30.b11.append(successor)
            if successor not in b25 and successor not in b26:
                fonk7(successor, b30, b28.b6)
                b25.append(successor)
            elif b30.b8 + successor.b7 < successor.b8:
                fonk7(successor, b30, b28.b6)
                if successor in b26:
                    fonk8(successor)
    return 'FAILED'
if b31 = = "__main__":
    os.makedirs("assignment3_images", b32 = True)
    b33 = ['b13-2-1.txt', 'b13-2-2.txt', 'b13-2-3.txt', 'b13-2-4.txt']
    for board_file in b33:
        b18, b14, b13 = fonk3(b9'b33/{board_file}')
        b34 = fonk11(b18, b14, b13, b9'assignment3_images/part2_{board_file}')
        print(b9'Result for {board_file}: {b34}')