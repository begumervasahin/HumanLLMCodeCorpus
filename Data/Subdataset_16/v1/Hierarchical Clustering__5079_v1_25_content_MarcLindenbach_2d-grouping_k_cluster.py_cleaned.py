import random
from PIL import Image, ImageDraw
b1 = [
    (255, 127, 39),
    (34, 177, 76),
    (0, 162, 232),
    (163, 73, 164),
    (255, 242, 0),
    (63, 72, 204)
]
a1 = 8
b2 = (0, 0, 0)
def fonk1(b3 = (400, 400)):
    b4 = Image.new('RGB', b3, (255, 255, 255))
    b5 = ImageDraw.Draw(b4)
    return b4, b5
def fonk2(b5, point, color, b3 = 3):
    x, b6 = point
    b5.ellipse([x - b3, b6 - b3, x + b3, b6 + b3], b7 = color, outline=color)
def fonk3(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
def fonk4(b8 = 100, b3=(400, 400)):
    return [(random.randint(0, b3[0]), random.randint(0, b3[1])) for _ in range(b8)]
def fonk5(b17, b9 = None, b15=None, b13='cluster.jpeg'):
    b4, b5 = fonk1()
    if b15:
        for i, matches in enumerate(b15):
            for match in matches:
                x1, b10 = b17[match]
                x2, b11 = b9[i]
                b5.line((x1, b10, x2, b11), b7 = b1[i])
    if b9:
        for i, cluster in enumerate(b9):
            fonk2(b5, cluster, b1[i], b3 = a1)
    for point in b17:
        fonk2(b5, point, b2)
    b4.save(b13)
def fonk6(b17, b12 = 6, distance=p_distance, b13='b12-iteration-%d.jpeg'):
    fonk5(b17, b13 = b13 % 0)
    b9 = fonk4(b8=b12)
    b14 = None
    for iter in range(1, 100):
        print(f'Iteration {iter}...')
        b15 = [[] for _ in range(b12)]
        for i, point in enumerate(b17):
            b16 = min(range(b12), key=lambda j: distance(b9[j], point))
            b15[b16].append(i)
        if b15 = = b14:
            break
        b14 = b15
        fonk5(b17, b9 = b9, b15=b15, b13=b13 % iter)
        for i, cluster in enumerate(b9):
            if b15[i]:
                b9[i] = [
                    sum(b17[j][0] for j in b15[i]) / len(b15[i]),
                    sum(b17[j][1] for j in b15[i]) / len(b15[i])
                ]
    return b9
def fonk7():
    b17 = fonk4(b8=100)
    fonk6(b17, b12 = 6)
if b18 = = "__main__":
    fonk7()