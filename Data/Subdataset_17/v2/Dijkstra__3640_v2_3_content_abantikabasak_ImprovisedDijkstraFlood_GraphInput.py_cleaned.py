import networkx as nx
import csv
import math
def calculate_distance(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
def process_edge_input(edge_input_path, node_output_path, edge_output_path):
    with open(node_output_path, 'w', newline='') as node_file, \
         open(edge_input_path, 'r') as edge_input, \
         open(edge_output_path, 'w', newline='') as edge_file:
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
            distance = calculate_distance(node1, node2)
            weight = int(line_data[8])
            edge_writer.writerow([node_dict[node1], node_dict[node2], weight, distance])
            edge_writer.writerow([node_dict[node2], node_dict[node1], weight, distance])
def main():
    edge_input_path = "q_result.csv"
    node_output_path = "bnk_node.csv"
    edge_output_path = "bnk_edge.csv"
    process_edge_input(edge_input_path, node_output_path, edge_output_path)
if __name__ == "__main__":
    main()