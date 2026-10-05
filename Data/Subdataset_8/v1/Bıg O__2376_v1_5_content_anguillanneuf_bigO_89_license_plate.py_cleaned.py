class TrieNode:
    def __init__(self, char=None, state=None):
        self.value = char
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
        currNode = self.root
        while currNode.next is not None:
            currNode = currNode.next
        currNode.next = trieNode
        currNode.next.prev = currNode
    def delete(self, trieNode):
        if self.root is None:
            raise Exception("There are no nodes left to delete!")
        if trieNode.prev:
            trieNode.prev.next = None
        else:
            self.root = None
def create_dict(plate):
    plate_dict = dict()
    for ch in plate:
        ch = ch.lower()
        if ch.isalpha():
            if ch not in plate_dict.keys():
                plate_dict.update({ch: 1})
            else:
                plate_dict[ch] += 1
    return plate_dict
def check_word(prev_tree, word, plate_dict):
    if prev_tree.root is not None:
        curr_node = prev_tree.root
    for ch in word:
        plate_dict = plate_dict.copy()
        if ch in plate_dict.keys():
            plate_dict[ch] -= 1
        if prev_tree.root is None:
            prev_tree.insert(TrieNode(ch, plate_dict))
            curr_node = prev_tree.root
        if curr_node is None:
            curr_node = TrieNode(ch, plate_dict)
            prev_tree.insert(curr_node)
            curr_node = curr_node.next
        elif ch == curr_node.value:
            curr_node = curr_node.next
        else:
            prev_tree.delete(curr_node)
            curr_node = TrieNode(ch, plate_dict)
            prev_tree.insert(curr_node)
            curr_node = curr_node.next
    return plate_dict
def search_prefix(vocab, plate):
    shortest = None
    prev_tree = TrieTree()
    plate_dict = create_dict(plate)
    for word in vocab:
        temp = check_word(prev_tree, word, plate_dict)
        if not any(v > 0 for v in temp.values()):
            if shortest is None:
                shortest = word
            elif len(shortest) > len(word):
                shortest = word
        print(word, shortest, temp)
    return shortest
vocab = ['enjoy', 'enjoying', 'joy', 'joyful', 'joyous', 'joyousness']
plate = 'NY10NJ'
ans = search_prefix(vocab, plate)
print("\nSolution...\nfor {} and {} is ...\n\n{}".format(vocab, plate, ans))