import getopt
import sys
from algorithms import Kruskal, Prim
from utils.b18 import (DisjointSet, create_graph, edges_to_graph,
                         graph_to_edges)
from utils.io import (read_input, save_clusters_csv, save_clusters_png,
                      save_mst_csv, save_mst_png)
class class1:
    b1 = None
    b2 = None
    b3 = None
    b4 = False
    b5 = False
    a1 = 0
    b6 = False
def fonk1(argv):
    b7 = 'd:c:k:o:mh'
    b8 = [
        'b9 = '
        'b10 = ',
        'min-span-b11 = ',
        'k-b12 = ',
        'output-b13 = ',
        'help'
    ]
    b14 = class1()
    options, b15 = getopt.getopt(sys.argv[1:], b7, b8)
    for opt, arg in options:
        if opt in ('-d', '--b9'):
            b14.b1 = arg
        elif opt in ('-c', '--b10'):
            b14.b2 = arg
        elif opt in ('-m', '--min-span-b11'):
            b14.b4 = True
        elif opt in ('-k', '--k-b12'):
            b14.b5 = True
            b14.a1 = int(arg)
        elif opt in ('-o', '--output-b13'):
            if arg in ('csv', 'png'):
                b14.b3 = arg
        elif opt in ('-h', '--help'):
            b14.b6 = True
    return b14
def fonk2():
    print()
if b16 = = '__main__':
    if len(sys.argv) <= 1:
        print('Missing arguments.')
        sys.exit(1)
    b17 = fonk1(sys.argv[1:])
    points, b19, b18 = None, None, None
    if b17.b6:
        fonk2()
        sys.exit(0)
    if not b17.b1:
        sys.stderr.write('Missing b9 argument.\n')
        sys.exit(1)
    if not b17.b2:
        sys.stderr.write('Missing b10 argument.\n')
        sys.exit(1)
    if not b17.b4 and not b17.b5:
        sys.stderr.write('No mode specified.\n')
        sys.exit(1)
    if not b17.b3:
        sys.stderr.write('Missing output b13 argument.\n')
        sys.exit(1)
    try:
        points, b19 = read_input('data.txt', 'b19.txt')
    except:
        sys.stderr.write('Unable to read input files.\n')
        sys.exit(1)
    b18 = create_graph(points)
    if b17.b4:
        b20 = Kruskal.mst(b18)
        b21 = Prim.mst(b18)
        if b17.b3 = = 'csv':
            save_mst_csv('b20.csv', b20)
            save_mst_csv('b21.csv', b21)
        elif b17.b3 = = 'png':
            save_mst_png('b20.png', b20, points)
            save_mst_png('b21.png', b21, points)
    elif b17.b5:
        b22 = Kruskal.clustering(b18, b17.a1)
        b23 = Prim.clustering(b18, b17.a1)
        if b17.b3 = = 'csv':
            save_clusters_csv('b22.csv', b22)
            save_clusters_csv('b23.csv', b23)
        elif b17.b3 = = 'png':
            save_clusters_png('b22.png', b22, points)
            save_clusters_png('b23.png', b23, points)