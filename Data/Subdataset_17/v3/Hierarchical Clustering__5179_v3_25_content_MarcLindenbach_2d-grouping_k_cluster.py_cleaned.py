import random
from PIL import Image, ImageDraw
CLUSTER_COLORS = [
    (255, 127, 39),
    (34, 177, 76),
    (0, 162, 232),
    (163, 73, 164),
    (255, 242, 0),
    (63, 72, 204)
]
POINT_SIZE = 3
CLUSTER_POINT_SIZE = 8
POINT_COLOR = (0, 0, 0)
def create_image(size=(400, 400)):
    image = Image.new('RGB', size, (255, 255, 255))
    draw = ImageDraw.Draw(image)
    return image, draw
def draw_point(draw, point, color, size=POINT_SIZE):
    x, y = point
    draw.ellipse([x - size, y - size, x + size, y + size], fill=color, outline=color)
def euclidean_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
def generate_random_points(num_points=100, size=(400, 400)):
    return [(random.randint(0, size[0]), random.randint(0, size[1])) for _ in range(num_points)]
def render_clusters(points, clusters=None, matches=None, file_name='cluster.jpeg'):
    image, draw = create_image()
    if matches:
        for cluster_index, cluster_points in enumerate(matches):
            for point_index in cluster_points:
                point = points[point_index]
                cluster_center = clusters[cluster_index]
                draw.line((point[0], point[1], cluster_center[0], cluster_center[1]), fill=CLUSTER_COLORS[cluster_index])
    if clusters:
        for cluster_index, cluster_center in enumerate(clusters):
            draw_point(draw, cluster_center, CLUSTER_COLORS[cluster_index], size=CLUSTER_POINT_SIZE)
    for point in points:
        draw_point(draw, point, POINT_COLOR)
    image.save(file_name)
def k_means_clustering(points, num_clusters=6, distance_func=euclidean_distance, file_template='k-iteration-%d.jpeg'):
    render_clusters(points, file_name=file_template % 0)
    clusters = generate_random_points(num_points=num_clusters)
    previous_matches = None
    for iteration in range(1, 100):
        print(f'Iteration {iteration}...')
        matches = [[] for _ in range(num_clusters)]
        for i, point in enumerate(points):
            best_cluster_index = min(range(num_clusters), key=lambda j: distance_func(clusters[j], point))
            matches[best_cluster_index].append(i)
        if matches == previous_matches:
            break
        previous_matches = matches
        render_clusters(points, clusters=clusters, matches=matches, file_name=file_template % iteration)
        for i, cluster_points in enumerate(matches):
            if cluster_points:
                clusters[i] = [
                    sum(points[j][0] for j in cluster_points) / len(cluster_points),
                    sum(points[j][1] for j in cluster_points) / len(cluster_points)
                ]
    return clusters
def main():
    points = generate_random_points(num_points=100)
    k_means_clustering(points, num_clusters=6)
if __name__ == "__main__":
    main()