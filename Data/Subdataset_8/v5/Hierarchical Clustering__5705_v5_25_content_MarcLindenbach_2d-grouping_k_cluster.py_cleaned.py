from cluster import *
COLOURS = [
    (255, 127, 39),
    (34, 177, 76),
    (0, 162, 232),
    (163, 73, 164),
    (255, 242, 0),
    (63, 72, 204),
]
CLUSTER_POINT_SIZE = 8
def k_cluster(points, k=6, distance=p_distance, file_name='k-iteration-%d.jpeg'):
    render_k(points, file_name=file_name % 0)
    clusters = generate_points(n=k)
    last_matches = None
    for iteration in range(1, 100):
        print(f'Iteration {iteration}...')
        best_matches = [[] for _ in range(k)]
        for i, point in enumerate(points):
            best_match = min(range(k), key=lambda j: distance(clusters[j], point))
            best_matches[best_match].append(i)
        if last_matches == best_matches:
            break
        last_matches = best_matches
        render_k(points, clusters=clusters, best_matches=best_matches, file_name=file_name % iteration)
        for i, cluster in enumerate(clusters):
            cluster_points = [points[idx] for idx in best_matches[i]]
            if cluster_points:
                avgs = [sum(coord) / len(cluster_points) for coord in zip(*cluster_points)]
                clusters[i] = avgs
    return clusters
def render_k(points, clusters=None, best_matches=None, file_name='cluster.jpeg'):
    img, draw = create_image()
    if best_matches:
        for i, matches in enumerate(best_matches):
            for j in matches:
                x1, y1 = points[j]
                x2, y2 = clusters[i]
                draw.line((x1, y1, x2, y2), fill=COLOURS[i])
    if clusters:
        for i, cluster in enumerate(clusters):
            draw_point(draw, cluster, COLOURS[i], size=CLUSTER_POINT_SIZE)
    for point in points:
        draw_point(draw, point, POINT_COLOR)
    img.save(file_name)