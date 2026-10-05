from PIL import Image, ImageDraw
import random
COLOURS = [
    (255, 127, 39),
    (34, 177, 76),
    (0, 162, 232),
    (163, 73, 164),
    (255, 242, 0),
    (63, 72, 204),
]
CLUSTER_POINT_SIZE = 8
POINT_COLOR = (0, 0, 0)
def create_image():
    img = Image.new('RGB', (500, 500), color='white')
    draw = ImageDraw.Draw(img)
    return img, draw
def draw_point(draw, point, color, size=1):
    x, y = point
    draw.ellipse((x - size, y - size, x + size, y + size), fill=color)
def euclidean_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
def generate_points(n=100):
    return [(random.randint(0, 500), random.randint(0, 500)) for _ in range(n)]
def k_means(points, k=6, distance=euclidean_distance, file_name='k-iteration-%d.jpeg'):
    render_clusters(points, file_name=file_name % 0)
    clusters = generate_points(n=k)
    last_matches = None
    for iteration in range(1, 100):
        print('Iteration %d...' % iteration)
        best_matches = [[] for _ in range(k)]
        for i, point in enumerate(points):
            best_match = min(range(k), key=lambda j: distance(clusters[j], point))
            best_matches[best_match].append(i)
        if last_matches == best_matches:
            break
        last_matches = best_matches
        render_clusters(points, clusters=clusters, best_matches=best_matches, file_name=file_name % iteration)
        for i in range(k):
            cluster_points = [points[idx] for idx in best_matches[i]]
            if cluster_points:
                clusters[i] = [sum(coord) / len(cluster_points) for coord in zip(*cluster_points)]
    return clusters
def render_clusters(points, clusters=None, best_matches=None, file_name='cluster.jpeg'):
    img, draw = create_image()
    if best_matches:
        for i, match in enumerate(best_matches):
            for j in match:
                x1, y1 = points[j]
                x2, y2 = clusters[i]
                draw.line((x1, y1, x2, y2), fill=COLOURS[i])
    if clusters:
        for i, cluster in enumerate(clusters):
            draw_point(draw, cluster, COLOURS[i], size=CLUSTER_POINT_SIZE)
    for point in points:
        draw_point(draw, point, POINT_COLOR)
    img.save(file_name)
if __name__ == "__main__":
    points = generate_points()
    clusters = k_means(points)
    render_clusters(points, clusters=clusters)