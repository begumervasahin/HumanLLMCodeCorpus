import csv
import math
def calculate_distance(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance
node_file = open("bnk_node.csv", 'w')
node_writer = csv.writer(node_file)
edge_input = open("q_result.csv", 'r')
edge_reader = csv.reader(edge_input)
edge_file = open("bnk_edge.csv", 'w')
edge_writer = csv.writer(edge_file)
index = 1
node_list = []
node_dict = {}
for line in edge_reader:
    elements = line[0].split()
    Node1 = (float(elements[1]), float(elements[2]))
    Node2 = (float(elements[4]), float(elements[5]))
    for node in [Node1, Node2]:
        if node not in node_list:
            node_list.append(node)
            node_writer.writerow([index, node[0], node[1]])
            node_dict[node] = index
            index += 1
    edge_writer.writerow([node_dict[Node1], node_dict[Node2], int(elements[8]), calculate_distance(Node1, Node2)])
    edge_writer.writerow([node_dict[Node2], node_dict[Node1], int(elements[8]), calculate_distance(Node1, Node2)])
node_file.close()
edge_file.close()
edge_input.close()