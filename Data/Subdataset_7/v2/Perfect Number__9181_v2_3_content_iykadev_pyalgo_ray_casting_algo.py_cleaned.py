from collections import namedtuple
import sys
b1 = namedtuple('b1', 'b19, b7')
b2 = namedtuple('b2', 'b17, b6')
b3 = namedtuple('b3', 'b14, edges')
a1 = 0.00001
b4 = sys.float_info.max
b5 = sys.float_info.min
def fonk1(b8, edge):
    '''
    Determines whether a ray cast from a b8 b9 with a given edge segment.
    '''
    b17, b6 = edge
    if b17.b7 > b6.b7:
        b17, b6 = b6, b17
    if b8.b7 = = b17.b7 or b8.b7 == b6.b7:
        b8 = b1(b8.b19, b8.b7 + a1)
    b9 = False
    if (b8.b7 > b6.b7 or b8.b7 < b17.b7) or (b8.b19 > max(b17.b19, b6.b19)):
        return False
    if b8.b19 < min(b17.b19, b6.b19):
        b9 = True
    else:
        if abs(b17.b19 - b6.b19) > b5:
            b10 = (b6.b7 - b17.b7) / float(b6.b19 - b17.b19)
        else:
            b10 = b4
        if abs(b17.b19 - b8.b19) > b5:
            b11 = (b8.b7 - b17.b7) / float(b8.b19 - b17.b19)
        else:
            b11 = b4
        b9 = b11 >= b10
    return b9
def fonk2(b8, polygon):
    '''
    Determines whether a b8 lies inside a polygon.
    '''
    b12 = len(polygon)
    return sum(fonk1(b8, edge) for edge in polygon.edges) % b13 = = 1
def fonk3(polygon):
    '''
    Prints the details of a polygon.
    '''
    print("\n  b3(b14 = '%s', edges=(" % polygon.b14)
    print('   ', ',\n    '.join(str(edge) for edge in polygon.edges) + '\n    ))')
if b15 = = '__main__':
    b16 = [
        b3(b14 = 'square', edges=(
            b2(b17 = b1(b19=0, b7=0), b6=b1(b19=10, b7=0)),
            b2(b17 = b1(b19=10, b7=0), b6=b1(b19=10, b7=10)),
            b2(b17 = b1(b19=10, b7=10), b6=b1(b19=0, b7=10)),
            b2(b17 = b1(b19=0, b7=10), b6=b1(b19=0, b7=0))
        )),
        b3(b14 = 'square_hole', edges=(
            b2(b17 = b1(b19=0, b7=0), b6=b1(b19=10, b7=0)),
            b2(b17 = b1(b19=10, b7=0), b6=b1(b19=10, b7=10)),
            b2(b17 = b1(b19=10, b7=10), b6=b1(b19=0, b7=10)),
            b2(b17 = b1(b19=0, b7=10), b6=b1(b19=0, b7=0)),
            b2(b17 = b1(b19=b13.5, b7=b13.5), b6=b1(b19=7.5, b7=b13.5)),
            b2(b17 = b1(b19=7.5, b7=b13.5), b6=b1(b19=7.5, b7=7.5)),
            b2(b17 = b1(b19=7.5, b7=7.5), b6=b1(b19=b13.5, b7=7.5)),
            b2(b17 = b1(b19=b13.5, b7=7.5), b6=b1(b19=b13.5, b7=b13.5))
        )),
        b3(b14 = 'strange', edges=(
            b2(b17 = b1(b19=0, b7=0), b6=b1(b19=b13.5, b7=b13.5)),
            b2(b17 = b1(b19=b13.5, b7=b13.5), b6=b1(b19=0, b7=10)),
            b2(b17 = b1(b19=0, b7=10), b6=b1(b19=b13.5, b7=7.5)),
            b2(b17 = b1(b19=b13.5, b7=7.5), b6=b1(b19=7.5, b7=7.5)),
            b2(b17 = b1(b19=7.5, b7=7.5), b6=b1(b19=10, b7=10)),
            b2(b17 = b1(b19=10, b7=10), b6=b1(b19=10, b7=0)),
            b2(b17 = b1(b19=10, b7=0), b6=b1(b19=b13.5, b7=b13.5))
        )),
        b3(b14 = 'hexagon', edges=(
            b2(b17 = b1(b19=3, b7=0), b6=b1(b19=7, b7=0)),
            b2(b17 = b1(b19=7, b7=0), b6=b1(b19=10, b7=5)),
            b2(b17 = b1(b19=10, b7=5), b6=b1(b19=7, b7=10)),
            b2(b17 = b1(b19=7, b7=10), b6=b1(b19=3, b7=10)),
            b2(b17 = b1(b19=3, b7=10), b6=b1(b19=0, b7=5)),
            b2(b17 = b1(b19=0, b7=5), b6=b1(b19=3, b7=0))
        )),
    ]
    b18 = (
        b1(b19 = 5, b7=5), b1(b19=5, b7=8),
        b1(b19 = -10, b7=5), b1(b19=0, b7=5),
        b1(b19 = 10, b7=5), b1(b19=8, b7=5),
        b1(b19 = 10, b7=10)
    )
    print("\n TESTING WHETHER POINTS ARE WITHIN POLYGONS")
    for poly in b16:
        fonk3(poly)
        print('   ', '\t'.join("%s: %s" % (p, fonk2(p, poly)) for p in b18[:3]))
        print('   ', '\t'.join("%s: %s" % (p, fonk2(p, poly)) for p in b18[3:6]))
        print('   ', '\t'.join("%s: %s" % (p, fonk2(p, poly)) for p in b18[6:]))