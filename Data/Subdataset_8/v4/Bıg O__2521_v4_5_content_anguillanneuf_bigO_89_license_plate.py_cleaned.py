class TrieNode:
    def __init__(self, char=None, state=None):
        self.char = char
        self.state = state
        self.prev = None
        self.next = None
class TrieTree:
    def __init__(self):
        self.root = None
    def insert(self, trieNode):
        if self.root is None:
            self.root = trieNode
            return
        current_node = self.root
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = trieNode
        current_node.next.prev = current_node
    def delete(self, trieNode):
        if self.root is None:
            raise Exception("The trie is empty. Cannot delete nodes.")
        if trieNode.prev:
            trieNode.prev.next = None
        else:
            self.root = None
def create_character_count_dict(plate):
    char_count_dict = {}
    for char in plate:
        char = char.lower()
        if char.isalpha():
            char_count_dict[char] = char_count_dict.get(char, 0) + 1
    return char_count_dict
def search_brute_force(vocabulary, plate):
    plate_char_count = create_character_count_dict(plate)
    shortest_word = None
    for word in vocabulary:
        word_char_count = create_character_count_dict(word)
        for key in plate_char_count.keys():
            if key in word_char_count.keys():
                word_char_count[key] -= plate_char_count[key]
                if word_char_count[key] < 0:
                    continue
            else:
                continue
        if sum(v < 0 for v in word_char_count.values()) > 0:
            if shortest_word is None:
                shortest_word = word
            elif len(shortest_word) > len(word):
                shortest_word = word
    return shortest_word
def check_word(prev_tree, word, plate_dict):
    if prev_tree.root is not None:
        current_node = prev_tree.root
    for char in word:
        plate_dict = plate_dict.copy()
        if char in plate_dict.keys():
            plate_dict[char] -= 1
        if prev_tree.root is None:
            prev_tree.insert(TrieNode(char, plate_dict))
            current_node = prev_tree.root
        if current_node is None:
            current_node = TrieNode(char, plate_dict)
            prev_tree.insert(current_node)
            current_node = current_node.next
        elif char == current_node.char:
            current_node = current_node.next
        else:
            prev_tree.delete(current_node)
            current_node = TrieNode(char, plate_dict)
            prev_tree.insert(current_node)
            current_node = current_node.next
    return plate_dict
def search_prefix(vocabulary, plate):
    shortest = None
    prev_tree = TrieTree()
    plate_dict = create_character_count_dict(plate)
    for word in vocabulary:
        temp = check_word(prev_tree, word, plate_dict)
        if not any(v > 0 for v in temp.values()):
            if shortest is None:
                shortest = word
            elif len(shortest) > len(word):
                shortest = word
    return shortest
vocabulary = ['enjoy', 'enjoying', 'joy', 'joyful', 'joyous', 'joyousness']
license_plate = 'NY10NJ'
print("Shortest word found:", search_brute_force(vocabulary, license_plate))
print("Solution for '{}' and '{}' is '{}'".format(vocabulary, license_plate, search_prefix(vocabulary, license_plate)))