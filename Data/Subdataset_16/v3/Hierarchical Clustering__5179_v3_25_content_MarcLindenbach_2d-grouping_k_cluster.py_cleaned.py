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
a1 = 3
a2 = 8
b2 = (0, 0, 0)
def fonk1(b3 = (400, 400)):
    b4 = Image.new('RGB', b3, (255, 255, 255))
    b5 = ImageDraw.Draw(b4)
    return b4, b5
def fonk2(b5, b10, color, b3 = a1):
    x, b6 = b10
    b5.ellipse([x - b3, b6 - b3, x + b3, b6 + b3], b7 = color, outline=color)
def fonk3(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
def fonk4(b8 = 100, b3=(400, 400)):
    return [(random.randint(0, b3[0]), random.randint(0, b3[1])) for _ in range(b8)]
def fonk5(b17, b9 = None, b15=None, b13='cluster.jpeg'):
    b4, b5 = fonk1()
    if b15:
        for cluster_index, cluster_points in enumerate(b15):
            for point_index in cluster_points:
                b10 = b17[point_index]
                b11 = b9[cluster_index]
                b5.line((b10[0], b10[1], b11[0], b11[1]), b7 = b1[cluster_index])
    if b9:
        for cluster_index, b11 in enumerate(b9):
            fonk2(b5, b11, b1[cluster_index], b3 = a2)
    for b10 in b17:
        fonk2(b5, b10, b2)
    b4.save(b13)
def fonk6(b17, b12 = 6, distance_func=euclidean_distance, file_template='k-iteration-%d.jpeg'):
    fonk5(b17, b13 = file_template % 0)
    b9 = fonk4(b8=b12)
    b14 = None
    for iteration in range(1, 100):
        print(f'Iteration {iteration}...')
        b15 = [[] for _ in range(b12)]
        for i, b10 in enumerate(b17):
            b16 = min(range(b12), key=lambda j: distance_func(b9[j], b10))
            b15[b16].append(i)
        if b15 = = b14:
            break
        b14 = b15
        fonk5(b17, b9 = b9, b15=b15, b13=file_template % iteration)
        for i, cluster_points in enumerate(b15):
            if cluster_points:
                b9[i] = [
                    sum(b17[j][0] for j in cluster_points) / len(cluster_points),
                    sum(b17[j][1] for j in cluster_points) / len(cluster_points)
                ]
    return b9
def fonk7():
    b17 = fonk4(b8=100)
    fonk6(b17, b12 = 6)
if b18 = = "__main__":
    fonk7()