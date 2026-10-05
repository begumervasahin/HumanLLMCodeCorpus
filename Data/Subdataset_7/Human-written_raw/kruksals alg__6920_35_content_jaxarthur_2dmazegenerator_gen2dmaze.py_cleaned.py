import math, random
class class1():
    def fonk1(self, b2, b3, b1 = None):
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
def fonk2(width, height):
    b4 = width * b18 + 1
    b5 = height * b18 + 1
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
    b15 = []
    for y in range(b5):
        b16 = []
        for b17 in range(b4):
            b16.append(0)
        b15.append(b16)
    for b2 in b14:
        b15[b2[1]][b2[0]] = 1
    return(b15)
def fonk3(width, height):
    b15 = []
    for b17 in range(width):
        for y in range(height):
            if b17 = = 0 or y == 0 or b17 == width-1 or y == height-1:
                b15.append(class1((b17, y), 0))
            elif b17 % b18 = = 0 and y % b18 == 0:
                b15.append(class1((b17, y), 0))
    return b15
def fonk4(width, height):
    b15 = []
    for b17 in range(width):
        for y in range(height):
            if b17 = = 0 or y == 0 or b17 == width-1 or y == height-1:
                pass
            elif b17 % b18 = = 1 and y % b18 == 0:
                b15.append(class1((b17, y), 1))
            elif b17 % b18 = = 0 and y % b18 == 1:
                b15.append(class1((b17,y), 1))
    return b15
def fonk5(width, height):
    b15 = []
    a1 = 0
    for b17 in range(width):
        for y in range(height):
            if b17 = = 0 or y == 0 or b17 == width-1 or y == height-1:
                pass
            elif b17 % b18 = = 1 and y % b18 == 1:
                b15.append(class1((b17, y), b18, a1))
                a1 += 1
    return (b15)
def fonk6(b17, y, b8):
    b2 = (b17, y)
    for cel in b8:
        if cel.b2 = = b2:
            return cel
    return None
def fonk7(b10, b8):
    b19 = []
    b19.append(fonk6(b10.b2[0], b10.b2[1] + 1, b8))
    b19.append(fonk6(b10.b2[0], b10.b2[1] - 1, b8))
    b19.append(fonk6(b10.b2[0] + 1, b10.b2[1], b8))
    b19.append(fonk6(b10.b2[0] - 1, b10.b2[1], b8))
    b19.remove(None)
    b19.remove(None)
    return(b19[0], b19[1])
def fonk8(width, height, nodes):
    b15 = []
    for b17 in range(width):
        b16 = []
        for y in range(height):
            b16.append(0)
        b15.append(b16)
    for node in nodes:
        b15[node[0]][node[1]] = 1
    print("drawing")
    for i in b15:
        print(str(i)+"\n")
def fonk9(width, height, nodes):
    b15 = []
    for b17 in range(height):
        b16 = []
        for y in range(width):
            b16.append(0)
        b15.append(b16)
    for node in nodes:
        b15[node.b2[0]][node.b2[1]] = node.b1
    print("drawing")
    for i in b15:
        print(str(i)+"\n")
if b20 = = "__main__":
    print(fonk2(5, 6))