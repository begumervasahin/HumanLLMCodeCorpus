import csv
import math
def calculate_distance(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance
def process_edge_input(edge_reader, node_writer, edge_writer):
    node_list = []
    node_dict = {}
    index = 1
    for line in edge_reader:
        elements = line[0].split()
        node1 = (float(elements[1]), float(elements[2]))
        node2 = (float(elements[4]), float(elements[5]))
        for node in [node1, node2]:
            if node not in node_list:
                node_list.append(node)
                node_writer.writerow([index, node[0], node[1]])
                node_dict[node] = index
                index += 1
        edge_writer.writerow([node_dict[node1], node_dict[node2], int(elements[8]), calculate_distance(node1, node2)])
        edge_writer.writerow([node_dict[node2], node_dict[node1], int(elements[8]), calculate_distance(node1, node2)])
def main():
    with open("bnk_node.csv", 'w') as node_file, \
         open("q_result.csv", 'r') as edge_input, \
         open("bnk_edge.csv", 'w') as edge_file:
        node_writer = csv.writer(node_file)
        edge_reader = csv.reader(edge_input)
        edge_writer = csv.writer(edge_file)
        process_edge_input(edge_reader, node_writer, edge_writer)
if __name__ == "__main__":
    main()