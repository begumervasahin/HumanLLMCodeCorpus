from PIL import Image, ImageDraw
import random
b1 = [
    (255, 127, 39),
    (34, 177, 76),
    (0, 162, 232),
    (163, 73, 164),
    (255, 242, 0),
    (63, 72, 204),
]
a1 = 8
b2 = (0, 0, 0)
def fonk1():
    b3 = Image.new('RGB', (500, 500), color='white')
    b4 = ImageDraw.Draw(b3)
    return b3, b4
def fonk2(b4, b14, color, b5 = 1):
    x, b6 = b14
    b4.ellipse((x - b5, b6 - b5, x + b5, b6 + b5), b7 = color)
def fonk3(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
def fonk4(b8 = 100):
    return [(random.randint(0, 500), random.randint(0, 500)) for _ in range(b8)]
def fonk5(b22, b9 = 6, distance=p_distance, b10='b9-iteration-%b15.jpeg'):
    fonk6(b22, b10 = b10 % 0)
    b11 = fonk4(b8=b9)
    b12 = None
    for iter in range(1, 100):
        print('iteration %b15...' % iter)
        b13 = [[] for i in range(b9)]
        for i in range(len(b22)):
            b14 = b22[i]
            a2 = 0
            for j in range(b9):
                b15 = distance(b11[j], b14)
                if b15 < distance(b11[a2], b14): a2 = j
            b13[a2].append(i)
        if b12 = = b13: break
        b12 = b13
        fonk6(b22, b11 = b11, b13=b13, b10=b10 % iter)
        for i in range(len(b11)):
            b16 = [0.0, 0.0]
            for j in range(len(b13[i])):
                b16[0] += b22[b13[i][j]][0]
                b16[1] += b22[b13[i][j]][1]
            if len(b13[i]) > 0:
                b16[0] /= len(b13[i])
            if len(b13[i]) > 0:
                b16[1] /= len(b13[i])
            b11[i] = b16
    return b11
def fonk6(b22, b11 = None, b13=None, b10='cluster.jpeg'):
    b3, b4 = fonk1()
    if b13:
        for i in range(len(b13)):
            for j in range(len(b13[i])):
                b17 = b22[b13[i][j]][0]
                b18 = b22[b13[i][j]][1]
                b19 = b11[i][0]
                b20 = b11[i][1]
                b4.line((b17, b18, b19, b20), b7 = b1[i])
    if b11:
        for i in range(len(b11)):
            fonk2(b4, b11[i], b1[i], b5 = a1)
    for b14 in b22:
        fonk2(b4, b14, b2)
    b3.save(b10)
if b21 = = "__main__":
    b22 = fonk4()
    b11 = fonk5(b22)
    fonk6(b22, b11 = b11)