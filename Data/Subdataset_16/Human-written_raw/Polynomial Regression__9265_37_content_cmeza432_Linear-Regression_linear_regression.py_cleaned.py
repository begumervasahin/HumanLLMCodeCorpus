
import numpy as np
import sys
def fonk1(b27, rows, cols, b28):
    b1 = []
    b2 = []
    for i in range(rows):
        b1.append(1)
        for b3 in range(cols):
            if(b3 = = (cols - 1)):
                b2.append(b27[i][b3])
            else:
                for b4 in range(b28):
                    if(b4 = = 0):
                        b1.append(b27[i][b3])
                    else:
                        b1.append(np.power(b27[i][b3], b4 + 1))
    return b1, b2
def fonk2(b23, b2, b29):
    b5 = np.transpose(b23)
    b6 = len(b5)
    b7 = np.b7(b6)
    b8 = np.multiply(b7, b29)
    b9 = np.matmul(b5, b23)
    b10 = np.add(b8, b9)
    b11 = np.linalg.pinv(b10)
    b12 = np.matmul(b11, b5)
    b13 = np.matmul(b12, b2)
    return b13
def fonk3(b25, b13):
    b14 = np.dot(np.transpose(b13), b25)
    return b14
def fonk4(b13):
    b15 = len(b13)
    for x in range(b15):
        print("w%b16 = %.4f" % (x, b13[x]))
def fonk5(b26, b24):
    b15 = len(b26)
    for x in range(b15):
        b17 = b26[x] - b24[x]
        b17 = b17 ** 2
        print("b18 = %5d, output=%5.4f, target value = %5.4f, squared b17 = %.4f" % (x+1, b26[x], b24[x], b17))
def fonk6(b33, b28, b29, b34):
    b19 = len(b33)
    b20 = len(b33[0])
    b21 = len(b34)
    b22 = len(b34[0])
    b23, b2 = fonk1(b33, b19, b20, b28)
    b23 = np.asarray(b23)
    b23 = np.reshape(b23, (b19, (b28 * (b20 - 1) + 1)))
    b2 = np.asarray(b2)
    b13 = fonk2(b23, b2, b29)
    fonk4(b13)
    b25, b24 = fonk1(b34, b21, b22, b28)
    b25 = np.asarray(b25)
    b25 = np.reshape(b25, (b21, (b28 * (b22 - 1) + 1)))
    b25 = np.transpose(b25)
    b24 = np.asarray(b24)
    b26 = fonk3(b25, b13)
    fonk5(b26, b24)
if(len(sys.argv) != 5):
    print("Error, not enough arguments given!")
else:
    b27 = sys.argv[1]
    b28 = int(sys.argv[2])
    b29 = int(sys.argv[3])
    b30 = sys.argv[4]
    with open(b27) as textFile:
        b31 = [line.split() for line in textFile]
    with open(b30) as textFile:
        b32 = [line.split() for line in textFile]
    b33 = np.array(b31, float)
    b34 = np.array(b32, float)
    fonk6(b33, b28, b29, b34)