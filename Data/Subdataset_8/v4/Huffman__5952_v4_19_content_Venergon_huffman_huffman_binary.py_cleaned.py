	class Node:
    def __init__(self, value, probability):
        self.value = value
        self.probability = probability
        self.code = ""
    def __str__(self):
        return "({})".format(self.value)
    def get_probability(self):
        return self.probability
    def get_value(self):
        return self.value
    def set_code(self, code):
        self.code = code
    def get_code(self):
        return self.code
class NodeJoin:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.probability = node1.get_probability() + node2.get_probability()
        self.code = ""
    def __str__(self):
        return "({},{})".format(self.node1, self.node2)
    def get_probability(self):
        return self.probability
    def get_value(self):
        return self.node1.get_value() + self.node2.get_value()
    def set_code(self, code):
        self.code = code
    def get_code(self):
        return self.code
def split_nodes(node):
    code = node.get_code()
    node1, node2 = node.node1, node.node2
    node1.set_code(code + "1")
    node2.set_code(code + "0")
    if isinstance(node1, NodeJoin):
        split_nodes(node1)
    else:
        final_codes.append(node1)
    if isinstance(node2, NodeJoin):
        split_nodes(node2)
    else:
        final_codes.append(node2)
nodes = []
n = input("Enter node (value, probability): ")
if "," not in n:
    print("No first node. Maybe you were trying to set a radix? (This version only works with radix two)")
    n = input("Enter node (value, probability): ")
while n:
    value, probability = n.split(",")
    probability = float(probability)
    nodes.append(Node(value, probability))
    n = input("Enter node (value, probability): ")
if sorted(nodes, key=lambda x: x.get_probability(), reverse=True) != nodes:
    print("Nodes are not sorted! Sorting...")
    nodes.sort(key=lambda x: x.get_probability(), reverse=True)
    print("New nodes:")
    for node in nodes:
        print("  " + str(node))
while len(nodes) > 1:
    new_nodes = nodes[:-2]
    new_node = NodeJoin(nodes[-1], nodes[-2])
    for i, obj in enumerate(new_nodes):
        if new_node.get_probability() >= obj.get_probability():
            new_nodes.insert(i, new_node)
            break
    else:
        new_nodes.append(new_node)
    nodes = new_nodes
assert len(nodes) == 1
node = nodes[0]
node.set_code("")
if isinstance(node, Node):
    final_codes.append(node)
else:
    split_nodes(node)
final_codes.sort(key=lambda x: x.get_value())
print()
for node in final_codes:
    print("Node {} has code {}".format(node, node.get_code()))