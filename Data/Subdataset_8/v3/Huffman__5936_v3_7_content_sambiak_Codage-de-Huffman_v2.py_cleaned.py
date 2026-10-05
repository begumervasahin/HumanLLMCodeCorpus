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
        return f"({self.element}{self.priority})"
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
                return None
        self.data.append(elem)
    def __str__(self):
        return str(self.data)
class Tree:
    def __init__(self, value):
        self.node = value
        self.left = None
        self.right = None
    def __str__(self):
        return f"({self.left}{self.node}{self.right})"
def create_tree(letter_density):
    priority_queue = PriorityQueue()
    for letter in letter_density.keys():
        priority_queue.put(Pair(Tree(letter), letter_density[letter]))
    while priority_queue.qsize() > 1:
        left = priority_queue.get()
        right = priority_queue.get()
        new_tree = Tree(None)
        new_tree.left = left.element
        new_tree.right = right.element
        priority_queue.put(Pair(new_tree, left.priority + right.priority))
    return priority_queue.get().element
def create_density(text):
    letter_density = {}
    for letter in text:
        letter_density[letter] = letter_density.get(letter, 0) + 1
    return letter_density
def create_dictionary(tree, path, dictionary):
    if tree.node is not None:
        dictionary[tree.node] = path
    if tree.left is not None:
        create_dictionary(tree.left, path + "0", dictionary)
    if tree.right is not None:
        create_dictionary(tree.right, path + "1", dictionary)
if __name__ == "__main__":
    density = create_density("chabadabada")
    print("Letter Densities:", density)
    tree = create_tree(density)
    dictionary = {}
    create_dictionary(tree, "", dictionary)
    print("Huffman Dictionary:", dictionary)