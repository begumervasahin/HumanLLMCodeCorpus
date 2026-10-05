import queue as Q
class Pair:
    def __init__(self, element, priority):
        self.element = element
        self.priority = priority
    def __lt__(self, other):
        return int.__lt__(self.priority, other.priority)
    def __gt__(self, other):
        return int.__gt__(self.priority, other.priority)
    def __eq__(self, other):
        return int.__eq__(self.priority, other.priority) and self.element == other.element
    def __le__(self, other):
        return int.__le__(self.priority, other.priority)
    def __ge__(self, other):
        return int.__ge__(self.priority, other.priority)
    def __str__(self):
        return "(" + self.element.__str__() + self.priority.__str__() + ")"
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
        self.data = self.data + [elem]
    def __str__(self):
        return self.data.__str__()
class Tree:
    def __init__(self, value):
        self.node = value
        self.left = None
        self.right = None
    def __str__(self):
        return "(" + self.left.__str__() + self.node.__str__() + self.right.__str__() + ")"
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
        if letter in letter_density:
            letter_density[letter] += 1
        else:
            letter_density[letter] = 1
    return letter_density
def create_dictionary(tree, traversal, dictionary):
    if tree.node is not None:
        dictionary[tree.node] = traversal
        return None
    if tree.left is not None:
        traversal = traversal + "0"
        create_dictionary(tree.left, traversal, dictionary)
        traversal = traversal[:-1]
    if tree.right is not None:
        traversal = traversal + "1"
        create_dictionary(tree.right, traversal, dictionary)
if __name__ == "__main__":
    density = create_density("chabadabada")
    print(density)
    tree = create_tree(density)
    dictionary = {}
    create_dictionary(tree, "", dictionary)
    print(dictionary)