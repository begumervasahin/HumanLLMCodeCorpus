from queue import PriorityQueue
class Node:
    def __init__(self, data, frequency, leftChild=None, rightChild=None):
        self.data = data
        self.frequency = frequency
        self.leftChild = leftChild
        self.rightChild = rightChild
    def __lt__(self, other):
        return self.frequency < other.frequency
    def __repr__(self):
        return "Node: value ({}), frequency ({}), leftChild(), rightChild()\n".format(self.data, self.frequency)
def init_list(string):
    queue = PriorityQueue()
    char_list = []
    is_space_added = False
    is_comma_added = False
    for char in string:
        if char not in char_list:
            char_list.append(char)
            queue.put(Node(char, string.count(char)))
        elif char == ' ' and not is_space_added:
            queue.put(Node(char, string.count(char)))
            is_space_added = True
        elif char == ',' and not is_comma_added:
            queue.put(Node(char, string.count(char)))
            is_comma_added = True
    return queue
def create_tree(queue):
    while queue.qsize() > 1:
        left_node = queue.get()
        right_node = queue.get()
        frequency = left_node.frequency + right_node.frequency
        node = Node(None, frequency, left_node, right_node)
        queue.put(node)
    return queue.get()
def create_hash_table(node, code, hash_table):
    if node.leftChild is None and node.rightChild is None:
        hash_table.update({node.data: code})
        return hash_table
    if node.leftChild is not None:
        create_hash_table(node.leftChild, code + "0", hash_table)
    if node.rightChild is not None:
        create_hash_table(node.rightChild, code + "1", hash_table)
def encode(string, hash_table):
    encoded_string = ""
    for char in string:
        encoded_string += str(hash_table[char])
    return encoded_string
def decode(string, node):
    global i
    if node.leftChild is None and node.rightChild is None:
        character = node.data
        return character
    if string[i] == "0":
        i += 1
        return decode(string, node.leftChild)
    elif string[i] == "1":
        i += 1
        return decode(string, node.rightChild)
i = 0
file = open('texteEncode.txt', 'r')
string = file.read()
file.close()
queue = init_list(string)
tree = create_tree(queue)
print(tree)
hash_table = {}
create_hash_table(tree, "", hash_table)
print(hash_table)
encoded_string = encode(string, hash_table)
print(encoded_string)
file = open('texteEncode.txt', 'w')
file.write(str(encoded_string))
file.close()
string = encode(string, hash_table)
decoded_string = ""
while i < len(string):
    decoded_string += decode(string, tree)
print(decoded_string)
file.close()