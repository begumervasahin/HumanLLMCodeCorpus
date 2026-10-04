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
        self.nodes = {}
    def add_node(self, node):
        self.nodes[node.index] = node
    def __str__(self):
        result = [f"Head node index: {self.head_index}"]
        for node in self.nodes.values():
            result.append(f"Node {node.index} has children {node.children}")
        return "\n".join(result)
def read_graph_from_file(file_path):
    with open(file_path, "r") as file:
        head_index = int(file.readline().strip())
        graph = Graph(head_index)
        for line in file:
            parent_index, child_index = map(int, line.strip().split(','))
            if parent_index not in graph.nodes:
                graph.add_node(Node(parent_index))
            graph.nodes[parent_index].add_child(child_index)
            if child_index not in graph.nodes:
                graph.add_node(Node(child_index))
    return graph
if __name__ == "__main__":
    file_path = 'graph_data.txt'
    graph = read_graph_from_file(file_path)
    print(graph)