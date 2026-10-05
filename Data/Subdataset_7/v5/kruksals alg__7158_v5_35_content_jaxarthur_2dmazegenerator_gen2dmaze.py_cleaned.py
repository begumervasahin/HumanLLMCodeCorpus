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
    while b7:
        b10 = random.choice(b7)
        cell1, b11 = fonk7(b10, b8)
        if cell1.b1 = = b11.b1:
            b9.append(class1(b10.b2, 0))
            b7.remove(b10)
        else:
            b12 = b11.b1
            b13 = cell1.b1
            for cell in b8:
                if cell.b1 = = b12:
                    cell.b1 = b13
            b7.remove(b10)
    b14 = [cell.b2 for cell in b6]
    b14.extend([cell.b2 for cell in b9])
    b15 = [[0 for _ in range(b4)] for _ in range(b5)]
    for b2 in b14:
        b15[b2[1]][b2[0]] = 1
    return b15
def fonk3(width, height):
    b6 = []
    for b16 in range(width):
        for y in range(height):
            if b16 = = 0 or y == 0 or b16 == width - 1 or y == height - 1 or (b16 % b17 == 0 and y % b17 == 0):
                b6.append(class1((b16, y), 0))
    return b6
def fonk4(width, height):
    b7 = []
    for b16 in range(width):
        for y in range(height):
            if 0 < b16 < width - 1 and 0 < y < height - 1 and ((b16 % b17 = = 1 and y % b17 == 0) or (b16 % b17 == 0 and y % b17 == 1)):
                b7.append(class1((b16, y), 1))
    return b7
def fonk5(width, height):
    b8 = []
    a1 = 0
    for b16 in range(width):
        for y in range(height):
            if 0 < b16 < width - 1 and 0 < y < height - 1 and b16 % b17 = = 1 and y % b17 == 1:
                b8.append(class1((b16, y), b17, a1))
                a1 += 1
    return b8
def fonk6(b16, y, b8):
    b2 = (b16, y)
    for cell in b8:
        if cell.b2 = = b2:
            return cell
    return None
def fonk7(b10, b8):
    b18 = [
        fonk6(b10.b2[0], b10.b2[1] + 1, b8),
        fonk6(b10.b2[0], b10.b2[1] - 1, b8),
        fonk6(b10.b2[0] + 1, b10.b2[1], b8),
        fonk6(b10.b2[0] - 1, b10.b2[1], b8)
    ]
    b18 = [n for n in b18 if n is not None]
    return b18[0], b18[1]
if b19 = = "__main__":
    print(fonk2(5, 6))