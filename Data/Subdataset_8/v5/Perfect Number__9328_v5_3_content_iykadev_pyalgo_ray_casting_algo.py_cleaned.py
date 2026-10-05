from collections import namedtuple
from pprint import pprint
import sys
Point = namedtuple('Point', 'x, y')
Edge = namedtuple('Edge', 'start, end')
Polygon = namedtuple('Polygon', 'name, edges')
EPSILON = 0.00001
HUGE = sys.float_info.max
TINY = sys.float_info.min
def ray_intersects_segment(point, edge):
    start, end = edge
    if start.y > end.y:
        start, end = end, start
    if point.y == start.y or point.y == end.y:
        point = Point(point.x, point.y + EPSILON)
    if (point.y > end.y or point.y < start.y) or (point.x > max(start.x, end.x)):
        return False
    if point.x < min(start.x, end.x):
        return True
    if abs(start.x - end.x) > TINY:
        slope_red = (end.y - start.y) / float(end.x - start.x)
    else:
        slope_red = HUGE
    if abs(start.x - point.x) > TINY:
        slope_blue = (point.y - start.y) / float(point.x - start.x)
    else:
        slope_blue = HUGE
    return slope_blue >= slope_red
def is_point_inside_polygon(point, polygon):
    num_edges = len(polygon.edges)
    return sum(ray_intersects_segment(point, edge) for edge in polygon.edges) % 2 == 1
def print_polygon(polygon):
    print(f"\nPolygon(name='{polygon.name}', edges=(")
    pprint(polygon.edges, indent=4)
    print("))")
if __name__ == '__main__':
    polygons = [
        Polygon(name='square', edges=(
            Edge(start=Point(x=0, y=0), end=Point(x=10, y=0)),
            Edge(start=Point(x=10, y=0), end=Point(x=10, y=10)),
            Edge(start=Point(x=10, y=10), end=Point(x=0, y=10)),
            Edge(start=Point(x=0, y=10), end=Point(x=0, y=0))
        )),
        Polygon(name='square_hole', edges=(
            Edge(start=Point(x=0, y=0), end=Point(x=10, y=0)),
            Edge(start=Point(x=10, y=0), end=Point(x=10, y=10)),
            Edge(start=Point(x=10, y=10), end=Point(x=0, y=10)),
            Edge(start=Point(x=0, y=10), end=Point(x=0, y=0)),
            Edge(start=Point(x=2.5, y=2.5), end=Point(x=7.5, y=2.5)),
            Edge(start=Point(x=7.5, y=2.5), end=Point(x=7.5, y=7.5)),
            Edge(start=Point(x=7.5, y=7.5), end=Point(x=2.5, y=7.5)),
            Edge(start=Point(x=2.5, y=7.5), end=Point(x=2.5, y=2.5))
        )),
        Polygon(name='strange', edges=(
            Edge(start=Point(x=0, y=0), end=Point(x=2.5, y=2.5)),
            Edge(start=Point(x=2.5, y=2.5), end=Point(x=0, y=10)),
            Edge(start=Point(x=0, y=10), end=Point(x=2.5, y=7.5)),
            Edge(start=Point(x=2.5, y=7.5), end=Point(x=7.5, y=7.5)),
            Edge(start=Point(x=7.5, y=7.5), end=Point(x=10, y=10)),
            Edge(start=Point(x=10, y=10), end=Point(x=10, y=0)),
            Edge(start=Point(x=10, y=0), end=Point(x=2.5, y=2.5))
        )),
        Polygon(name='exagon', edges=(
            Edge(start=Point(x=3, y=0), end=Point(x=7, y=0)),
            Edge(start=Point(x=7, y=0), end=Point(x=10, y=5)),
            Edge(start=Point(x=10, y=5), end=Point(x=7, y=10)),
            Edge(start=Point(x=7, y=10), end=Point(x=3, y=10)),
            Edge(start=Point(x=3, y=10), end=Point(x=0, y=5)),
            Edge(start=Point(x=0, y=5), end=Point(x=3, y=0))
        )),
    ]
    test_points = [
        Point(x=5, y=5), Point(x=5, y=8),
        Point(x=-10, y=5), Point(x=0, y=5),
        Point(x=10, y=5), Point(x=8, y=5),
        Point(x=10, y=10)
    ]
    print("\nTESTING WHETHER POINTS ARE WITHIN POLYGONS")
    for poly in polygons:
        print_polygon(poly)
        for p in test_points:
            print(f"   {p}: {is_point_inside_polygon(p, poly)}")