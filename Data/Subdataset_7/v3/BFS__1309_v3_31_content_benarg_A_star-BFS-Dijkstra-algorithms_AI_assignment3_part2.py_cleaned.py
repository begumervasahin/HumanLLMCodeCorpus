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
            b15 = class2(class1(j, len(b11) - i - 1, b3), fonk9(b3))
            b14.append(b15)
            if b3 = = 'A':
                b16 = (j, len(b11) - i - 1)
            elif b3 = = 'B':
                b13 = (j, len(b11) - i - 1)
        b12.append(b14)
    b12.reverse()
    return b16, b13, b12
def fonk4(s1, s2):
    return abs(s2.b1 - s1.b1) + abs(s2.b2 - s1.b2)
def fonk5(s1, sf):
    return s1.b1 = = sf.b1 and s1.b2 == sf.b2
def fonk6(s, b12):
    b17 = []
    if s.b1 > 0:
        b17.append(b12[s.b2][s.b1 - 1])
    if s.b1 < (len(b12[s.b2]) - 1):
        b17.append(b12[s.b2][s.b1 + 1])
    if s.b2 > 0:
        b17.append(b12[s.b2 - 1][s.b1])
    if s.b2 < (len(b12) - 1):
        b17.append(b12[s.b2 + 1][s.b1])
    return b17
def fonk7(child, b9, goal_state):
    child.b9 = b9
    child.b6 = b9.b6 + child.b5
    child.b7 = fonk4(child.b4, goal_state)
    child.b8 = child.b6 + child.b7
def fonk8(b15):
    for child in b15.b10:
        if b15.b6 + child.b5 < child.b6:
            child.b9 = b15
            child.b6 = b15.b6 + child.b5
            child.b8 = child.b6 + child.b7
            fonk8(child)
def fonk9(b3):
    b18 = {'w': 100, 'm': 50, 'b8': 10, 'b6': 5, 'r': 1}
    return b18.get(b3, 1)
def fonk10(b15):
    b19 = {'w': (73, 216, 245), 'm': (99, 99, 99), 'b8': (3, 82, 0),
                      'b6': (50, 200, 50), 'r': (114, 80, 41), 'A': (90, 180, 90), 'B': (255, 90, 90)}
    return b19.get(b15.b4.b3, (255, 255, 255))
def fonk11(b30, end_node, b12, filename):
    b20 = end_node
    b21 = [end_node]
    while b20 != b30:
        b20 = b20.b9
        b21.append(b20)
    b12.reverse()
    fonk12(b12, b21, filename)
    b22 = ''
    for b15 in b21[1:-1]:
        b15.b4.b3 = 'O'
    for line in b12:
        for b15 in line:
            b22 += b15.b4.b3
        b22 += '\n'
    print(b22)
def fonk12(b12, b21, filename):
    b23 = Image.new('RGB', (len(b12[0]) * 20, len(b12) * 20), "white")
    b24 = ImageDraw.Draw(b23)
    for b2 in range(len(b12)):
        for b1 in range(len(b12[0])):
            b25 = fonk10(b12[b2][b1])
            b24.rectangle([(b1 * 20, b2 * 20), (b1 * 20 + 20, b2 * 20 + 20)], b26 = b25, outline=(0, 0, 0))
            if b12[b2][b1] in b21:
                b24.rectangle([(b1 * 20 + 6, b2 * 20 + 6), (b1 * 20 + 14, b2 * 20 + 14)], b26 = (107, 97, 255), outline=(0, 0, 0))
    b27 = "assignment3_images/part2_" + filename + ".png"
    b23.save(b27, "PNG")
def fonk13(b16, b13, b12, filename):
    b28 = []
    b29 = []
    b30 = b12[b16[1]][b16[0]]
    b31 = b12[b13[1]][b13[0]]
    b30.b6 = 0
    b30.b7 = fonk4(b30.b4, b31.b4)
    b30.b8 = b30.b7
    b29.append(b30)
    while b29:
        b20 = b29.pop()
        b28.append(b20)
        if fonk5(b20.b4, b31.b4):
            fonk11(b30, b31, b12, filename)
            return 'SUCCEED'
        b17 = fonk6(b20.b4, b12)
        for successor in b17:
            b20.b10.append(successor)
            if successor not in b29 and successor not in b28:
                fonk7(successor, b20, b31.b4)
                b29.append(successor)
                b29.sort(b32 = lambda b1: b1.b8, reverse=True)
            elif b20.b6 + successor.b5 < successor.b6:
                fonk7(successor, b20, b31.b4)
                if successor in b28:
                    fonk8(successor)
    return 'FAIL'
start_1, end_1, b33 = fonk3('boards/b12-2-1.txt')
b33 = fonk13(start_1, end_1, b33, 'b12-2-1')
start_2, end_2, b34 = fonk3('boards/b12-2-2.txt')
b34 = fonk13(start_2, end_2, b34, 'b12-2-2')
start_3, end_3, b35 = fonk3('boards/b12-2-3.txt')
b35 = fonk13(start_3, end_3, b35, 'b12-2-3')
start_4, end_4, b36 = fonk3('boards/b12-2-4.txt')
b36 = fonk13(start_4, end_4, b36, 'b12-2-4')