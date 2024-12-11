import re
import numpy as np
def fonk1(filename):
    with open(filename, 'r') as graph_file:
        b1 = int(graph_file.readline())
        b2 = [graph_file.readline().strip() for _ in range(b1)]
    return b1, b2
def fonk2(b1, b2):
    b3 = ''.join([str(i) + '+' + '(.+)' for i in range(1, b1 + 1)])
    b3 = re.compile(b3)
    b4 = np.zeros(shape=(b1, b1))
    for index, line in enumerate(b2):
        b5 = b3.match(line)
        for x in range(b1):
            b4[index][x] = int(b5.group(x + 1))
    return b4
def fonk3(filename):
    with open(filename, 'r') as input_file:
        b6 = []
        for line in input_file:
            b7 = line.strip()
            if b7 = = '0':
                break
            b6.append(b7)
    return np.array(b6)
def fonk4(graph, b23, b24):
    b8 = len(graph)
    with open('Output.dat', 'w+') as output_file:
        for b9, b10 in zip(b23, b24):
            b9 = int(b9) - 1
            b10 = int(b10) - 1
            b11 = np.zeros(shape=(b8))
            b12 = np.array([b9])
            b13 = np.zeros(shape=(b8))
            while True:
                b14 = float('inf')
                for i in b12:
                    for j in range(b8):
                        if j not in b12 and graph[int(i)][j] > 0:
                            if b13[int(i)] + graph[int(i)][j] < b14:
                                b14 = b13[int(i)] + graph[int(i)][j]
                                b15 = j
                                b16 = i
                b12 = np.append(b12, [b15])
                b13[b15] = b13[int(b16)] + graph[int(b16)][b15]
                b11[b15] = b16
                if b10 in b12:
                    break
            b17 = np.array([b10])
            while b9 not in b17:
                b17 = np.append(b17, [b11[int(b17[-1])]])
            output_file.write(str(b13[b10]) + '\n')
            b18 = len(b17) - 1
            while b18 >= 0:
                output_file.write(str(int(b17[-1]) + 1) + '\n')
                b17 = b17[:-1]
                b18 -= 1
            output_file.write('FFFF\n')
        output_file.write('0\n')
if b19 = = '__main__':
    b1, b20 = fonk1('Graph.dat')
    b21 = fonk2(b1, b20)
    b22 = fonk3('Input.dat')
    b23 = b22[::3]
    b24 = b22[1::3]
    fonk4(b21, b23, b24)