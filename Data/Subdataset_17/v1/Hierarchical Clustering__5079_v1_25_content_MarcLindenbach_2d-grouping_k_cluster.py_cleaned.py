import random
from PIL import Image, ImageDraw
COLOURS = [
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
def p_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
def generate_points(n=100, size=(400, 400)):
    return [(random.randint(0, size[0]), random.randint(0, size[1])) for _ in range(n)]
def render_k(points, clusters=None, best_matches=None, file_name='cluster.jpeg'):
    img, draw = create_image()
    if best_matches:
        for i, matches in enumerate(best_matches):
            for match in matches:
                x1, y1 = points[match]
                x2, y2 = clusters[i]
                draw.line((x1, y1, x2, y2), fill=COLOURS[i])
    if clusters:
        for i, cluster in enumerate(clusters):
            draw_point(draw, cluster, COLOURS[i], size=CLUSTER_POINT_SIZE)
    for point in points:
        draw_point(draw, point, POINT_COLOR)
    img.save(file_name)
def k_cluster(points, k=6, distance=p_distance, file_name='k-iteration-%d.jpeg'):
    render_k(points, file_name=file_name % 0)
    clusters = generate_points(n=k)
    last_matches = None
    for iter in range(1, 100):
        print(f'Iteration {iter}...')
        best_matches = [[] for _ in range(k)]
        for i, point in enumerate(points):
            best_match = min(range(k), key=lambda j: distance(clusters[j], point))
            best_matches[best_match].append(i)
        if best_matches == last_matches:
            break
        last_matches = best_matches
        render_k(points, clusters=clusters, best_matches=best_matches, file_name=file_name % iter)
        for i, cluster in enumerate(clusters):
            if best_matches[i]:
                clusters[i] = [
                    sum(points[j][0] for j in best_matches[i]) / len(best_matches[i]),
                    sum(points[j][1] for j in best_matches[i]) / len(best_matches[i])
                ]
    return clusters
def main():
    points = generate_points(n=100)
    k_cluster(points, k=6)
if __name__ == "__main__":
    main()