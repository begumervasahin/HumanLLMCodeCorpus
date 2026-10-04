import os
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
        for j, b14 in enumerate(line):
            b13.append(class2(class1(j, len(b11) - i - 1, b14), fonk9(b14)))
            if b14 = = 'A':
                b15 = (j, len(b11) - i - 1)
            elif b14 = = 'B':
                b16 = (j, len(b11) - i - 1)
        b12.append(b13)
    b12.reverse()
    return b15, b16, b12
def fonk4(s1, s2):
    return abs(s2.b1 - s1.b1) + abs(s2.b2 - s1.b2)
def fonk5(s1, sf):
    return s1.b1 = = sf.b1 and s1.b2 == sf.b2
def fonk6(s, b12):
    b17 = []
    if s.b1 > 0:
        b17.append(b12[s.b2][s.b1 - 1])
    if s.b1 < len(b12[s.b2]) - 1:
        b17.append(b12[s.b2][s.b1 + 1])
    if s.b2 > 0:
        b17.append(b12[s.b2 - 1][s.b1])
    if s.b2 < len(b12) - 1:
        b17.append(b12[s.b2 + 1][s.b1])
    return b17
def fonk7(child, b9, goal):
    child.b9 = b9
    child.b6 = b9.b6 + child.b5
    b7 = fonk4(child.b4, goal)
    child.b7 = b7
    child.b8 = b7 + child.b6
def fonk8(b9):
    for child in b9.b10:
        if b9.b6 + child.b5 < child.b6:
            child.b9 = b9
            child.b6 = b9.b6 + child.b5
            child.b8 = child.b6 + child.b7
            fonk8(child)
def fonk9(b3):
    b18 = {'w': 100, 'm': 50, 'b8': 10, 'b6': 5, 'r': 1, 'A': 1, 'B': 1}
    return b18.get(b3, 1)
def fonk10(node):
    b19 = {
        'w': (73, 216, 245), 'm': (99, 99, 99), 'b8': (3, 82, 0),
        'b6': (50, 200, 50), 'r': (114, 80, 41), 'A': (90, 180, 90), 'B': (255, 90, 90)
    }
    return b19.get(node.b4.b3, (255, 255, 255))
def fonk11(b12, b24, filename):
    b20 = Image.new('RGB', (len(b12[0]) * 20, len(b12) * 20), "white")
    b21 = ImageDraw.Draw(b20)
    for b2 in range(len(b12)):
        for b1 in range(len(b12[0])):
            b22 = fonk10(b12[b2][b1])
            b21.rectangle([(b1 * 20, b2 * 20), (b1 * 20 + 20, b2 * 20 + 20)], b23 = b22, outline=(0, 0, 0))
            if b12[b2][b1] in b24:
                b22 = (107, 97, 255)
                b21.rectangle([(b1 * 20 + 6, b2 * 20 + 6), (b1 * 20 + 14, b2 * 20 + 14)], b23 = b22, outline=(0, 0, 0))
    b20.save(filename, "PNG")
def fonk12(b28, b29, b12, filename):
    b24 = []
    b25 = b29
    while b25 != b28:
        b24.append(b25)
        b25 = b25.b9
    b24.append(b28)
    b24.reverse()
    fonk11(b12, b24, filename)
def fonk13(b15, b16, b12, filename):
    b26 = []
    b27 = []
    b28 = b12[b15[1]][b15[0]]
    b29 = b12[b16[1]][b16[0]]
    b28.b6 = 0
    b28.b7 = fonk4(b28.b4, b29.b4)
    b28.b8 = b28.b7
    b26.append(b28)
    while b26:
        b26.sort(b30 = lambda node: node.b8)
        b31 = b26.pop(0)
        b27.append(b31)
        if fonk5(b31.b4, b29.b4):
            fonk12(b28, b29, b12, filename)
            return 'SUCCEED'
        b17 = fonk6(b31.b4, b12)
        for successor in b17:
            b31.b10.append(successor)
            if successor not in b26 and successor not in b27:
                fonk7(successor, b31, b29.b4)
                b26.append(successor)
            elif b31.b6 + successor.b5 < successor.b6:
                fonk7(successor, b31, b29.b4)
                if successor in b27:
                    fonk8(successor)
    return 'FAIL'
if b32 = = "__main__":
    os.makedirs("assignment3_images", b33 = True)
    b34 = ['b12-2-1.txt', 'b12-2-2.txt', 'b12-2-3.txt', 'b12-2-4.txt']
    for board_file in b34:
        b15, b16, b12 = fonk3(b8'b34/{board_file}')
        fonk13(b15, b16, b12, b8'assignment3_images/part2_{board_file}')