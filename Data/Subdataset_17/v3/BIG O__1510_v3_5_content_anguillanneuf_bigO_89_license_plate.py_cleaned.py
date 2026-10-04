import re
def create_dict(plate):
    plate_dict = {}
    for ch in plate.lower():
        if ch.isalpha():
            plate_dict[ch] = plate_dict.get(ch, 0) + 1
    return plate_dict
def search_brute_force(vocab, plate):
    plate_dict = create_dict(plate)
    shortest = None
    for word in vocab:
        word_dict = create_dict(word)
        for key in plate_dict:
            if key in word_dict:
                word_dict[key] -= plate_dict[key]
                if word_dict[key] < 0:
                    break
            else:
                break
        else:
            if shortest is None or len(shortest) > len(word):
                shortest = word
    return shortest
vocab = ['enjoy','enjoying', 'joy','joyful','joyous','joyousness']
plate = 'NY10NJ'
print(f"Working solution for the shortest word: {search_brute_force(vocab, plate)}\n")
class TrieNode:
    def __init__(self, char=None, state=None):
        self.char = char
        self.state = state
        self.prev = None
        self.next = None
class TrieTree:
    def __init__(self):
        self.root = None
    def insert(self, trie_node):
        if self.root is None:
            self.root = trie_node
        else:
            current = self.root
            while current.next:
                current = current.next
            current.next = trie_node
            trie_node.prev = current
    def delete(self, trie_node):
        if self.root is None:
            raise Exception("There are no nodes left to delete!")
        if trie_node.prev:
            trie_node.prev.next = trie_node.next
        if trie_node.next:
            trie_node.next.prev = trie_node.prev
        if trie_node == self.root:
            self.root = trie_node.next
def check_word(prev_tree, word, plate_dict):
    current_node = prev_tree.root
    updated_plate_dict = plate_dict.copy()
    for ch in word:
        if ch in updated_plate_dict:
            updated_plate_dict[ch] -= 1
        if current_node is None or ch != current_node.char:
            new_node = TrieNode(ch, updated_plate_dict.copy())
            prev_tree.insert(new_node)
            current_node = new_node
        else:
            current_node = current_node.next
    return updated_plate_dict
def search_prefix(vocab, plate):
    shortest = None
    prev_tree = TrieTree()
    plate_dict = create_dict(plate)
    for word in vocab:
        temp = check_word(prev_tree, word, plate_dict)
        if all(v <= 0 for v in temp.values()):
            if shortest is None or len(shortest) > len(word):
                shortest = word
        print(word, shortest, temp)
    return shortest
if __name__ == "__main__":
    trie_node1 = TrieNode('e', {'j': 1, 'n': 2, 'y': 1})
    trie_node2 = TrieNode('n', {'j': 1, 'n': 1, 'y': 1})
    trie_node3 = TrieNode('j', {'n': 1, 'y': 1})
    my_trie_tree = TrieTree()
    my_trie_tree.insert(trie_node1)
    my_trie_tree.insert(trie_node2)
    my_trie_tree.insert(trie_node3)
    print("Constructing...")
    node = my_trie_tree.root
    while node:
        print(node.prev.char if node.prev else None, node.char, node.state)
        node = node.next
    print("Deleting... and inserting...")
    my_trie_tree.delete(trie_node3)
    trie_node4 = TrieNode('o', {'n': 1, 'y': 1})
    trie_node5 = TrieNode('y', {'n': 1})
    my_trie_tree.insert(trie_node4)
    node = my_trie_tree.root
    while node:
        print(node.char, node.state)
        node = node.next
    print('\nTesting...')
    prev_tree = TrieTree()
    word = 'enjoy'
    plate_dict = {'j': 1, 'n': 2, 'y': 1}
    check_word(prev_tree, word, plate_dict)
    print(word)
    node = prev_tree.root
    while node:
        print(node.char, node.state)
        node = node.next
    word = 'english'
    check_word(prev_tree, word, plate_dict)
    print(word)
    node = prev_tree.root
    while node:
        print(node.char, node.state)
        node = node.next
    ans = search_prefix(vocab, plate)
    print(f"\nSolution...\nfor {vocab} and {plate} is ...\n\n{ans}")