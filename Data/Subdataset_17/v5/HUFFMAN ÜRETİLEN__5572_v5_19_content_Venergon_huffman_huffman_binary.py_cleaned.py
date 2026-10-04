class Node:
    def __init__(self, value, probability):
        self.value = value
        self.probability = probability
        self.code = ""
    def __str__(self):
        return f"({self.value})"
    def set_code(self, code):
        self.code = code
    def get_code(self):
        return self.code
class NodeJoin(Node):
    def __init__(self, node1, node2):
        super().__init__(node1.value + node2.value, node1.probability + node2.probability)
        self.node1 = node1
        self.node2 = node2
    def __str__(self):
        return f"({self.node1},{self.node2})"
def split_nodes(node, final_codes):
    node1, node2 = node.node1, node.node2
    node1.set_code(node.get_code() + "1")
    node2.set_code(node.get_code() + "0")
    if isinstance(node1, NodeJoin):
        split_nodes(node1, final_codes)
    else:
        final_codes.append(node1)
    if isinstance(node2, NodeJoin):
        split_nodes(node2, final_codes)
    else:
        final_codes.append(node2)
def build_huffman_tree(nodes):
    while len(nodes) > 1:
        node1, node2 = nodes.pop(), nodes.pop()
        new_node = NodeJoin(node1, node2)
        for i, node in enumerate(nodes):
            if new_node.probability >= node.probability:
                nodes.insert(i, new_node)
                break
        else:
            nodes.append(new_node)
    return nodes[0]
def main():
    nodes = []
    while True:
        n = input("Enter node (format: value,probability) or leave empty to finish: ")
        if not n:
            break
        try:
            value, probability = n.split(",")
            probability = float(probability.strip())
            nodes.append(Node(value.strip(), probability))
        except ValueError:
            print("Invalid input format. Please enter in format: value,probability")
    if not nodes:
        print("No nodes entered. Exiting.")
        return
    nodes.sort(key=lambda x: x.probability, reverse=True)
    print("Nodes sorted by probability:")
    for node in nodes:
        print(f"  {node}")
    root_node = build_huffman_tree(nodes)
    final_codes = []
    if isinstance(root_node, NodeJoin):
        split_nodes(root_node, final_codes)
    else:
        final_codes.append(root_node)
    final_codes.sort(key=lambda x: x.value)
    print("\nHuffman Codes:")
    for node in final_codes:
        print(f"Node {node.value} has code {node.get_code()}")
if __name__ == "__main__":
    main()