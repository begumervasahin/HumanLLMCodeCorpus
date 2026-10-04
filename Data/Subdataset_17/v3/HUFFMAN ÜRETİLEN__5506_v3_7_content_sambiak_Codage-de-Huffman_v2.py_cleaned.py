class Pair:
    def __init__(self, element, priority):
        self.element = element
        self.priority = priority
    def __lt__(self, other):
        return self.priority < other.priority
    def __gt__(self, other):
        return self.priority > other.priority
    def __eq__(self, other):
        return self.priority == other.priority and self.element == other.element
    def __le__(self, other):
        return self.priority <= other.priority
    def __ge__(self, other):
        return self.priority >= other.priority
    def __str__(self):
        return f"({self.element}, {self.priority})"
    def __repr__(self):
        return self.__str__()
class PriorityQueue:
    def __init__(self):
        self.data = []
    def qsize(self):
        return len(self.data)
    def get(self):
        return self.data.pop()
    def put(self, elem):
        for i, el in enumerate(self.data):
            if elem > el:
                self.data.insert(i, elem)
                return
        self.data.append(elem)
    def __str__(self):
        return str(self.data)
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return f"({self.left}, {self.value}, {self.right})"
def create_huffman_tree(letter_frequencies):
    priority_queue = PriorityQueue()
    for letter, frequency in letter_frequencies.items():
        priority_queue.put(Pair(TreeNode(letter), frequency))
    while priority_queue.qsize() > 1:
        left = priority_queue.get()
        right = priority_queue.get()
        merged_node = TreeNode(None)
        merged_node.left = left.element
        merged_node.right = right.element
        priority_queue.put(Pair(merged_node, left.priority + right.priority))
    return priority_queue.get().element
def calculate_frequencies(text):
    frequencies = {}
    for letter in text:
        frequencies[letter] = frequencies.get(letter, 0) + 1
    return frequencies
def generate_huffman_codes(tree, path="", code_dict=None):
    if code_dict is None:
        code_dict = {}
    if tree.value is not None:
        code_dict[tree.value] = path
    else:
        if tree.left:
            generate_huffman_codes(tree.left, path + "0", code_dict)
        if tree.right:
            generate_huffman_codes(tree.right, path + "1", code_dict)
    return code_dict
if __name__ == "__main__":
    text = "chabadabada"
    frequencies = calculate_frequencies(text)
    print("Frequencies:", frequencies)
    huffman_tree = create_huffman_tree(frequencies)
    print("Huffman Tree:", huffman_tree)
    huffman_codes = generate_huffman_codes(huffman_tree)
    print("Huffman Codes:", huffman_codes)