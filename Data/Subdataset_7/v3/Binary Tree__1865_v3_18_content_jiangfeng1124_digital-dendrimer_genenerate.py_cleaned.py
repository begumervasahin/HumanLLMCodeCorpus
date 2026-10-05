from anytree import Node, RenderTree
from copy import deepcopy
import sys
import numpy as np
import matplotlib.pyplot as plt
def fonk1(path):
    b1 = []
    with open(path, 'r') as b23:
        for line in b23:
            b2 = line.strip().split()
            b1.append(b2)
    b1.reverse()
    return b1
def fonk2(b1):
    b3 = len(b1)
    assert len(b1[0]) == 1
    b4 = []
    b5 = []
    for b6 in range(b3):
        if b6 = = 0:
            b7 = Node(b1[0][0])
            b4.append([b7])
        else:
            b8 = len(b1[b6-1])
            b9 = len(b1[b6])
            assert b9 in (b8, 2 * b8)
            b2 = []
            for j in range(b9):
                b10 = j
                b2.append(Node(b1[b6][j], b11 = b4[b6-1][b10]))
                if b6 = = b3 - 1:
                    b5.append((b6, j))
            b4.append(b2)
    return b4, b5
def fonk3(b4, b6, j):
    b12 = deepcopy(b4)
    b12[b6][j].b11 = None
    return b12
def fonk4(b4, b5, path, fw):
    b13 = set()
    for b6, j in b5:
        b14 = b4[b6][j]
        if b14.is_leaf:
            if b14.is_root:
                b13.add(path + b14.name)
                if len(b13) % b15 = = 0:
                    print(len(b13))
                    sys.stdout.flush()
                if len(b13) % b16 = = 0:
                    for p in b13:
                        fw.write("{}\n".format(p))
                    fw.flush()
                    sys.exit(-1)
            else:
                b17 = deepcopy(b5)
                b10 = j
                b17.remove((b6,j))
                b17.append((b6-1, b10))
                fonk4(fonk3(b4, b6, j), b17, path + b14.name, fw)
def fonk5(b7):
    for pre, fill, b14 in RenderTree(b7):
        print("%s%s" % (pre, b14.name))
def fonk6(data, filename):
    b18 = np.shape(data)
    b19 = plt.figure()
    b20 = plt.Axes(b19, [0., 0., 1., 1.])
    b20.set_axis_off()
    b19.add_axes(b20)
    b21 = b20.imshow(data, interpolation='nearest')
    b21.set_cmap('gray')
    plt.savefig(filename, b22 = 'hot')
    plt.close()
if len(sys.argv) != 4:
    print("Usage: python generate.py [input_file] [output_file] [image_file]", b23 = sys.stderr)
    sys.exit(-1)
b1 = fonk1(sys.argv[1])
b4, b5 = fonk2(b1)
b13 = set()
with open(sys.argv[2], "w") as fw:
    fonk4(b4, b5, "", fw)
print("Input b4:")
fonk5(b4[0][0])
print("\nPossible b13 written to {}\n".format(sys.argv[2]))
b24 = np.asarray([list(map(int, list(e))) for e in b13])
b24 = 1 - b24
plt.imshow(b24, b22 = 'gray', interpolation='none')
plt.savefig(sys.argv[3], b25 = 'tight')