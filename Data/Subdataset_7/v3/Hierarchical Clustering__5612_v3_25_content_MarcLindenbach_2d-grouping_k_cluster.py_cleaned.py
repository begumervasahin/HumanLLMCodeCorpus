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
def fonk2(b4, point, color, b5 = 1):
    x, b6 = point
    b4.ellipse((x - b5, b6 - b5, x + b5, b6 + b5), b7 = color)
def fonk3(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
def fonk4(b8 = 100):
    return [(random.randint(0, 500), random.randint(0, 500)) for _ in range(b8)]
def fonk5(b19, b9 = 6, distance=euclidean_distance, b10='b9-iteration-%d.jpeg'):
    fonk6(b19, b10 = b10 % 0)
    b11 = fonk4(b8=b9)
    b12 = None
    for iteration in range(1, 100):
        print('Iteration %d...' % iteration)
        b13 = [[] for _ in range(b9)]
        for i, point in enumerate(b19):
            b14 = min(range(b9), key=lambda j: distance(b11[j], point))
            b13[b14].append(i)
        if b12 = = b13:
            break
        b12 = b13
        fonk6(b19, b11 = b11, b13=b13, b10=b10 % iteration)
        for i in range(b9):
            b15 = [b19[idx] for idx in b13[i]]
            if b15:
                b11[i] = [sum(coord) / len(b15) for coord in zip(*b15)]
    return b11
def fonk6(b19, b11 = None, b13=None, b10='cluster.jpeg'):
    b3, b4 = fonk1()
    if b13:
        for i, match in enumerate(b13):
            for j in match:
                x1, b16 = b19[j]
                x2, b17 = b11[i]
                b4.line((x1, b16, x2, b17), b7 = b1[i])
    if b11:
        for i, cluster in enumerate(b11):
            fonk2(b4, cluster, b1[i], b5 = a1)
    for point in b19:
        fonk2(b4, point, b2)
    b3.save(b10)
if b18 = = "__main__":
    b19 = fonk4()
    b11 = fonk5(b19)
    fonk6(b19, b11 = b11)