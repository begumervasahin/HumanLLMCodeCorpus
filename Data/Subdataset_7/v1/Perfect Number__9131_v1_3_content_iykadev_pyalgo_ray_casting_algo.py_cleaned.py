from collections import namedtuple
import sys
b1 = namedtuple('b1', 'b19, b8')
b2 = namedtuple('b2', 'b17, b7')
b3 = namedtuple('b3', 'b14, edges')
a1 = 0.00001
b4 = sys.float_info.max
b5 = sys.float_info.min
def fonk1(b6, edge):
    '''
    Takes b17 point b6 = b1() and an edge of two endpoints b17,b7=b1() of b17 line segment.
    Returns boolean.
    '''
    b17, b7 = edge
    if b17.b8 > b7.b8:
        b17, b7 = b7, b17
    if b6.b8 = = b17.b8 or b6.b8 == b7.b8:
        b6 = b1(b6.b19, b6.b8 + a1)
    b9 = False
    if (b6.b8 > b7.b8 or b6.b8 < b17.b8) or (b6.b19 > max(b17.b19, b7.b19)):
        return False
    if b6.b19 < min(b17.b19, b7.b19):
        b9 = True
    else:
        if abs(b17.b19 - b7.b19) > b5:
            b10 = (b7.b8 - b17.b8) / float(b7.b19 - b17.b19)
        else:
            b10 = b4
        if abs(b17.b19 - b6.b19) > b5:
            b11 = (b6.b8 - b17.b8) / float(b6.b19 - b17.b19)
        else:
            b11 = b4
        b9 = b11 >= b10
    return b9
def fonk2(b19):
    return b19 % b12 = = 1
def fonk3(b6, poly):
    b13 = len(poly)
    return fonk2(sum(fonk1(b6, edge) for edge in poly.edges))
def fonk4(poly):
    print("\n  Polygon(b14 = '%s', edges=(" % poly.b14)
    print('   ', ',\n    '.join(str(e) for e in poly.edges) + '\n    ))')
if b15 = = '__main__':
    b16 = [
        b3(b14 = 'square', edges=(
            b2(b17 = b1(b19=0, b8=0), b7=b1(b19=10, b8=0)),
            b2(b17 = b1(b19=10, b8=0), b7=b1(b19=10, b8=10)),
            b2(b17 = b1(b19=10, b8=10), b7=b1(b19=0, b8=10)),
            b2(b17 = b1(b19=0, b8=10), b7=b1(b19=0, b8=0))
        )),
        b3(b14 = 'square_hole', edges=(
            b2(b17 = b1(b19=0, b8=0), b7=b1(b19=10, b8=0)),
            b2(b17 = b1(b19=10, b8=0), b7=b1(b19=10, b8=10)),
            b2(b17 = b1(b19=10, b8=10), b7=b1(b19=0, b8=10)),
            b2(b17 = b1(b19=0, b8=10), b7=b1(b19=0, b8=0)),
            b2(b17 = b1(b19=b12.5, b8=b12.5), b7=b1(b19=7.5, b8=b12.5)),
            b2(b17 = b1(b19=7.5, b8=b12.5), b7=b1(b19=7.5, b8=7.5)),
            b2(b17 = b1(b19=7.5, b8=7.5), b7=b1(b19=b12.5, b8=7.5)),
            b2(b17 = b1(b19=b12.5, b8=7.5), b7=b1(b19=b12.5, b8=b12.5))
        )),
        b3(b14 = 'strange', edges=(
            b2(b17 = b1(b19=0, b8=0), b7=b1(b19=b12.5, b8=b12.5)),
            b2(b17 = b1(b19=b12.5, b8=b12.5), b7=b1(b19=0, b8=10)),
            b2(b17 = b1(b19=0, b8=10), b7=b1(b19=b12.5, b8=7.5)),
            b2(b17 = b1(b19=b12.5, b8=7.5), b7=b1(b19=7.5, b8=7.5)),
            b2(b17 = b1(b19=7.5, b8=7.5), b7=b1(b19=10, b8=10)),
            b2(b17 = b1(b19=10, b8=10), b7=b1(b19=10, b8=0)),
            b2(b17 = b1(b19=10, b8=0), b7=b1(b19=b12.5, b8=b12.5))
        )),
        b3(b14 = 'exagon', edges=(
            b2(b17 = b1(b19=3, b8=0), b7=b1(b19=7, b8=0)),
            b2(b17 = b1(b19=7, b8=0), b7=b1(b19=10, b8=5)),
            b2(b17 = b1(b19=10, b8=5), b7=b1(b19=7, b8=10)),
            b2(b17 = b1(b19=7, b8=10), b7=b1(b19=3, b8=10)),
            b2(b17 = b1(b19=3, b8=10), b7=b1(b19=0, b8=5)),
            b2(b17 = b1(b19=0, b8=5), b7=b1(b19=3, b8=0))
        )),
    ]
    b18 = (
        b1(b19 = 5, b8=5), b1(b19=5, b8=8),
        b1(b19 = -10, b8=5), b1(b19=0, b8=5),
        b1(b19 = 10, b8=5), b1(b19=8, b8=5),
        b1(b19 = 10, b8=10)
    )
    print("\n TESTING WHETHER POINTS ARE WITHIN POLYGONS")
    for poly in b16:
        fonk4(poly)
        print('   ', '\t'.join("%s: %s" % (b6, fonk3(b6, poly)) for b6 in b18[:3]))
        print('   ', '\t'.join("%s: %s" % (b6, fonk3(b6, poly)) for b6 in b18[3:6]))
        print('   ', '\t'.join("%s: %s" % (b6, fonk3(b6, poly)) for b6 in b18[6:]))