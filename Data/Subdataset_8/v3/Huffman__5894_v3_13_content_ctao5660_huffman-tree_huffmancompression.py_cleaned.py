class Node:
    def __init__(self, frequency, char):
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
        self.list_length = len(self.sorted_list)
        self.freq_list = frequency_list
        self.code_dict = {}
        self.reverse_dict = {}
        self.node_list = []
    def create_tree(self):
        for char in self.sorted_list:
            self.node_list.append(Node(self.freq_list[char], char))
        while True:
            self.node_list.sort(key=lambda node: node.frequency)
            node1 = self.node_list.pop(0)
            node2 = self.node_list.pop(0)
            new_node = Node(node1.frequency + node2.frequency, None)
            new_node.left, new_node.right = (node1, node2) if node1.frequency >= node2.frequency else (node2, node1)
            self.node_list.append(new_node)
            self.node_list.sort(key=lambda node: node.frequency)
            if len(self.node_list) == 1:
                break
        return self.node_list.pop(0)
    def search_and_code(self, root_node, encoded):
        if root_node is None:
            return
        if root_node.char is not None:
            self.code_dict[root_node.char] = encoded
            self.reverse_dict[encoded] = root_node.char
            print('Character: {}, Code: {}'.format(root_node.char, encoded))
            return
        self.search_and_code(root_node.left, encoded + "1")
        self.search_and_code(root_node.right, encoded + "0")
    def is_node(self, string_list, node):
        s = string_list
        if node.char is not None:
            return True
        if not s:
            return False
        if s[0] == '1':
            s.pop(0)
            return self.is_node(s, node.left)
        elif s[0] == '0':
            s.pop(0)
            return self.is_node(s, node.right)
        return False
    def decode_message(self, file_location, root_node):
        with open(file_location, 'r+') as file_test:
            encoded_list = list(file_test.read())
            index = 0
            decoded_string = ''
            while index < len(encoded_list):
                index_range = 0
                while self.is_node(encoded_list[index:index + index_range], root_node) is False:
                    index_range += 1
                    try:
                        decoded_string += self.reverse_dict[''.join(encoded_list[index:index + index_range])]
                        print(self.reverse_dict[''.join(encoded_list[index:index + index_range])])
                    except KeyError:
                        continue
                index += index_range
            print(decoded_string)
def count_chars(file_location):
    char_list = {}
    with open(file_location, 'r') as file_test:
        while True:
            char = file_test.read(1)
            if not char:
                break
            char_list[char] = char_list.get(char, 0) + 1
    return char_list
def encode_message(file_location, new_file_location, huffman_tree):
    with open(file_location, 'r+') as file_test, open(new_file_location, 'w+') as file_output:
        for k, v in huffman_tree.reverse_dict.items():
            v = '\\n' if v == '\n' else v
            file_output.write(f'{k}.-.{v}\n')
        file_output.write('```\n')
        while True:
            char = file_test.read(1)
            if not char:
                break
            file_output.write(huffman_tree.code_dict[char])
if __name__ == "__main__":
    char_list = count_chars('/Users/christao/downloads/freshprince.txt')
    huffman_tree = BinaryTree(char_list)
    root_node = huffman_tree.create_tree()
    huffman_tree.search_and_code(root_node, '')
    encode_message('/Users/christao/downloads/freshprince.txt', '/Users/christao/downloads/testparagraph.txt', huffman_tree)
    print(huffman_tree.reverse_dict)