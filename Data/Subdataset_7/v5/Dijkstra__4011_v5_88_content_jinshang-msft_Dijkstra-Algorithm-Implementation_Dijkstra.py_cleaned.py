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
        b5 = b3.b5(line)
        for x in range(b1):
            b4[index][x] = int(b5.group(x + 1)))
    return b4
def fonk3(filename):
    with open(filename, 'r') as input_file:
        b6 = [line.strip() for line in input_file.readlines() if line.strip() != '0']
    return np.array(b6)
def fonk4(graph, b22, b23, output_filename):
    b7 = len(graph)
    with open(output_filename, 'w+') as output_file:
        for b8, b9 in zip(b22, b23):
            b8 = int(b8) - 1
            b9 = int(b9) - 1
            b10 = np.zeros(shape=(b7))
            b11 = np.array([b8])
            b12 = np.zeros(shape=(b7))
            while True:
                b13 = np.inf
                for i in b11:
                    for j in range(b7):
                        if j not in b11 and graph[int(i)][j] > 0:
                            if b12[int(i)] + graph[int(i)][j] < b13:
                                b13 = b12[int(i)] + graph[int(i)][j]
                                b14 = j
                                b15 = i
                b11 = np.append(b11, [b14], axis=0)
                b12[b14] = b12[int(b15)] + graph[int(b15)][b14]
                b10[b14] = b15
                if b9 in b11:
                    break
            b16 = np.array([b9])
            while b8 not in b16:
                b16 = np.append(b16, [b10[int(b16[-1])]], axis=0)
            output_file.write(str(b12[b9]) + '\n')
            b17 = len(b16) - 1
            while b17 >= 0:
                output_file.write(str(int(b16[-1]) + 1) + '\n')
                b16 = b16[:-1]
                b17 -= 1
            output_file.write('FFFF\n')
        output_file.write('0\n')
if b18 = = '__main__':
    b1, b19 = fonk1('Graph.dat')
    b20 = fonk2(b1, b19)
    b21 = fonk3('Input.dat')
    b22 = b21[::3]
    b23 = b21[1::3]
    fonk4(b20, b22, b23, '/Users/JcShang/Desktop/Output.dat')