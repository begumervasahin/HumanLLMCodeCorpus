class TrieNode:
    def __init__(self):
        self.children = {}
        self.weight = 0
def add_word(root, word, weight):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
        if node.weight < weight:
            node.weight = weight
def find_max_weight(root, prefix):
    node = root
    for char in prefix:
        if char not in node.children:
            return -1
        node = node.children[char]
    return node.weight
def task1():
    root = TrieNode()
    n, q = map(int, input().split())
    for _ in range(n):
        word, weight = input().split()
        add_word(root, word, int(weight))
    for _ in range(q):
        query = input()
        print(find_max_weight(root, query))
class CommonPrefixNode:
    def __init__(self):
        self.children = {}
        self.common = 0
def add_word_with_prefix(root, word):
    node = root
    result = 0
    for level, char in enumerate(word):
        if char not in node.children:
            node.children[char] = CommonPrefixNode()
        node = node.children[char]
        node.common += 1
        result = max(result, node.common * (level + 1))
    return result
def task2():
    t = int(input())
    for case_num in range(t):
        root = CommonPrefixNode()
        result = 0
        n = int(input())
        for _ in range(n):
            result = max(result, add_word_with_prefix(root, input()))
        print(f'Case {case_num + 1}: {result}')
class ConsistencyNode:
    def __init__(self):
        self.children = {}
        self.count_word = 0
def add_word_with_consistency_check(root, word):
    node = root
    s_prefix_another = True
    another_prefix_s = False
    for char in word:
        if char not in node.children:
            node.children[char] = ConsistencyNode()
            s_prefix_another = False
        node = node.children[char]
        if node.count_word != 0:
            another_prefix_s = True
    node.count_word += 1
    return s_prefix_another or another_prefix_s
def task3():
    t = int(input())
    for case_num in range(t):
        n = int(input())
        is_inconsistent = False
        root = ConsistencyNode()
        for _ in range(n):
            if not is_inconsistent:
                is_inconsistent = add_word_with_consistency_check(root, input())
            else:
                input()
        print(f'Case {case_num + 1}: {"NO" if is_inconsistent else "YES"}')
class PasswordNode:
    def __init__(self):
        self.children = {}
        self.count_password = 0
def add_password(root, password):
    node = root
    s_prefix_another = True
    another_prefix_s = False
    for char in password:
        if char not in node.children:
            node.children[char] = PasswordNode()
            s_prefix_another = False
        node = node.children[char]
        if node.count_password != 0:
            another_prefix_s = True
    node.count_password += 1
    return s_prefix_another or another_prefix_s
def task4():
    n = int(input())
    root = PasswordNode()
    is_vulnerable = False
    for _ in range(n):
        if not is_vulnerable:
            is_vulnerable = add_password(root, input())
        else:
            input()
    print('vulnerable' if is_vulnerable else 'non vulnerable')
class ContactNode:
    def __init__(self):
        self.children = {}
        self.contact_count = 0
def add_contact(root, contact):
    node = root
    for char in contact:
        if char not in node.children:
            node.children[char] = ContactNode()
        node = node.children[char]
        node.contact_count += 1
def find_contact(root, prefix):
    node = root
    for char in prefix:
        if char not in node.children:
            return 0
        node = node.children[char]
    return node.contact_count
def task5():
    n = int(input())
    root = ContactNode()
    for _ in range(n):
        command, value = input().split()
        if command == 'add':
            add_contact(root, value)
        elif command == 'find':
            print(find_contact(root, value))
if __name__ == "__main__":
    task5()