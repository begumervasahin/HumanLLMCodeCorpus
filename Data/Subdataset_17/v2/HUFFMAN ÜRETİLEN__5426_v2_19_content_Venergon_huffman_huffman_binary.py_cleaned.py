class Node:
    def __init__(self, value, probability):
        self.val = value
        self.probability = probability
        self.code = ""
    def __str__(self):
        return f"({self.val})"
    def set_code(self, code):
        self.code = code
    def get_code(self):
        return self.code
class NodeJoin:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.probability = node1.probability + node2.probability
        self.code = ""
    def __str__(self):
        return f"({self.node1},{self.node2})"
    def set_code(self, code):
        self.code = code
    def get_code(self):
        return self.code
def split_nodes(node, final_codes):
    code = node.get_code()
    node1, node2 = node.node1, node.node2
    node1.set_code(code + "1")
    node2.set_code(code + "0")
    if isinstance(node1, NodeJoin):
        split_nodes(node1, final_codes)
    else:
        final_codes.append(node1)
    if isinstance(node2, NodeJoin):
        split_nodes(node2, final_codes)
    else:
        final_codes.append(node2)
def main():
    nodes = []
    while True:
        n = input("Enter node (or leave blank to stop): ")
        if not n:
            break
        if "," not in n:
            print("Invalid input. Please use the format 'value,probability'.")
            continue
        value, probability = n.split(",")
        nodes.append(Node(value, float(probability)))
    if not nodes:
        print("No nodes entered. Exiting.")
        return
    nodes.sort(key=lambda x: x.probability, reverse=True)
    print("Nodes sorted by probability:")
    for node in nodes:
        print(f"  {node}")
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.probability)
        node1 = nodes.pop(0)
        node2 = nodes.pop(0)
        new_node = NodeJoin(node1, node2)
        nodes.append(new_node)
    final_codes = []
    root = nodes[0]
    root.set_code("")
    if isinstance(root, Node):
        final_codes.append(root)
    else:
        split_nodes(root, final_codes)
    final_codes.sort(key=lambda x: x.val)
    print("\nHuffman Codes:")
    for node in final_codes:
        print(f"Node {node} has code {node.get_code()}")
if __name__ == "__main__":
    main()