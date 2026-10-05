import sys
class Node:
    def __init__(self, val, key=''):
        self.key = key
        self.val = val
        self.code = None
        self.left = None
        self.right = None
def fill_codes(node):
    if node.left is None and node.right is None:
        return
    if node.left is not None:
        node.left.code = '0'
        fill_codes(node.left)
    if node.right is not None:
        node.right.code = '1'
        fill_codes(node.right)
def get_letter_codes(di, node, val):
    if node.left is None and node.right is None:
        di[node.key] = '{}'.format(node.code) + val
        return
    get_letter_codes(di, node.left, val + node.left.code)
    get_letter_codes(di, node.right, val + node.right.code)
def huffman_encoding(data):
    if data is None:
        return None
    val = {}
    for char in data:
        if char not in val:
            val[char] = 1
            continue
        val[char] += 1
    if len(val) == 1:
        first_node = Node(val[data[0]], data[0])
        root = Node(first_node.val)
        root.left = first_node
        first_node.code = 0
        result = '0' * val[data[0]]
        return result, root
    sorted_values = sorted(val.items(), key=lambda x: x[1])
    queue_of_nodes = [Node(value[1], value[0]) for value in sorted_values]
    queue_of_nodes.append(Node(None))
    while len(queue_of_nodes) > 2:
        left_node = queue_of_nodes.pop(0)
        if left_node.val is None:
            queue_of_nodes.append(left_node)
            continue
        right_node = queue_of_nodes.pop(0)
        if right_node.val is None:
            queue_of_nodes.append(left_node)
            queue_of_nodes.append(right_node)
            continue
        internal_node = Node(left_node.val + right_node.val)
        internal_node.left = left_node
        internal_node.right = right_node
        queue_of_nodes.append(internal_node)
    root = queue_of_nodes.pop(0)
    if root.val is None:
        root = queue_of_nodes.pop(0)
    fill_codes(root)
    di = {}
    get_letter_codes(di, root, '')
    e = ''
    for char in data:
        e += di[char]
    return e, root
def huffman_decoding(data, dec_tree):
    if data is None or dec_tree is None:
        return
    if dec_tree.right is None:
        count = len(data)
        get_letter = dec_tree.left.key
        return get_letter * count
    final_value = ''
    temp = {}
    get_letter_codes(temp, dec_tree, '')
    generated_dict = {}
    for key in temp:
        generated_dict[temp[key]] = key
    v = ''
    for char in data:
        v += char
        if v in generated_dict:
            final_value += generated_dict[v]
            v = ''
    return final_value
def replicate_functionality(input_data):
    print("The size of the data is: {}\n".format(sys.getsizeof(input_data)))
    print("The content of the data is: {}\n".format(input_data))
    encoded_data, tree = huffman_encoding(input_data)
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))
if __name__ == "__main__":
    replicate_functionality("The bird is the word")
if __name__ == "__main__":
    replicate_functionality("The bird is the word23y rkuwejfkjgfkj vduhdqlihoi fhglkrhtieriyweo iwefhli whiflhevidfghierhg")
if __name__ == "__main__":
    replicate_functionality(None)
if __name__ == "__main__":
    replicate_functionality("aaaaaaaa")