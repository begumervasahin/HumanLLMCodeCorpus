class Node:
    def __init__(self, datum):
        self.datum = datum
        self.left = None
        self.right = None
    def get_datum(self):
        return self.datum
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
    def insert_left(self, node):
        self.left = node
    def insert_right(self, node):
        self.right = node
class Huffman:
    def __init__(self):
        self.root = None
        self.encoding_log = []
    def is_empty(self):
        return self.root is None
    def size(self):
        return self._size(self.root)
    def _size(self, node):
        if not node:
            return 0
        return 1 + self._size(node.get_left()) + self._size(node.get_right())
    def height(self):
        return self._height(self.root)
    def _height(self, node):
        if not node:
            return 0
        return 1 + max(self._height(node.get_left()), self._height(node.get_right()))
    def find_char(self, char):
        if not self.encoding_log:
            self._initialize_encoding_log(self.root, "")
            self.encoding_log = sorted(self.encoding_log, key=lambda x: x.get_datum()[1], reverse=True)
        for node in self.encoding_log:
            if node.get_datum()[0] == char:
                return node.get_datum()[2]
        return "error"
    def _initialize_encoding_log(self, node, path):
        if node.get_datum()[0] == '':
            if node.get_left():
                self._initialize_encoding_log(node.get_left(), path + "0")
            if node.get_right():
                self._initialize_encoding_log(node.get_right(), path + "1")
        if not node.get_right() and not node.get_left():
            node.datum.append(path)
            self.encoding_log.append(node)
    def translate(self, bit_string):
        return self._translate(self.root, bit_string)
    def _translate(self, node, bit_string):
        if len(bit_string) > 0:
            if bit_string[0] == "0":
                if node.get_left():
                    return self._translate(node.get_left(), bit_string[1:])
                else:
                    return node.get_datum()[0], bit_string
            if bit_string[0] == "1":
                if node.get_right():
                    return self._translate(node.get_right(), bit_string[1:])
                else:
                    return node.get_datum()[0], bit_string
        return node.get_datum()[0], bit_string
    def insert(self, char_frequency_list):
        if isinstance(char_frequency_list[0], list):
            char_frequency_list = [Node(item) for item in char_frequency_list]
        if len(char_frequency_list) > 1:
            combined_node = Node(['', char_frequency_list[0].get_datum()[1] + char_frequency_list[1].get_datum()[1]])
            combined_node.insert_left(char_frequency_list[0])
            combined_node.insert_right(char_frequency_list[1])
            char_frequency_list.append(combined_node)
            char_frequency_list = sorted(char_frequency_list[2:], key=lambda x: x.get_datum()[1])
            self.insert(char_frequency_list)
        else:
            self.root = char_frequency_list[0]
    def print_inorder(self):
        self._print_inorder(self.root)
        print()
    def _print_inorder(self, node):
        if node.get_left():
            self._print_inorder(node.get_left())
        print(node.get_datum(), end=" ")
        if node.get_right():
            self._print_inorder(node.get_right())
if __name__ == "__main__":
    huffman_tree = Huffman()
    char_freqs = [['a', 1], ['b', 1], ['c', 1], ['d', 2], ['e', 6], ['f', 10], ['g', 15]]
    huffman_tree.insert(char_freqs)
    encoding_c = huffman_tree.find_char('c')
    encoding_a = huffman_tree.find_char('a')
    encoded_string = str(encoding_c + encoding_a)
    print(encoded_string)
    while encoded_string:
        decoded_char, encoded_string = huffman_tree.translate(encoded_string)
        print(decoded_char, end="")