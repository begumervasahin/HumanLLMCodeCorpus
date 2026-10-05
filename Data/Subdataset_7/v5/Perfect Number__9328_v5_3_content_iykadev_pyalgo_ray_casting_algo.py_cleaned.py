from collections import namedtuple
from pprint import pprint
import sys
b1 = namedtuple('b1', 'b19, b7')
b2 = namedtuple('b2', 'b17, b6')
b3 = namedtuple('b3', 'b13, edges')
a1 = 0.00001
b4 = sys.float_info.max
b5 = sys.float_info.min
def fonk1(b8, edge):
    b17, b6 = edge
    if b17.b7 > b6.b7:
        b17, b6 = b6, b17
    if b8.b7 = = b17.b7 or b8.b7 == b6.b7:
        b8 = b1(b8.b19, b8.b7 + a1)
    if (b8.b7 > b6.b7 or b8.b7 < b17.b7) or (b8.b19 > max(b17.b19, b6.b19)):
        return False
    if b8.b19 < min(b17.b19, b6.b19):
        return True
    if abs(b17.b19 - b6.b19) > b5:
        b9 = (b6.b7 - b17.b7) / float(b6.b19 - b17.b19)
    else:
        b9 = b4
    if abs(b17.b19 - b8.b19) > b5:
        b10 = (b8.b7 - b17.b7) / float(b8.b19 - b17.b19)
    else:
        b10 = b4
    return b10 >= b9
def fonk2(b8, polygon):
    b11 = len(polygon.edges)
    return sum(fonk1(b8, edge) for edge in polygon.edges) % b12 = = 1
def fonk3(polygon):
    print(f"\nPolygon(b13 = '{polygon.b13}', edges=(")
    pprint(polygon.edges, b14 = 4)
    print("))")
if b15 = = '__main__':
    b16 = [
        b3(b13 = 'square', edges=(
            b2(b17 = b1(b19=0, b7=0), b6=b1(b19=10, b7=0)),
            b2(b17 = b1(b19=10, b7=0), b6=b1(b19=10, b7=10)),
            b2(b17 = b1(b19=10, b7=10), b6=b1(b19=0, b7=10)),
            b2(b17 = b1(b19=0, b7=10), b6=b1(b19=0, b7=0))
        )),
        b3(b13 = 'square_hole', edges=(
            b2(b17 = b1(b19=0, b7=0), b6=b1(b19=10, b7=0)),
            b2(b17 = b1(b19=10, b7=0), b6=b1(b19=10, b7=10)),
            b2(b17 = b1(b19=10, b7=10), b6=b1(b19=0, b7=10)),
            b2(b17 = b1(b19=0, b7=10), b6=b1(b19=0, b7=0)),
            b2(b17 = b1(b19=b12.5, b7=b12.5), b6=b1(b19=7.5, b7=b12.5)),
            b2(b17 = b1(b19=7.5, b7=b12.5), b6=b1(b19=7.5, b7=7.5)),
            b2(b17 = b1(b19=7.5, b7=7.5), b6=b1(b19=b12.5, b7=7.5)),
            b2(b17 = b1(b19=b12.5, b7=7.5), b6=b1(b19=b12.5, b7=b12.5))
        )),
        b3(b13 = 'strange', edges=(
            b2(b17 = b1(b19=0, b7=0), b6=b1(b19=b12.5, b7=b12.5)),
            b2(b17 = b1(b19=b12.5, b7=b12.5), b6=b1(b19=0, b7=10)),
            b2(b17 = b1(b19=0, b7=10), b6=b1(b19=b12.5, b7=7.5)),
            b2(b17 = b1(b19=b12.5, b7=7.5), b6=b1(b19=7.5, b7=7.5)),
            b2(b17 = b1(b19=7.5, b7=7.5), b6=b1(b19=10, b7=10)),
            b2(b17 = b1(b19=10, b7=10), b6=b1(b19=10, b7=0)),
            b2(b17 = b1(b19=10, b7=0), b6=b1(b19=b12.5, b7=b12.5))
        )),
        b3(b13 = 'exagon', edges=(
            b2(b17 = b1(b19=3, b7=0), b6=b1(b19=7, b7=0)),
            b2(b17 = b1(b19=7, b7=0), b6=b1(b19=10, b7=5)),
            b2(b17 = b1(b19=10, b7=5), b6=b1(b19=7, b7=10)),
            b2(b17 = b1(b19=7, b7=10), b6=b1(b19=3, b7=10)),
            b2(b17 = b1(b19=3, b7=10), b6=b1(b19=0, b7=5)),
            b2(b17 = b1(b19=0, b7=5), b6=b1(b19=3, b7=0))
        )),
    ]
    b18 = [
        b1(b19 = 5, b7=5), b1(b19=5, b7=8),
        b1(b19 = -10, b7=5), b1(b19=0, b7=5),
        b1(b19 = 10, b7=5), b1(b19=8, b7=5),
        b1(b19 = 10, b7=10)
    ]
    print("\nTESTING WHETHER POINTS ARE WITHIN POLYGONS")
    for poly in b16:
        fonk3(poly)
        for p in b18:
            print(f"   {p}: {fonk2(p, poly)}")