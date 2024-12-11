from anytree import Node, RenderTree
from copy import deepcopy
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
def fonk1(path):
    b1 = []
    for l in open(path):
        b2 = l.strip().split()
        b1.append(b2)
    b1.reverse()
    return b1
def fonk2(b1):
    b3 = len(b1)
    assert (len(b1[0]) == 1)
    b4 = []
    b5 = []
    for b6 in range(b3):
        if b6 = = 0:
            b7 = Node(b1[0][0])
            b4.append([b7])
        else:
            b8 = len(b1[b6-1])
            b9 = len(b1[b6])
            assert (b9 = = b8 or b9 == 2 * b8)
            b2 = []
            if b9 = = b8:
                for j in range(b9):
                    b2.append(Node(b1[b6][j], b10 = b4[b6-1][j]))
                    if b6 = = b3 - 1:
                        b5.append((b6, j))
                b4.append(b2)
            elif b9 = = 2 * b8:
                for j in range(b9):
                    b2.append(Node(b1[b6][j], b10 = b4[b6-1][j/2]))
                    if b6 = = b3 - 1:
                        b5.append((b6, j))
                b4.append(b2)
            else:
                raise ValueError("Incorrect number of b1 in b2: %d" % (b6))
    return b4, b5
def fonk3(b4, b6, j):
    b11 = deepcopy(b4)
    b2 = b11[b6]
    b12 = b2[j]
    b12.b10 = None
    return b11
def fonk4(b4, b5, path):
    for b6, j in b5:
        b12 = b4[b6][j]
        if b12.is_leaf:
            if b12.is_root:
                b16.add(path + b12.name)
                if len(b16) % b13 = = 0:
                    print(len(b16))
                    sys.stdout.flush()
                if len(b16) % b14 = = 0:
                    for path in b16:
                        b17.write("{}\n".format(path))
                    b17.flush()
                    sys.exit(-1)
            else:
                b15 = deepcopy(b5)
                if len(b12.b10.children) == 1:
                    if len(b4[b6]) == len(b4[b6-1]):
                        b15.append((b6-1, j))
                    else:
                        b15.append((b6-1, j/2))
                b15.remove((b6,j))
                fonk4(fonk3(b4, b6, j), b15, path + b12.name)
def fonk5(b7):
    for pre, fill, b12 in RenderTree(b7):
        print("%s%s" % (pre, b12.name))
if len(sys.argv) != 4:
    print >> sys.stderr, "Usage: python generate.py [input_file] [output_file] [image_file]"
    sys.exit(-1)
b1 = fonk1(sys.argv[1])
b4, b5 = fonk2(b1)
b16 = set()
b17 = open(sys.argv[2], "w")
fonk4(b4, b5, "")
print("Input b4:")
fonk5(b4[0][0])
b16 = sorted(list(b16), reverse=True)
b16 = [ path[::-1] for path in b16 ]
print("\nPossible b16 written to {}\n".format(sys.argv[2]))
with open(sys.argv[2], "w") as b17:
    for path in b16:
        b17.write("{}\n".format(path))
b17.close()
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
b23 = np.asarray([map(int, list(e)) for e in b16])
b23 = 1 - b23
plt.imshow(b23, b22 = 'gray', interpolation='none')
plt.savefig(sys.argv[3], b24 = 'tight')