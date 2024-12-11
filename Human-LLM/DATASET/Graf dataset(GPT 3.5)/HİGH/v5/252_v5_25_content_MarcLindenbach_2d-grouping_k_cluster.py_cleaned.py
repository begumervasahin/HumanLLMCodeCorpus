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
def fonk1(points, b2 = 6, distance=p_distance, b3='b2-iteration-%d.jpeg'):
    fonk2(points, b3 = b3 % 0)
    b4 = generate_points(n=b2)
    b5 = None
    for iteration in range(1, 100):
        print(f'Iteration {iteration}...')
        b6 = [[] for _ in range(b2)]
        for i, point in enumerate(points):
            b7 = min(range(b2), key=lambda j: distance(b4[j], point))
            b6[b7].append(i)
        if b5 = = b6:
            break
        b5 = b6
        fonk2(points, b4 = b4, b6=b6, b3=b3 % iteration)
        for i, cluster in enumerate(b4):
            b8 = [points[idx] for idx in b6[i]]
            if b8:
                b9 = [sum(coord) / len(b8) for coord in zip(*b8)]
                b4[i] = b9
    return b4
def fonk2(points, b4 = None, b6=None, b3='cluster.jpeg'):
    img, b10 = create_image()
    if b6:
        for i, matches in enumerate(b6):
            for j in matches:
                x1, b11 = points[j]
                x2, b12 = b4[i]
                b10.line((x1, b11, x2, b12), b13 = b1[i])
    if b4:
        for i, cluster in enumerate(b4):
            draw_point(b10, cluster, b1[i], b14 = a1)
    for point in points:
        draw_point(b10, point, POINT_COLOR)
    img.save(b3)