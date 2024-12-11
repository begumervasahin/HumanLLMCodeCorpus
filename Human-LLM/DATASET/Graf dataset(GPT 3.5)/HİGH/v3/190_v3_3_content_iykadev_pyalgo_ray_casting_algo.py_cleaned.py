from collections import namedtuple
import sys
b1 = namedtuple('b1', ['b18', 'y'])
b2 = namedtuple('b2', ['b16', 'b6'])
b3 = namedtuple('b3', ['b13', 'edges'])
a1 = 0.00001
b4 = sys.float_info.max
b5 = sys.float_info.min
def fonk1(b7, edge):
    '''
    Determines whether a ray cast from a b7 b8 with a given edge segment.
    '''
    b16, b6 = edge
    if b16.y > b6.y:
        b16, b6 = b6, b16
    if b7.y in {b16.y, b6.y}:
        b7 = b1(b7.b18, b7.y + a1)
    b8 = False
    if (b7.y > b6.y or b7.y < b16.y) or (b7.b18 > max(b16.b18, b6.b18)):
        return False
    if b7.b18 < min(b16.b18, b6.b18):
        b8 = True
    else:
        if abs(b16.b18 - b6.b18) > b5:
            b9 = (b6.y - b16.y) / float(b6.b18 - b16.b18)
        else:
            b9 = b4
        if abs(b16.b18 - b7.b18) > b5:
            b10 = (b7.y - b16.y) / float(b7.b18 - b16.b18)
        else:
            b10 = b4
        b8 = b10 >= b9
    return b8
def fonk2(b7, polygon):
    '''
    Determines whether a b7 lies inside a polygon.
    '''
    b11 = len(polygon)
    return sum(fonk1(b7, edge) for edge in polygon.edges) % b12 = = 1
def fonk3(polygon):
    '''
    Prints the details of a polygon.
    '''
    print(f"\nPolygon(b13 = '{polygon.b13}', edges=(")
    for edge in polygon.edges:
        print(f'    {edge},')
    print('))')
if b14 = = '__main__':
    b15 = [
        b3(b13 = 'square', edges=(
            b2(b16 = b1(b18=0, y=0), b6=b1(b18=10, y=0)),
            b2(b16 = b1(b18=10, y=0), b6=b1(b18=10, y=10)),
            b2(b16 = b1(b18=10, y=10), b6=b1(b18=0, y=10)),
            b2(b16 = b1(b18=0, y=10), b6=b1(b18=0, y=0))
        )),
        b3(b13 = 'square_hole', edges=(
            b2(b16 = b1(b18=0, y=0), b6=b1(b18=10, y=0)),
            b2(b16 = b1(b18=10, y=0), b6=b1(b18=10, y=10)),
            b2(b16 = b1(b18=10, y=10), b6=b1(b18=0, y=10)),
            b2(b16 = b1(b18=0, y=10), b6=b1(b18=0, y=0)),
            b2(b16 = b1(b18=b12.5, y=b12.5), b6=b1(b18=7.5, y=b12.5)),
            b2(b16 = b1(b18=7.5, y=b12.5), b6=b1(b18=7.5, y=7.5)),
            b2(b16 = b1(b18=7.5, y=7.5), b6=b1(b18=b12.5, y=7.5)),
            b2(b16 = b1(b18=b12.5, y=7.5), b6=b1(b18=b12.5, y=b12.5))
        )),
        b3(b13 = 'strange', edges=(
            b2(b16 = b1(b18=0, y=0), b6=b1(b18=b12.5, y=b12.5)),
            b2(b16 = b1(b18=b12.5, y=b12.5), b6=b1(b18=0, y=10)),
            b2(b16 = b1(b18=0, y=10), b6=b1(b18=b12.5, y=7.5)),
            b2(b16 = b1(b18=b12.5, y=7.5), b6=b1(b18=7.5, y=7.5)),
            b2(b16 = b1(b18=7.5, y=7.5), b6=b1(b18=10, y=10)),
            b2(b16 = b1(b18=10, y=10), b6=b1(b18=10, y=0)),
            b2(b16 = b1(b18=10, y=0), b6=b1(b18=b12.5, y=b12.5))
        )),
        b3(b13 = 'hexagon', edges=(
            b2(b16 = b1(b18=3, y=0), b6=b1(b18=7, y=0)),
            b2(b16 = b1(b18=7, y=0), b6=b1(b18=10, y=5)),
            b2(b16 = b1(b18=10, y=5), b6=b1(b18=7, y=10)),
            b2(b16 = b1(b18=7, y=10), b6=b1(b18=3, y=10)),
            b2(b16 = b1(b18=3, y=10), b6=b1(b18=0, y=5)),
            b2(b16 = b1(b18=0, y=5), b6=b1(b18=3, y=0))
        )),
    ]
    b17 = (
        b1(b18 = 5, y=5), b1(b18=5, y=8),
        b1(b18 = -10, y=5), b1(b18=0, y=5),
        b1(b18 = 10, y=5), b1(b18=8, y=5),
        b1(b18 = 10, y=10)
    )
    print("\nTESTING WHETHER POINTS ARE WITHIN POLYGONS")
    for poly in b15:
        fonk3(poly)
        print('   ', '\t'.join(f"{p}: {fonk2(p, poly)}" for p in b17[:3]))
        print('   ', '\t'.join(f"{p}: {fonk2(p, poly)}" for p in b17[3:6]))
        print('   ', '\t'.join(f"{p}: {fonk2(p, poly)}" for p in b17[6:]))