from cluster import *
b1 = [
    (255, 127, 39),
    (34, 177, 76),
    (0, 162, 232),
    (163, 73, 164),
    (255, 242, 0),
    (63, 72, 204)
]
a1 = 8
def fonk1(points, b2 = 6, distance_func=p_distance, file_name_template='k-iteration-%d.jpeg'):
    fonk2(points, b3 = file_name_template % 0)
    b4 = generate_points(n=b2)
    b5 = None
    for iteration in range(1, 100):
        print(f'Iteration {iteration}...')
        b6 = [[] for _ in range(b2)]
        for i, b9 in enumerate(points):
            b7 = min(range(b2), key=lambda j: distance_func(b4[j], b9))
            b6[b7].append(i)
        if b6 = = b5:
            break
        b5 = b6
        fonk2(points, b4 = b4, matches=b6, b3=file_name_template % iteration)
        for i in range(len(b4)):
            if b6[i]:
                b4[i] = [
                    sum(points[j][0] for j in b6[i]) / len(b6[i]),
                    sum(points[j][1] for j in b6[i]) / len(b6[i])
                ]
    return b4
def fonk2(points, b4 = None, matches=None, b3='cluster.jpeg'):
    img, b8 = create_image()
    if matches and b4:
        for i, cluster_points in enumerate(matches):
            for point_index in cluster_points:
                b9 = points[point_index]
                b10 = b4[i]
                b8.line((b9[0], b9[1], b10[0], b10[1]), b11 = b1[i])
    if b4:
        for i, b10 in enumerate(b4):
            draw_point(b8, b10, b1[i], b12 = a1)
    for b9 in points:
        draw_point(b8, b9, POINT_COLOR)
    img.save(b3)
q,