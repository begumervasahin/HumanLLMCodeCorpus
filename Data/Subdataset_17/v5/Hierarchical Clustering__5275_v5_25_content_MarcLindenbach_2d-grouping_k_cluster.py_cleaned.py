from cluster import *
CLUSTER_COLORS = [
    (255, 127, 39),
    (34, 177, 76),
    (0, 162, 232),
    (163, 73, 164),
    (255, 242, 0),
    (63, 72, 204)
]
CLUSTER_POINT_SIZE = 8
def k_means_clustering(points, num_clusters=6, distance_func=p_distance, file_name_template='k-iteration-%d.jpeg'):
    render_clusters(points, file_name=file_name_template % 0)
    clusters = generate_points(n=num_clusters)
    previous_matches = None
    for iteration in range(1, 100):
        print(f'Iteration {iteration}...')
        best_matches = [[] for _ in range(num_clusters)]
        for i, point in enumerate(points):
            best_cluster = min(range(num_clusters), key=lambda j: distance_func(clusters[j], point))
            best_matches[best_cluster].append(i)
        if best_matches == previous_matches:
            break
        previous_matches = best_matches
        render_clusters(points, clusters=clusters, matches=best_matches, file_name=file_name_template % iteration)
        for i in range(len(clusters)):
            if best_matches[i]:
                clusters[i] = [
                    sum(points[j][0] for j in best_matches[i]) / len(best_matches[i]),
                    sum(points[j][1] for j in best_matches[i]) / len(best_matches[i])
                ]
    return clusters
def render_clusters(points, clusters=None, matches=None, file_name='cluster.jpeg'):
    img, draw = create_image()
    if matches and clusters:
        for i, cluster_points in enumerate(matches):
            for point_index in cluster_points:
                point = points[point_index]
                cluster_center = clusters[i]
                draw.line((point[0], point[1], cluster_center[0], cluster_center[1]), fill=CLUSTER_COLORS[i])
    if clusters:
        for i, cluster_center in enumerate(clusters):
            draw_point(draw, cluster_center, CLUSTER_COLORS[i], size=CLUSTER_POINT_SIZE)
    for point in points:
        draw_point(draw, point, POINT_COLOR)
    img.save(file_name)
def main():
    points = generate_points(n=100)
    k_means_clustering(points, num_clusters=6)
if __name__ == "__main__":
    main()