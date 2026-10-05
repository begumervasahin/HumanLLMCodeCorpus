import os
from collections import Counter
class Node:
    def __init__(self, content, frequency, binary='', left=None, right=None):
        self.content = content
        self.frequency = frequency
        self.binary = binary
        self.left = left
        self.right = right
    def __repr__(self):
        return repr((self.content, self.frequency, self.binary))
    def is_leaf(self):
        return self.left is None and self.right is None
class NodeList:
    def __init__(self, lst):
        self.text = lst
    def insert_root(self, new_node):
        self.root = [new_node]
        return
    def insert_element(self, new_node):
        for i in self.root:
            if i.content == new_node.content:
                i.frequency += 1
                self.root = sorted(self.root, key=lambda node: node.frequency)
                return
        self.root += [new_node]
        self.root = sorted(self.root, key=lambda node: node.frequency)
    def create_list(self):
        for l in self.text:
            if not self.root:
                self.insert_root(Node(l, 1, '', None, None))
            else:
                self.insert_element(Node(l, 1, '', None, None))
        return
    def print_list(self):
        for elem in self.root:
            print(elem)
        return
    def create_tree(self):
        self.create_list()
        while len(self.root) > 1:
            new_node = Node("", self.root[0].frequency + self.root[1].frequency, '', self.root[0], self.root[1])
            del self.root[0]
            del self.root[0]
            self.root += [new_node]
            self.root = sorted(self.root, key=lambda node: node.frequency)
        return
class HuffmanTree:
    def encode(self, node):
        if node is None:
            return
        if node.left is not None:
            node.left.binary = node.binary + '1'
            self.encode(node.left)
        if node.right is not None:
            node.right.binary = node.binary + '0'
            self.encode(node.right)
        return
    def character_binary(self, tree, l):
        binary = ''
        if tree.content == l:
            binary = tree.binary
        if tree.left is not None:
            binary = self.character_binary(tree.left, l)
        if binary == '':
            if tree.right is not None:
                binary = self.character_binary(tree.right, l)
        return binary
    def text_binary(self, tree, text):
        result = ''
        for l in text:
            result += self.character_binary(tree, l)
        return result
    def decode(self, tree2, binary_text):
        tree = tree2
        result = ''
        for bin in binary_text:
            if bin == '1':
                if tree.left is not None:
                    tree = tree.left
                    if tree.left is None and tree.right is None:
                        result += (tree.content)
                        tree = tree2
            else:
                if tree.right is not None:
                    tree = tree.right
                    if tree.left is None and tree.right is None:
                        result += (tree.content)
                        tree = tree2
        return result
    def print_table(self, node):
        if node is None:
            return
        if node.left is not None:
            self.print_table(node.left)
        if node.is_leaf():
            print(node)
        if node.right is not None:
            self.print_table(node.right)
        return
def load_frequencies(lst):
    frequencies = Counter(lst)
    return frequencies
def open_file(file_name):
    if not os.path.isfile(file_name):
        print("File not found!")
        exit()
    else:
        with open(file_name, "r") as file:
            text = file.read()
        return text
def create_file(file_name, text):
    try:
        file = open(file_name, 'w')
        file.write(text)
        file.close()
    except IOError:
        raise print("Error creating file!")
def main(args):
    print("TO START THE PROGRAM, INSERT THE FILE NAME WHERE THE WORD TO BE COMPRESSED IS LOCATED")
    file_name = input("Name: ")
    word = open_file(file_name)
    lst = list(open_file(file_name))
    huffman = HuffmanTree()
    node_list = NodeList(lst)
    node_list.create_tree()
    huffman.encode(node_list.root[0])
    print("--------------------- EXECUTION OF HUFFMAN CODE ---------------------")
    print("Inserted word:", word)
    print("")
    print("Character frequencies:")
    freqs = load_frequencies(lst)
    print(freqs)
    print("")
    print("Tree created successfully!")
    print("")
    print("Huffman table:")
    huffman.print_table(node_list.root[0])
    print("")
    code = huffman.text_binary(node_list.root[0], node_list.text)
    print("Word compressed to binary:", code)
    print("")
    decode_code = huffman.decode(node_list.root[0], huffman.text_binary(node_list.root[0], node_list.text))
    print("Decompressed word:", decode_code)
    print("")
    create_file("result.txt", ("Inserted Word: " + word + "\n" +
                               "Compressed Word: " + code + "\n" +
                               "Decompressed Word: " + decode_code + "\n"
    ))
    print("Output file generated successfully!")
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))