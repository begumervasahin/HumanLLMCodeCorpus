import random
from PIL import Image, ImageDraw
COLORS = [
    (255, 127, 39),
    (34, 177, 76),
    (0, 162, 232),
    (163, 73, 164),
    (255, 242, 0),
    (63, 72, 204)
]
CLUSTER_POINT_SIZE = 8
POINT_COLOR = (0, 0, 0)
def create_image(size=(400, 400)):
    img = Image.new('RGB', size, (255, 255, 255))
    draw = ImageDraw.Draw(img)
    return img, draw
def draw_point(draw, point, color, size=3):
    x, y = point
    draw.ellipse([x - size, y - size, x + size, y + size], fill=color, outline=color)
def euclidean_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
def generate_random_points(n=100, size=(400, 400)):
    return [(random.randint(0, size[0]), random.randint(0, size[1])) for _ in range(n)]
def render_clusters(points, clusters=None, matches=None, file_name='cluster.jpeg'):
    img, draw = create_image()
    if matches:
        for i, cluster_points in enumerate(matches):
            for match in cluster_points:
                x1, y1 = points[match]
                x2, y2 = clusters[i]
                draw.line((x1, y1, x2, y2), fill=COLORS[i])
    if clusters:
        for i, cluster in enumerate(clusters):
            draw_point(draw, cluster, COLORS[i], size=CLUSTER_POINT_SIZE)
    for point in points:
        draw_point(draw, point, POINT_COLOR)
    img.save(file_name)
def k_means_clustering(points, k=6, distance_func=euclidean_distance, file_template='k-iteration-%d.jpeg'):
    render_clusters(points, file_name=file_template % 0)
    clusters = generate_random_points(n=k)
    previous_matches = None
    for iteration in range(1, 100):
        print(f'Iteration {iteration}...')
        matches = [[] for _ in range(k)]
        for i, point in enumerate(points):
            best_cluster = min(range(k), key=lambda j: distance_func(clusters[j], point))
            matches[best_cluster].append(i)
        if matches == previous_matches:
            break
        previous_matches = matches
        render_clusters(points, clusters=clusters, matches=matches, file_name=file_template % iteration)
        for i, cluster in enumerate(clusters):
            if matches[i]:
                clusters[i] = [
                    sum(points[j][0] for j in matches[i]) / len(matches[i]),
                    sum(points[j][1] for j in matches[i]) / len(matches[i])
                ]
    return clusters
def main():
    points = generate_random_points(n=100)
    k_means_clustering(points, k=6)
if __name__ == "__main__":
    main()