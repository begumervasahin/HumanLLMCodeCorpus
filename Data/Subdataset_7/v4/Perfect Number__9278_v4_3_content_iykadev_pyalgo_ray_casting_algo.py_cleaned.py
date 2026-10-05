from collections import namedtuple
from pprint import pprint
import sys
b1 = namedtuple('b1', 'b20, b7')
b2 = namedtuple('b2', 'b18, b6')
b3 = namedtuple('b3', 'b14, edges')
a1 = 0.00001
b4 = sys.float_info.max
b5 = sys.float_info.min
def fonk1(b8, edge):
    b18, b6 = edge
    if b18.b7 > b6.b7:
        b18, b6 = b6, b18
    if b8.b7 = = b18.b7 or b8.b7 == b6.b7:
        b8 = b1(b8.b20, b8.b7 + a1)
    b9 = False
    if (b8.b7 > b6.b7 or b8.b7 < b18.b7) or (b8.b20 > max(b18.b20, b6.b20)):
        return False
    if b8.b20 < min(b18.b20, b6.b20):
        b9 = True
    else:
        if abs(b18.b20 - b6.b20) > b5:
            b10 = (b6.b7 - b18.b7) / float(b6.b20 - b18.b20)
        else:
            b10 = b4
        if abs(b18.b20 - b8.b20) > b5:
            b11 = (b8.b7 - b18.b7) / float(b8.b20 - b18.b20)
        else:
            b11 = b4
        b9 = b11 >= b10
    return b9
def fonk2(b8, polygon):
    b12 = len(polygon)
    return sum(fonk1(b8, edge) for edge in polygon.edges) % b13 = = 1
def fonk3(polygon):
    print(f"\nPolygon(b14 = '{polygon.b14}', edges=(")
    pprint(polygon.edges, b15 = 4)
    print("))")
if b16 = = '__main__':
    b17 = [
        b3(b14 = 'square', edges=(
            b2(b18 = b1(b20=0, b7=0), b6=b1(b20=10, b7=0)),
            b2(b18 = b1(b20=10, b7=0), b6=b1(b20=10, b7=10)),
            b2(b18 = b1(b20=10, b7=10), b6=b1(b20=0, b7=10)),
            b2(b18 = b1(b20=0, b7=10), b6=b1(b20=0, b7=0))
        )),
        b3(b14 = 'square_hole', edges=(
            b2(b18 = b1(b20=0, b7=0), b6=b1(b20=10, b7=0)),
            b2(b18 = b1(b20=10, b7=0), b6=b1(b20=10, b7=10)),
            b2(b18 = b1(b20=10, b7=10), b6=b1(b20=0, b7=10)),
            b2(b18 = b1(b20=0, b7=10), b6=b1(b20=0, b7=0)),
            b2(b18 = b1(b20=b13.5, b7=b13.5), b6=b1(b20=7.5, b7=b13.5)),
            b2(b18 = b1(b20=7.5, b7=b13.5), b6=b1(b20=7.5, b7=7.5)),
            b2(b18 = b1(b20=7.5, b7=7.5), b6=b1(b20=b13.5, b7=7.5)),
            b2(b18 = b1(b20=b13.5, b7=7.5), b6=b1(b20=b13.5, b7=b13.5))
        )),
        b3(b14 = 'strange', edges=(
            b2(b18 = b1(b20=0, b7=0), b6=b1(b20=b13.5, b7=b13.5)),
            b2(b18 = b1(b20=b13.5, b7=b13.5), b6=b1(b20=0, b7=10)),
            b2(b18 = b1(b20=0, b7=10), b6=b1(b20=b13.5, b7=7.5)),
            b2(b18 = b1(b20=b13.5, b7=7.5), b6=b1(b20=7.5, b7=7.5)),
            b2(b18 = b1(b20=7.5, b7=7.5), b6=b1(b20=10, b7=10)),
            b2(b18 = b1(b20=10, b7=10), b6=b1(b20=10, b7=0)),
            b2(b18 = b1(b20=10, b7=0), b6=b1(b20=b13.5, b7=b13.5))
        )),
        b3(b14 = 'exagon', edges=(
            b2(b18 = b1(b20=3, b7=0), b6=b1(b20=7, b7=0)),
            b2(b18 = b1(b20=7, b7=0), b6=b1(b20=10, b7=5)),
            b2(b18 = b1(b20=10, b7=5), b6=b1(b20=7, b7=10)),
            b2(b18 = b1(b20=7, b7=10), b6=b1(b20=3, b7=10)),
            b2(b18 = b1(b20=3, b7=10), b6=b1(b20=0, b7=5)),
            b2(b18 = b1(b20=0, b7=5), b6=b1(b20=3, b7=0))
        )),
    ]
    b19 = (b1(b20=5, b7=5), b1(b20=5, b7=8),
                   b1(b20 = -10, b7=5), b1(b20=0, b7=5),
                   b1(b20 = 10, b7=5), b1(b20=8, b7=5),
                   b1(b20 = 10, b7=10))
    print("\nTESTING WHETHER POINTS ARE WITHIN POLYGONS")
    for poly in b17:
        fonk3(poly)
        print('   ', '\t'.join("%s: %s" % (p, fonk2(p, poly)) for p in b19[:3]))
        print('   ', '\t'.join("%s: %s" % (p, fonk2(p, poly)) for p in b19[3:6]))
        print('   ', '\t'.join("%s: %s" % (p, fonk2(p, poly)) for p in b19[6:]))