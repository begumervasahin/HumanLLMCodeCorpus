from cluster import *
b1 = [
    (255, 127, 39),
    (34, 177, 76),
    (0, 162, 232),
    (163, 73, 164),
    (255, 242, 0),
    (63, 72, 204),
]
a1 = 8
def fonk1(points, b2 = 6, distance=p_distance, b3='b2-iteration-%b8.jpeg'):
    fonk2(points, b3 = b3 % 0)
    b4 = generate_points(n=b2)
    b5 = None
    for iter in range(1, 100):
        print('iteration %b8...' % iter)
        b6 = [[] for i in range(b2)]
        for i in range(len(points)):
            b7 = points[i]
            a2 = 0
            for j in range(b2):
                b8 = distance(b4[j], b7)
                if b8 < distance(b4[a2], b7): a2 = j
            b6[a2].append(i)
        if b5 = = b6: break
        b5 = b6
        fonk2(points, b4 = b4, b6=b6, b3=b3 % iter)
        for i in range(len(b4)):
            b9 = [0.0, 0.0]
            for j in range(len(b6[i])):
                b9[0] += points[b6[i][j]][0]
                b9[1] += points[b6[i][j]][1]
            if len(b6[i])>0:
                b9[0] /= len(b6[i])
            if len(b6[i])>0:
                b9[1] /= len(b6[i])
            b4[i] = b9
    return b4
def fonk2(points, b4 = None, b6=None, b3='cluster.jpeg'):
    img, b10 = create_image()
    if b6:
        for i in range(len(b6)):
            for j in range(len(b6[i])):
                b11 = points[b6[i][j]][0]
                b12 = points[b6[i][j]][1]
                b13 = b4[i][0]
                b14 = b4[i][1]
                b10.line((b11, b12, b13, b14), b15 = b1[i])
    if b4:
        for i in range(len(b4)):
            draw_point(b10, b4[i], b1[i], b16 = a1)
    for b7 in points:
        draw_point(b10, b7, POINT_COLOR)
    img.save(b3)