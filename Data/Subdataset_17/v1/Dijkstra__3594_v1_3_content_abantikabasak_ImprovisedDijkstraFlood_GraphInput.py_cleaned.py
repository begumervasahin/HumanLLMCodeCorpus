import networkx as nx
import csv
import math
def dist(Node1, Node2):
    x1, y1 = Node1
    x2, y2 = Node2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance
def main():
    with open("bnk_node.csv", 'w', newline='') as node_file, \
         open("q_result.csv", 'r') as edge_input, \
         open("bnk_edge.csv", 'w', newline='') as edge_file:
        node_writer = csv.writer(node_file)
        edge_writer = csv.writer(edge_file)
        edge_reader = csv.reader(edge_input)
        node_list = []
        node_dict = {}
        index = 1
        for line in edge_reader:
            print(line)
            line_data = str(line[0]).split()
            node1 = (float(line_data[1]), float(line_data[2]))
            node2 = (float(line_data[4]), float(line_data[5]))
            if node1 not in node_list:
                node_list.append(node1)
                node_writer.writerow([index, node1[0], node1[1]])
                node_dict[node1] = index
                index += 1
            if node2 not in node_list:
                node_list.append(node2)
                node_writer.writerow([index, node2[0], node2[1]])
                node_dict[node2] = index
                index += 1
            distance = dist(node1, node2)
            weight = int(line_data[8])
            edge_writer.writerow([node_dict[node1], node_dict[node2], weight, distance])
            edge_writer.writerow([node_dict[node2], node_dict[node1], weight, distance])
if __name__ == "__main__":
    main()