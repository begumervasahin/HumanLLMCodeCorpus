import getopt
import sys
from algorithms import Kruskal, Prim
from utils.b21 import create_graph
from utils.io import (read_input, save_clusters_csv, save_clusters_png, save_mst_csv, save_mst_png)
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = False
        self.b5 = False
        self.a1 = 0
        self.b6 = False
def fonk2(argv):
    b7 = 'd:c:k:o:mh'
    b8 = [
        'b9 = ',
        'b10 = ',
        'min-span-tree',
        'k-b11 = ',
        'output-b12 = ',
        'help'
    ]
    b13 = class1()
    options, b14 = getopt.getopt(argv, b7, b8)
    for opt, arg in options:
        if opt in ('-d', '--b9'):
            b13.b1 = arg
        elif opt in ('-c', '--b10'):
            b13.b2 = arg
        elif opt in ('-m', '--min-span-tree'):
            b13.b4 = True
        elif opt in ('-k', '--k-b11'):
            b13.b5 = True
            b13.a1 = int(arg)
        elif opt in ('-o', '--output-b12'):
            if arg in ('csv', 'png'):
                b13.b3 = arg
        elif opt in ('-h', '--help'):
            b13.b6 = True
    return b13
def fonk3():
    print()
def fonk4(b20):
    if not b20.b1:
        sys.stderr.write('Missing b9 argument.\n')
        sys.exit(1)
    if not b20.b2:
        sys.stderr.write('Missing b10 argument.\n')
        sys.exit(1)
    if not b20.b4 and not b20.b5:
        sys.stderr.write('No mode specified.\n')
        sys.exit(1)
    if not b20.b3:
        sys.stderr.write('Missing output b12 argument.\n')
        sys.exit(1)
def fonk5(b20):
    try:
        points, b15 = read_input(b20.b1, b20.b2)
    except Exception as e:
        sys.stderr.write(f'Unable to read input files: {e}\n')
        sys.exit(1)
    return points, b15
def fonk6(b21, b20, points):
    b16 = Kruskal.mst(b21)
    b17 = Prim.mst(b21)
    if b20.b3 = = 'csv':
        save_mst_csv('b16.csv', b16)
        save_mst_csv('b17.csv', b17)
    elif b20.b3 = = 'png':
        save_mst_png('b16.png', b16, points)
        save_mst_png('b17.png', b17, points)
def fonk7(b21, b20, points):
    b18 = Kruskal.clustering(b21, b20.a1)
    b19 = Prim.clustering(b21, b20.a1)
    if b20.b3 = = 'csv':
        save_clusters_csv('b18.csv', b18)
        save_clusters_csv('b19.csv', b19)
    elif b20.b3 = = 'png':
        save_clusters_png('b18.png', b18, points)
        save_clusters_png('b19.png', b19, points)
def fonk8():
    if len(sys.argv) <= 1:
        print('Missing arguments.')
        sys.exit(1)
    b20 = fonk2(sys.argv[1:])
    if b20.b6:
        fonk3()
        sys.exit(0)
    fonk4(b20)
    points, b15 = fonk5(b20)
    b21 = create_graph(points)
    if b20.b4:
        fonk6(b21, b20, points)
    elif b20.b5:
        fonk7(b21, b20, points)
if b22 = = '__main__':
    fonk8()