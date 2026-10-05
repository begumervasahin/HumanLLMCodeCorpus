import math
import random
class class1:
    def fonk1(self, b2, b3, b1 = None):
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
def fonk2(width, height):
    b4 = width * b17 + 1
    b5 = height * b17 + 1
    b6 = fonk3(b4, b5)
    b7 = fonk4(b4, b5)
    b8 = fonk5(b4, b5)
    b9 = []
    while len(b7) > 0:
        b10 = b7[random.randint(0, len(b7)-1)]
        cell1, b11 = fonk7(b10, b8)
        if cell1.b1 = = b11.b1:
            b9.append(class1(b10.b2, 0))
            b7.remove(b10)
        else:
            b12 = b11.b1
            b13 = cell1.b1
            for cel in b8:
                if cel.b1 = = b12:
                    cel.b1 = b13
            b7.remove(b10)
    b14 = []
    for cel in b6:
        b14.append(cel.b2)
    for cel in b9:
        b14.append(cel.b2)
    b15 = [[0 for _ in range(b4)] for _ in range(b5)]
    for b2 in b14:
        b15[b2[1]][b2[0]] = 1
    return b15
def fonk3(width, height):
    b15 = []
    for b16 in range(width):
        for y in range(height):
            if b16 = = 0 or y == 0 or b16 == width-1 or y == height-1:
                b15.append(class1((b16, y), 0))
            elif b16 % b17 = = 0 and y % b17 == 0:
                b15.append(class1((b16, y), 0))
    return b15
def fonk4(width, height):
    b15 = []
    for b16 in range(width):
        for y in range(height):
            if b16 = = 0 or y == 0 or b16 == width-1 or y == height-1:
                pass
            elif b16 % b17 = = 1 and y % b17 == 0:
                b15.append(class1((b16, y), 1))
            elif b16 % b17 = = 0 and y % b17 == 1:
                b15.append(class1((b16,y), 1))
    return b15
def fonk5(width, height):
    b15 = []
    a1 = 0
    for b16 in range(width):
        for y in range(height):
            if b16 = = 0 or y == 0 or b16 == width-1 or y == height-1:
                pass
            elif b16 % b17 = = 1 and y % b17 == 1:
                b15.append(class1((b16, y), b17, a1))
                a1 += 1
    return b15
def fonk6(b16, y, b8):
    b2 = (b16, y)
    for cel in b8:
        if cel.b2 = = b2:
            return cel
    return None
def fonk7(b10, b8):
    b18 = []
    b18.append(fonk6(b10.b2[0], b10.b2[1] + 1, b8))
    b18.append(fonk6(b10.b2[0], b10.b2[1] - 1, b8))
    b18.append(fonk6(b10.b2[0] + 1, b10.b2[1], b8))
    b18.append(fonk6(b10.b2[0] - 1, b10.b2[1], b8))
    b18 = [neighbor for neighbor in b18 if neighbor is not None]
    return b18[0], b18[1]
if b19 = = "__main__":
    print(fonk2(5, 6))