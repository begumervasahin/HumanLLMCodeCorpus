import sys
import getopt
from algorithms import Kruskal, Prim
from utils.b17 import create_graph
from utils.io import read_input, save_clusters_csv, save_clusters_png, save_mst_csv, save_mst_png
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
    try:
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
    except getopt.GetoptError as e:
        print(f"Error parsing arguments: {e}")
        b13.b6 = True
    return b13
def fonk3():
    print()
def fonk4(b15):
    if not b15.b1:
        sys.stderr.write('Missing b9 argument.\n')
        sys.exit(1)
    if not b15.b2:
        sys.stderr.write('Missing b10 argument.\n')
        sys.exit(1)
    if not b15.b4 and not b15.b5:
        sys.stderr.write('No mode specified.\n')
        sys.exit(1)
    if not b15.b3:
        sys.stderr.write('Missing output b12 argument.\n')
        sys.exit(1)
def fonk5(argv):
    b15 = fonk2(argv)
    if b15.b6:
        fonk3()
        sys.exit(0)
    fonk4(b15)
    try:
        points, b16 = read_input(b15.b1, b15.b2)
    except Exception as e:
        sys.stderr.write(f'Unable to read input files: {str(e)}\n')
        sys.exit(1)
    b17 = create_graph(points)
    if b15.b4:
        fonk6(b15, b17, points)
    elif b15.b5:
        fonk7(b15, b17, points)
def fonk6(b15, b17, points):
    b18 = Kruskal.mst(b17)
    b19 = Prim.mst(b17)
    if b15.b3 = = 'csv':
        save_mst_csv('b18.csv', b18)
        save_mst_csv('b19.csv', b19)
    elif b15.b3 = = 'png':
        save_mst_png('b18.png', b18, points)
        save_mst_png('b19.png', b19, points)
def fonk7(b15, b17, points):
    b20 = Kruskal.clustering(b17, b15.a1)
    b21 = Prim.clustering(b17, b15.a1)
    if b15.b3 = = 'csv':
        save_clusters_csv('b20.csv', b20)
        save_clusters_csv('b21.csv', b21)
    elif b15.b3 = = 'png':
        save_clusters_png('b20.png', b20, points)
        save_clusters_png('b21.png', b21, points)
if b22 = = '__main__':
    fonk5(sys.argv[1:])