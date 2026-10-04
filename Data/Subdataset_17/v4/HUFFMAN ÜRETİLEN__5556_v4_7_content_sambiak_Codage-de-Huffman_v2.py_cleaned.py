import queue as Q
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
                self.data = self.data[:i] + [elem] + self.data[i:]
                return
        self.data.append(elem)
    def __str__(self):
        return str(self.data)
class Tree:
    def __init__(self, value):
        self.node = value
        self.left = None
        self.right = None
    def __str__(self):
        return f"({self.left}, {self.node}, {self.right})"
def create_tree(frequency_dict):
    priority_queue = PriorityQueue()
    for letter, frequency in frequency_dict.items():
        priority_queue.put(Pair(Tree(letter), frequency))
    while priority_queue.qsize() > 1:
        left = priority_queue.get()
        right = priority_queue.get()
        new_tree = Tree(None)
        new_tree.left = left.element
        new_tree.right = right.element
        priority_queue.put(Pair(new_tree, left.priority + right.priority))
    return priority_queue.get().element
def create_frequency_dict(text):
    frequency_dict = {}
    for letter in text:
        if letter in frequency_dict:
            frequency_dict[letter] += 1
        else:
            frequency_dict[letter] = 1
    return frequency_dict
def create_code_dict(tree, path, code_dict):
    if tree.node is not None:
        code_dict[tree.node] = path
        return
    if tree.left is not None:
        create_code_dict(tree.left, path + "0", code_dict)
    if tree.right is not None:
        create_code_dict(tree.right, path + "1", code_dict)
if __name__ == "__main__":
    text = "chabadabada"
    frequency_dict = create_frequency_dict(text)
    print("Frequency Dictionary:", frequency_dict)
    huffman_tree = create_tree(frequency_dict)
    print("Huffman Tree:", huffman_tree)
    code_dict = {}
    create_code_dict(huffman_tree, "", code_dict)
    print("Code Dictionary:", code_dict)