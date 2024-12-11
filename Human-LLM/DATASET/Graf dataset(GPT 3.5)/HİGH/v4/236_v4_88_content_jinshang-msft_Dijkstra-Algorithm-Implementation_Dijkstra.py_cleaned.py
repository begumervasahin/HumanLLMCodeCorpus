import re
import numpy as np
with open('Graph.dat', 'r') as graph_file:
    b1 = int(graph_file.readline())
    b2 = [graph_file.readline().strip() for _ in range(b1)]
b3 = ''.join([str(i) + '+' + '(.+)' for i in range(1, b1 + 1)])
b3 = re.compile(b3)
b4 = np.zeros(shape=(b1, b1))
for index, line in enumerate(b2):
    b5 = b3.match(line)
    for x in range(b1):
        b4[index][x] = int(b5.group(x + 1)))
with open('Input.dat', 'r') as input_file:
    b6 = [line.strip() for line in input_file.readlines() if line.strip() != '0']
b7 = np.array(b6)
b8 = b7[::3]
b9 = b7[1::3]
with open('/Users/JcShang/Desktop/Output.dat', 'w+') as output_file:
    for b10, b11 in zip(b8, b9):
        b10 = int(b10) - 1
        b11 = int(b11) - 1
        b12 = np.zeros(shape=(b1))
        b13 = np.array([b10])
        b14 = np.zeros(shape=(b1))
        while True:
            b15 = np.inf
            for i in b13:
                for j in range(b1):
                    if j not in b13:
                        if b14[int(i)] + b4[int(i)][j] < b15 and b4[int(i)][j] > 0:
                            b15 = b14[int(i)] + b4[int(i)][j]
                            b16 = j
                            b17 = i
            b13 = np.append(b13, [b16], axis=0)
            b14[b16] = b14[int(b17)] + b4[int(b17)][b16]
            b12[b16] = b17
            if b11 in b13:
                break
        b18 = np.array([])
        b18 = np.append(b18, [b11], axis=0)
        while b10 not in b18:
            b18 = np.append(b18, [b12[int(b18[-1])]], axis=0)
        output_file.write(str(b14[b11]) + '\n')
        b19 = len(b18) - 1
        while b19 >= 0:
            output_file.write(str(b18[-1] + 1) + '\n')
            b18 = b18[:-1]
            b19 -= 1
        output_file.write('FFFF\n')
output_file.write('0\n')