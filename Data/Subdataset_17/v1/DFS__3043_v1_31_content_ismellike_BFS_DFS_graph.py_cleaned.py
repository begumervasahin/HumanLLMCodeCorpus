class Node:
    def __init__(self, index):
        self.children = []
        self.index = index
        self.discovered = False
    def add_child(self, index):
        self.children.append(index)
class Graph:
    def __init__(self, head, nodes):
        self.head = head
        self.nodes = nodes
def read_file(path):
    nodes = []
    with open(path, "r") as file:
        head = int(file.readline().strip())
        current_index = -1
        current_node = None
        for line in file:
            split1, split2 = map(int, line.strip().split(','))
            if current_index == split1:
                current_node.add_child(split2)
            else:
                if current_index != -1:
                    nodes.append(current_node)
                current_index = split1
                current_node = Node(split1)
                current_node.add_child(split2)
        if current_node:
            nodes.append(current_node)
    return Graph(head, nodes)
if __name__ == "__main__":
    file_path = 'graph_data.txt'
    graph = read_file(file_path)
    print(f"Head node: {graph.head}")
    for node in graph.nodes:
        print(f"Node {node.index} has children {node.children}")