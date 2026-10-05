import re
import numpy as np
with open('Graph.dat', 'r') as graph_file:
    num_node = int(graph_file.readline())
    lines = [graph_file.readline().strip() for _ in range(num_node)]
pattern = ''.join([str(i) + '+' + '(.+)' for i in range(1, num_node + 1)])
pattern = re.compile(pattern)
result = np.zeros(shape=(num_node, num_node))
for index, line in enumerate(lines):
    ma = pattern.match(line)
    for x in range(num_node):
        result[index][x] = int(ma.group(x + 1)))
with open('Input.dat', 'r') as input_file:
    in_put = [line.strip() for line in input_file.readlines() if line.strip() != '0']
inPut = np.array(in_put)
sources = inPut[::3]
sinks = inPut[1::3]
with open('/Users/JcShang/Desktop/Output.dat', 'w+') as output_file:
    for source, sink in zip(sources, sinks):
        source = int(source) - 1
        sink = int(sink) - 1
        prev = np.zeros(shape=(num_node))
        visited = np.array([source])
        dis = np.zeros(shape=(num_node))
        while True:
            minDis = np.inf
            for i in visited:
                for j in range(num_node):
                    if j not in visited:
                        if dis[int(i)] + result[int(i)][j] < minDis and result[int(i)][j] > 0:
                            minDis = dis[int(i)] + result[int(i)][j]
                            nextHop = j
                            lastHop = i
            visited = np.append(visited, [nextHop], axis=0)
            dis[nextHop] = dis[int(lastHop)] + result[int(lastHop)][nextHop]
            prev[nextHop] = lastHop
            if sink in visited:
                break
        path = np.array([])
        path = np.append(path, [sink], axis=0)
        while source not in path:
            path = np.append(path, [prev[int(path[-1])]], axis=0)
        output_file.write(str(dis[sink]) + '\n')
        pointer = len(path) - 1
        while pointer >= 0:
            output_file.write(str(path[-1] + 1) + '\n')
            path = path[:-1]
            pointer -= 1
        output_file.write('FFFF\n')
output_file.write('0\n')