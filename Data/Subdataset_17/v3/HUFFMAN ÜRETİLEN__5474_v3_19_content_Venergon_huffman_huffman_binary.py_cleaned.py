class Node:
    def __init__(self, val, probability):
        self.val = val
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
def assign_codes(node, final_codes):
    code = node.get_code()
    node1, node2 = node.node1, node.node2
    node1.set_code(code + "0")
    node2.set_code(code + "1")
    if isinstance(node1, NodeJoin):
        assign_codes(node1, final_codes)
    else:
        final_codes.append(node1)
    if isinstance(node2, NodeJoin):
        assign_codes(node2, final_codes)
    else:
        final_codes.append(node2)
def build_huffman_tree(nodes):
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.probability)
        node1 = nodes.pop(0)
        node2 = nodes.pop(0)
        new_node = NodeJoin(node1, node2)
        nodes.append(new_node)
    return nodes[0]
def main():
    nodes = []
    while True:
        n = input("Enter node (or leave blank to stop): ")
        if not n:
            break
        try:
            val, probability = n.split(",")
            nodes.append(Node(val, float(probability)))
        except ValueError:
            print("Invalid input. Please use the format 'value,probability'.")
            continue
    if not nodes:
        print("No nodes entered. Exiting.")
        return
    root = build_huffman_tree(nodes)
    final_codes = []
    root.set_code("")
    if isinstance(root, Node):
        final_codes.append(root)
    else:
        assign_codes(root, final_codes)
    final_codes.sort(key=lambda x: x.val)
    print("\nHuffman Codes:")
    for node in final_codes:
        print(f"Node {node} has code {node.get_code()}")
if __name__ == "__main__":
    main()