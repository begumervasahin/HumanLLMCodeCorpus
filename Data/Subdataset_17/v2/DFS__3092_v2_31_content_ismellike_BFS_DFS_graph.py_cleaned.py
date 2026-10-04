class Node:
    def __init__(self, index):
        self.index = index
        self.children = []
        self.discovered = False
    def add_child(self, child_index):
        self.children.append(child_index)
class Graph:
    def __init__(self, head_index):
        self.head_index = head_index
        self.nodes = []
    def add_node(self, node):
        self.nodes.append(node)
def read_graph_from_file(file_path):
    with open(file_path, 'r') as file:
        head_index = int(file.readline().strip())
        graph = Graph(head_index)
        current_index = -1
        current_node = None
        for line in file:
            parent_index, child_index = map(int, line.strip().split(','))
            if current_index == parent_index:
                current_node.add_child(child_index)
            else:
                if current_node is not None:
                    graph.add_node(current_node)
                current_index = parent_index
                current_node = Node(parent_index)
                current_node.add_child(child_index)
        if current_node is not None:
            graph.add_node(current_node)
    return graph
if __name__ == "__main__":
    file_path = 'graph_data.txt'
    graph = read_graph_from_file(file_path)
    print(f"Head node index: {graph.head_index}")
    for node in graph.nodes:
        print(f"Node {node.index} has children {node.children}")