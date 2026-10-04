class Node:
    def __init__(self, frequency, char=None):
        self.left = None
        self.right = None
        self.frequency = frequency
        self.char = char
    def print_tree(self):
        if self.char is not None:
            print(self.char, end=" ")
        else:
            if self.left:
                self.left.print_tree()
            if self.right:
                self.right.print_tree()
class BinaryTree:
    def __init__(self, frequency_list):
        self.sorted_list = sorted(frequency_list, key=frequency_list.get, reverse=True)
        self.frequency_list = frequency_list
        self.code_dict = {}
        self.reverse_dict = {}
        self.node_list = []
    def create_tree(self):
        for char in self.sorted_list:
            self.node_list.append(Node(self.frequency_list[char], char))
        while len(self.node_list) > 1:
            self.node_list.sort(key=lambda node: node.frequency)
            node1 = self.node_list.pop(0)
            node2 = self.node_list.pop(0)
            new_node = Node(node1.frequency + node2.frequency)
            new_node.left = node1
            new_node.right = node2
            self.node_list.append(new_node)
        return self.node_list.pop(0)
    def generate_codes(self, node, encoded=""):
        if node is None:
            return
        if node.char is not None:
            self.code_dict[node.char] = encoded
            self.reverse_dict[encoded] = node.char
            print(f'Character: {node.char}, Code: {encoded}')
            return
        self.generate_codes(node.left, encoded + "1")
        self.generate_codes(node.right, encoded + "0")
    def decode_message(self, file_location, node):
        with open(file_location, 'r') as file:
            encoded = list(file.read())
        index = 0
        decoded_message = ""
        while index < len(encoded):
            index_range = 0
            while not self._is_node(encoded[index:index + index_range], node):
                index_range += 1
                try:
                    decoded_char = self.reverse_dict[''.join(encoded[index:index + index_range])]
                    decoded_message += decoded_char
                    print(decoded_char, end="")
                except KeyError:
                    continue
            index += index_range
        print("\nDecoded Message:", decoded_message)
    def _is_node(self, string_list, node):
        if node.char is not None:
            return True
        if not string_list:
            return False
        if string_list[0] == '1':
            return self._is_node(string_list[1:], node.left)
        elif string_list[0] == '0':
            return self._is_node(string_list[1:], node.right)
        return False
def count_chars(file_location):
    with open(file_location, 'r') as file:
        char_count = Counter(file.read())
    return char_count
def encode_message(file_location, output_location, tree):
    with open(file_location, 'r') as input_file, open(output_location, 'w') as output_file:
        for code, char in tree.reverse_dict.items():
            output_file.write(f'{code} -> {char if char != "\n" else "\\n"}\n')
        output_file.write('```\n')
        total_bits = 0
        for char in input_file.read():
            encoded_char = tree.code_dict[char]
            output_file.write(encoded_char)
            total_bits += len(encoded_char)
    print(f'Number of bits: {total_bits / 8} bytes')
if __name__ == '__main__':
    frequency_list = count_chars('/path/to/your/input.txt')
    tree = BinaryTree(frequency_list)
    root_node = tree.create_tree()
    tree.generate_codes(root_node)
    encode_message('/path/to/your/input.txt', '/path/to/your/output.txt', tree)
    tree.decode_message('/path/to/your/output.txt', root_node)